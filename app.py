from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data for doctors and appointments
doctors = ["Dr. Smith", "Dr. Johnson", "Dr. Davis"]
appointments = []

# Explicitly set the host and port
host = '0.0.0.0'
port = 5000

@app.route('/')
def index():
    return render_template('index.html', doctors=doctors, appointments=appointments)

@app.route('/schedule', methods=['POST'])
def schedule():
    if request.method == 'POST':
        doctor = request.form.get('doctor')
        date = request.form.get('date')
        time = request.form.get('time')
        patient_name = request.form.get('patient_name')
        appointment = {
            'doctor': doctor,
            'date': date,
            'time': time,
            'patient_name': patient_name,
        }
        appointments.append(appointment)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)

