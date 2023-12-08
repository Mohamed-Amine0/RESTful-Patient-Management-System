# Patient Management System (PMS)

This is a Django-based Restful web application for managing patients, appointments, and prescriptions.

## Starting a Django Project Guide

### 1. Install Django and Django Rest Framework
```bash
$ pip install django
$ pip install djangorestframework
```

### 2. Create a new Django project and app
```bash
$ django-admin startproject storage .
$ django-admin startapp nameApp
```

### 3. Configure Project Settings
- Open **storage/settings.py**
- Add the app to `INSTALLED_APPS`:
  ```python
  INSTALLED_APPS = [
      # ...
      "nameApp.apps.PmsConfig",
      "rest_framework",
  ]
  ```

### 4. Create Necessary Folders
Create the following folders and files:
- api/urls.py
- api/serializers.py

### 5. Define Database Entities
- Define classes/objects in **nameApp/models.py** for your database entities (e.g., student, teacher).

### 6. Register Models in Admin Panel
- Go to **nameApp/admin.py** and import your models.

### 7. Run Migrations
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

### 8. Create Serializers
- Define serializers for each class in **nameApp/serializers.py** to convert data from SQL to JSON.

### 9. Create Views
- Define methods and functions in **nameApp/views.py** to handle data and build your app.

### 10. Define URLs
- Define URL patterns in **nameApp/urls.py**.

### 11. Include API URLs in Project URLs
- Open **storage/urls.py**
- Include the API URLs:
  ```python
  from django.contrib import admin
  from django.urls import include, path

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('nameApp.urls')),
  ]
  ```

### 12. Start the App
```bash
$ python manage.py runserver
```

**Hierarchy Summary:**
- Project Settings: `nameProject/settings`
- App Models: `nameApp/models`
- Admin Registration: `nameApp/admin`
- Serializers: `nameApp/serializers`
- Views: `nameApp/views`
- URLs: `nameApp/urls`
- Project URLs: `nameProject/urls`

Follow these steps to set up and run your Django project.

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

## Usage

Navigate to `http://localhost:8000/PMS/patient/` to access the application.
