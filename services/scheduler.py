import random
from services.json_storage import load_data, save_data

def generate_schedule():
    """
    Constraint-based scheduling engine using Dynamic Rules.
    Phase 1: Greedy Allocation with Merging Logic
    Phase 2: Optimization (minimize unused capacity)
    """
    teachers = load_data('data/teachers.json')
    rooms = load_data('data/rooms.json')
    timeslots = load_data('data/timeslots.json')
    classes = load_data('data/classes.json')

    # Normalize class data structure
    for c in classes:
        c['students'] = c.get('students', c.get('students_count', 0))
        c['subject'] = c.get('subject', c.get('name', 'Unknown'))
        c['allowed_merge_with'] = c.get('allowed_merge_with', [])
        c['not_allowed_with'] = c.get('not_allowed_with', [])
        c['fixed_group'] = c.get('fixed_group', False)

    # Sort classes: Priority ascending (1 is highest), then by students descending
    sorted_classes = sorted(classes, key=lambda x: (x.get('priority', 99), -x.get('students', 0)))
    
    schedule = []
    
    # Resource tracking: Map timeslot -> List of IDs
    used_rooms_by_timeslot = {ts['name']: [] for ts in timeslots}
    used_teachers_by_timeslot = {ts['name']: [] for ts in timeslots}
    
    class_assigned = set()
    
    for cls in sorted_classes:
        if cls['id'] in class_assigned:
            continue
            
        # 1. Class Merging Logic
        merge_group = [cls]
        total_students = cls['students']
        
        if not cls['fixed_group'] and cls['allowed_merge_with']:
            for other in sorted_classes:
                if other['id'] in class_assigned or other['id'] == cls['id'] or other['fixed_group']:
                    continue
                
                # Check explicit merge constraints
                # Allow merge if mutually allowed, or one allows the other (soft fallback)
                if other['subject'] in cls['allowed_merge_with'] or cls['subject'] in other['allowed_merge_with']:
                    
                    # Verify 'not_allowed_with' conflict
                    conflict = False
                    for member in merge_group:
                        if other['subject'] in member['not_allowed_with'] or member['subject'] in other['not_allowed_with']:
                            conflict = True
                            break
                    
                    if not conflict:
                        merge_group.append(other)
                        total_students += other['students']

        # 2. Assign Resources
        assigned = False
        reason = ""
        
        group_subjects = [c['subject'] for c in merge_group]
        class_name_str = " + ".join(group_subjects)
        
        # Primary subject determines teacher requirements for simplicity
        primary_subject = cls['subject']
        eligible_teachers = [t for t in teachers if primary_subject in t.get('subjects', [])]
        
        if not eligible_teachers:
            reason = f"No teacher available for subject: {primary_subject}"
        else:
            eligible_rooms = [r for r in rooms if r.get('capacity', 0) >= total_students]
            
            if not eligible_rooms:
                reason = f"Capacity exceeded: No room large enough for {total_students} students"
            else:
                for ts in timeslots:
                    ts_name = ts['name']
                    
                    # Find available resources for this timeslot
                    avail_teachers = [t for t in eligible_teachers if ts_name in t.get('availability', []) and t['id'] not in used_teachers_by_timeslot[ts_name]]
                    avail_rooms = [r for r in eligible_rooms if r['id'] not in used_rooms_by_timeslot[ts_name]]
                    
                    if avail_teachers and avail_rooms:
                        # Optimization: Pick the smallest room that fits to minimize unused capacity
                        avail_rooms.sort(key=lambda r: r['capacity'])
                        best_room = avail_rooms[0]
                        teacher = avail_teachers[0]
                        
                        schedule.append({
                            "status": "assigned",
                            "class": class_name_str,
                            "students": total_students,
                            "teacher": teacher['name'],
                            "room": best_room['name'],
                            "timeslot": ts_name
                        })
                        
                        # Mark resources as used
                        used_teachers_by_timeslot[ts_name].append(teacher['id'])
                        used_rooms_by_timeslot[ts_name].append(best_room['id'])
                        assigned = True
                        
                        # Mark classes as assigned
                        for c in merge_group:
                            class_assigned.add(c['id'])
                        
                        break
                
                if not assigned:
                    reason = "Constraint violation: No overlapping availability for teacher, room, and timeslot"
        
        # 3. Conflict Handling (Unassigned)
        if not assigned:
            # If the group failed, we just record the primary class as unassigned. 
            # In a more advanced engine, we would try to decouple the merge group, but this satisfies the requirements.
            schedule.append({
                "status": "unassigned",
                "class": cls['subject'],
                "students": cls['students'],
                "reason": reason
            })
            class_assigned.add(cls['id'])

    # Final optimization phase hook (e.g. gap reduction, though currently handled by greedy sorting)
    
    save_data('data/schedule.json', schedule)
    return schedule
