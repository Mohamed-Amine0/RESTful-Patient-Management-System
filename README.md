# Patient Management System (PMS)

This is a Django-based web application for managing patients, appointments, and prescriptions.

## Project Structure

- `db.sqlite3`: The SQLite database file.
- `manage.py`: The Django management script.
- `PMS/models.py`: Contains the data models for the application.
- `PMS/serializers.py`: Contains the serializers for the data models.
- `PMS/views.py`: Contains the views for the application.
- `storage/urls.py`: The main URL configuration for the project.

## Models

- `Appointment`: Represents an appointment with fields for date and time.
- `Patient`: Represents a patient with fields for CIN, name, sex, and age.
- `Prescription`: Represents a prescription with a description field.

## Views

- `AppointmentList`, `AppointmentDetail`, `AppointmentUpdate`, `AppointmentDelete`, `AppointmentCreate`: Views for listing, detailing, updating, deleting, and creating appointments.
- `PatientList`, `PatientDetail`, `PatientUpdate`, `PatientDelete`, `PatientCreate`: Views for listing, detailing, updating, deleting, and creating patients.
- `PrescriptionList`, `PrescriptionDetail`, `PrescriptionUpdate`, `PrescriptionDelete`, `PrescriptionCreate`: Views for listing, detailing, updating, deleting, and creating Prescriptions.

## Setup

1. Clone the repository.
2. Install django and django rest framwork :
```
    $pip install django
    $pip install djangorestframework
```
3. Run the migrations: `python manage.py migrate`.
4. Start the server: `python manage.py runserver`.

## Usage

Navigate to `http://localhost:8000/PMS/patient/` to access the application.
