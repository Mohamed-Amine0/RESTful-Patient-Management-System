from django.db import models

# Class Patient that have a cin, name, sex and age
class Patient(models.Model):
    # the cin is unique
    cin = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# Class Appointment that have a patient, date and time
class Appointment(models.Model):
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        # concatenate the patient name with datetime.date and datetime.time
        return self.patientId.name + " " + str(self.date) + " " + str(self.time)
    
# Class Prescription that have a patient, date, time from an Appointment and a description
class Prescription(models.Model):
    appointmentId = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.appointmentId.patientId.name + " " + str(self.appointmentId.date) + " " + str(self.appointmentId.time) + " " + self.description