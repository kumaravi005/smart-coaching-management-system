from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash
from services.json_storage import load_data, append_data, update_data, delete_data
import uuid

resources_bp = Blueprint('resources', __name__)

# --- Teachers ---
@resources_bp.route('/teachers', methods=['GET', 'POST'])
def manage_teachers():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_teacher = {
                'id': str(uuid.uuid4()),
                'name': request.form.get('name'),
                'subjects': [s.strip() for s in request.form.get('subjects', '').split(',')],
                'availability': [a.strip() for a in request.form.get('availability', '').split(',')]
            }
            append_data('data/teachers.json', new_teacher)
            flash('Teacher added successfully.', 'success')
        elif action == 'delete':
            delete_data('data/teachers.json', request.form.get('id'))
            flash('Teacher deleted successfully.', 'success')
        return redirect(url_for('resources.manage_teachers'))
        
    teachers = load_data('data/teachers.json')
    return render_template('teachers.html', teachers=teachers)

# --- Rooms ---
@resources_bp.route('/rooms', methods=['GET', 'POST'])
def manage_rooms():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_room = {
                'id': str(uuid.uuid4()),
                'name': request.form.get('name'),
                'capacity': int(request.form.get('capacity', 0))
            }
            append_data('data/rooms.json', new_room)
            flash('Room added successfully.', 'success')
        elif action == 'delete':
            delete_data('data/rooms.json', request.form.get('id'))
            flash('Room deleted successfully.', 'success')
        return redirect(url_for('resources.manage_rooms'))
        
    rooms = load_data('data/rooms.json')
    return render_template('rooms.html', rooms=rooms)

# --- Timeslots ---
@resources_bp.route('/timeslots', methods=['GET', 'POST'])
def manage_timeslots():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_slot = {
                'id': str(uuid.uuid4()),
                'start_time': request.form.get('start_time'),
                'end_time': request.form.get('end_time'),
                'name': f"{request.form.get('start_time')}-{request.form.get('end_time')}"
            }
            append_data('data/timeslots.json', new_slot)
            flash('Timeslot added successfully.', 'success')
        elif action == 'delete':
            delete_data('data/timeslots.json', request.form.get('id'))
            flash('Timeslot deleted successfully.', 'success')
        return redirect(url_for('resources.manage_timeslots'))
        
    timeslots = load_data('data/timeslots.json')
    return render_template('timeslots.html', timeslots=timeslots)

# --- Classes ---
@resources_bp.route('/classes', methods=['GET', 'POST'])
def manage_classes():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_class = {
                'id': str(uuid.uuid4()),
                'subject': request.form.get('subject'),
                'students': int(request.form.get('students', 0)),
                'priority': int(request.form.get('priority', 1)),
                'allowed_merge_with': [s.strip() for s in request.form.get('allowed_merge_with', '').split(',') if s.strip()],
                'not_allowed_with': [s.strip() for s in request.form.get('not_allowed_with', '').split(',') if s.strip()],
                'fixed_group': request.form.get('fixed_group') == 'on'
            }
            append_data('data/classes.json', new_class)
            flash('Class added successfully.', 'success')
        elif action == 'delete':
            delete_data('data/classes.json', request.form.get('id'))
            flash('Class deleted successfully.', 'success')
        return redirect(url_for('resources.manage_classes'))
        
    classes = load_data('data/classes.json')
    return render_template('classes.html', classes=classes)
