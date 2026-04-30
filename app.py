from flask import Flask, render_template, redirect, url_for, session
from routes.auth import auth_bp
from routes.resources import resources_bp
from routes.schedule import schedule_bp
from services.json_storage import load_data

app = Flask(__name__)
app.secret_key = 'super_secret_coaching_key'

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(resources_bp)
app.register_blueprint(schedule_bp)

@app.before_request
def require_login():
    from flask import request
    allowed_routes = ['auth.login', 'static']
    if request.endpoint not in allowed_routes and not session.get('logged_in'):
        return redirect(url_for('auth.login'))

@app.route('/')
def index():
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    teachers = load_data('data/teachers.json')
    rooms = load_data('data/rooms.json')
    classes = load_data('data/classes.json')
    
    stats = {
        'teachers_count': len(teachers),
        'rooms_count': len(rooms),
        'classes_count': len(classes)
    }
    return render_template('dashboard.html', stats=stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
