from django.urls import path
from .views import *

urlpatterns = [
    path("patient/", PatientList.as_view(), name='patient_list'),
    path("patient/<int:pk>/", PatientDetail.as_view(), name='patient_detail'),
    path("patient/<int:pk>/update/", PatientUpdate.as_view(), name='patient_update'),
    path("patient/<int:pk>/delete/", PatientDelete.as_view(), name='patient_delete'),
    path("patient/create/", PatientCreate.as_view(), name='patient_create'),
    path("appointment/", AppointmentList.as_view(), name='appointment_list'),
    path("appointment/<int:pk>/", AppointmentDetail.as_view(), name='appointment_detail'),
    path('appointment/<int:pk>/update/', AppointmentUpdate.as_view(), name='appointment_update'),    
    path('appointment/<int:pk>/delete/', AppointmentDelete.as_view(), name='appointment_delete'),
    path('appointment/create/', AppointmentCreate.as_view(), name='appointment_create'),    
    path('prescription/', PrescriptionList.as_view(), name='prescription_list'),
    path('prescription/<int:pk>/', PrescriptionDetail.as_view(), name='prescription_detail'),
    path('prescription/<int:pk>/update/', PrescriptionUpdate.as_view(), name='prescription_update'),
    path('prescription/<int:pk>/delete/', PrescriptionDelete.as_view(), name='prescription_delete'),
    path('prescription/create/', PrescriptionCreate.as_view(), name='prescription_create'),
]