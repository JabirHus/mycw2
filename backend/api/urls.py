from django.urls import path
from . import views

urlpatterns = [
    # Endpoint for handling a collection of patients
    path('patients/', views.patients_api, name='patients_api'),
    path('patient/<int:patient_id>/', views.patient_api, name='patient_api'),

    # Endpoint for handling a collection of treatments
    path('treatments/', views.treatments_api, name='treatments_api'),
    path('treatment/<int:treatment_id>/', views.treatment_api, name='treatment_api'),

    # Endpoint for managing patient-treatment relationships
    path('patient-treatments/', views.patient_treatments_api, name='patient_treatments_api'),
    path('patient-treatment/<int:patient_treatment_id>/', views.patient_treatment_api, name='patient_treatment_api'),
]
