from django.contrib import admin
from .models import Patient, Treatment, PatientTreatment

# Register the new models
admin.site.register(Patient)
admin.site.register(Treatment)
admin.site.register(PatientTreatment)
