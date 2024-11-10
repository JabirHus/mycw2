from django.db import models

class Patient(models.Model):
    """Patient model"""
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Treatment(models.Model):
    """Treatment model"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    patients = models.ManyToManyField(Patient, through='PatientTreatment')

    def __str__(self):
        return self.name


class PatientTreatment(models.Model):
    """Through model linking Patient and Treatment with an extra field"""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    treatment_date = models.DateField()

    def __str__(self):
        return f"{self.patient} - {self.treatment} on {self.treatment_date}"
