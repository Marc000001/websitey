from django.urls import path
from staff.views import PatientDetailView, PatientListView, addPatient, updatePatient, deletePatient, list_patient, \
    result, add_note, delete_note, list_ward

urlpatterns = [
    path('addPatient/', addPatient, name='addPatient'),
    path('updatePatient/<int:pk>/', updatePatient, name='updatePatient'),
    path('deletePatient/<int:pk>/', deletePatient, name='deletePatient'),

    path('patients/', list_patient, name='patient_list'),
    path('patients/<int:pk>', PatientDetailView.as_view(), name='detailed'),
    path('result/', result, name='result'),
    path('patients/<int:pk>/add-note/', add_note, name='add-note'),
    path('patients/<int:pk>/delete-note/', delete_note, name='delete-note'),
    path('wardlist/', list_ward, name='wardlist')
]
