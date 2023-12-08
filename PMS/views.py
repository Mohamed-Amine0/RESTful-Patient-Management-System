from rest_framework import generics
from .models import *
from .serializers import PatientSerializer, AppointmentSerializer, PrescriptionSerializer

from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView


# AppointmentList and AppointmentDetail are used to list and detail the appointments

class AppointmentList(View):
    template_name = 'pms/appointment/appointment_list.html'

    def get(self, request, *args, **kwargs):
        appointments = Appointment.objects.all()
        return render(request, self.template_name, {'appointments': appointments})

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    template_name = 'pms/appointment/appointment_detail.html'

    def get(self, request, pk, *args, **kwargs):
        appointment = Appointment.objects.get(pk=pk)
        return render(request, self.template_name, {'appointment': appointment})

class AppointmentUpdate(UpdateView):
    model = Appointment
    template_name = 'pms/appointment/appointment_update.html'
    fields = ['patientId', 'date', 'time']
    success_url = reverse_lazy('appointment_list')


class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'pms/appointment/appointment_delete.html'
    success_url = reverse_lazy('appointment_list')

class AppointmentCreate(CreateView): 
    model = Appointment
    fields = ['patientId', 'date', 'time']
    template_name = 'pms/appointment/appointment_create.html'
    success_url = reverse_lazy('appointment_list')

# PatientList and PatientDetail are used to list and detail the patients

class PatientList(View):
    template_name = 'pms/patient/patient_list.html'

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        return render(request, self.template_name, {'patients': patients})

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    template_name = 'pms/patient/patient_detail.html'

    def get(self, request, pk, *args, **kwargs):
        patient = Patient.objects.get(pk=pk)
        return render(request, self.template_name, {'patient': patient})

class PatientUpdate(UpdateView):
    model = Patient
    template_name = 'pms/patient/patient_update.html'
    fields = ['name', 'cin', 'sex', 'age']
    success_url = reverse_lazy('patient_list')

class PatientDelete(DeleteView):
    model = Patient
    template_name = 'pms/patient/patient_delete.html'
    success_url = reverse_lazy('patient_list')

class PatientCreate(CreateView):
    model = Patient
    fields = ['cin', 'name', 'sex', 'age']
    template_name = 'pms/patient/patient_create.html'
    success_url = reverse_lazy('patient_list')

#PrescriptionList and PrescriptionDetail are used to list and detail the prescriptions
#http://127.0.0.1:8000/PMS/prescription/?patient_name=Mary Brown

class PrescriptionList(View):
    template_name = 'pms/prescription/prescription_list.html'

    def get(self, request, *args, **kwargs):
        prescriptions = Prescription.objects.all()
        return render(request, self.template_name, {'prescriptions': prescriptions})

class PrescriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrescriptionSerializer
    queryset = Prescription.objects.all()

    template_name = 'pms/prescription/prescription_detail.html'

    def get(self, request, pk, *args, **kwargs):
        prescription = Prescription.objects.get(pk=pk)
        return render(request, self.template_name, {'prescription': prescription})

class PrescriptionUpdate(UpdateView):
    model = Prescription
    template_name = 'pms/prescription/prescription_update.html'
    fields = ['appointmentId', 'description']
    success_url = reverse_lazy('prescription_list')

class PrescriptionDelete(DeleteView):
    model = Prescription
    template_name = 'pms/prescription/prescription_delete.html'
    success_url = reverse_lazy('prescription_list')

class PrescriptionCreate(CreateView):
    model = Prescription
    fields = ['appointmentId', 'description']
    template_name = 'pms/prescription/prescription_create.html'
    success_url = reverse_lazy('prescription_list')