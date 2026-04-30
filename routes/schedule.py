from flask import Blueprint, render_template, jsonify, flash, redirect, url_for
from services.scheduler import generate_schedule as run_scheduler
from services.json_storage import load_data

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/schedule')
def view_schedule():
    schedule = load_data('data/schedule.json')
    return render_template('schedule.html', schedule=schedule)

@schedule_bp.route('/generate-schedule', methods=['POST'])
def generate_schedule():
    try:
        schedule = run_scheduler()
        flash('Schedule generated successfully!', 'success')
    except Exception as e:
        flash(f'Error generating schedule: {str(e)}', 'danger')
    return redirect(url_for('schedule.view_schedule'))
