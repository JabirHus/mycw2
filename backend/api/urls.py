from django.urls import path
from . import views

urlpatterns = [
    # Patient URLs
    path('patients/', views.patients_api, name='patients_api'),
    path('patient/<int:patient_id>/', views.patient_api, name='patient_api'),

    # Treatment URLs
    path('treatments/', views.treatments_api, name='treatments_api'),
    path('treatment/<int:treatment_id>/', views.treatment_api, name='treatment_api'),

    # PatientTreatment URLs
    path('patient-treatments/', views.patient_treatments_api, name='patient_treatments_api'),
    path('patient-treatment/<int:patient_treatment_id>/', views.patient_treatment_api, name='patient_treatment_api'),
]
