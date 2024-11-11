import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient, Treatment, PatientTreatment


@csrf_exempt
def patients_api(request):
    """API endpoint for the collection of patients"""
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = Patient.objects.create(
            name=data['name'],
            date_of_birth=data['date_of_birth'],
            contact_info=data['contact_info']
        )
        return JsonResponse({
            'id': patient.id,
            'name': patient.name,
            'date_of_birth': patient.date_of_birth,
            'contact_info': patient.contact_info
        })

    patients = list(Patient.objects.values())
    return JsonResponse({'patients': patients})


@csrf_exempt
def patient_api(request, patient_id):
    """API endpoint for a single patient"""
    try:
        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        patient.name = data['name']
        patient.date_of_birth = data['date_of_birth']
        patient.contact_info = data['contact_info']
        patient.save()
        return JsonResponse({
            'id': patient.id,
            'name': patient.name,
            'date_of_birth': patient.date_of_birth,
            'contact_info': patient.contact_info
        })

    if request.method == 'DELETE':
        patient.delete()
        return JsonResponse({})

    return JsonResponse({
        'id': patient.id,
        'name': patient.name,
        'date_of_birth': patient.date_of_birth,
        'contact_info': patient.contact_info
    })


@csrf_exempt
def treatments_api(request):
    """API endpoint for the collection of treatments"""
    if request.method == 'POST':
        data = json.loads(request.body)
        treatment = Treatment.objects.create(
            name=data['name'],
            description=data['description']
        )
        return JsonResponse({
            'id': treatment.id,
            'name': treatment.name,
            'description': treatment.description
        })

    treatments = list(Treatment.objects.values())
    return JsonResponse({'treatments': treatments})


@csrf_exempt
def treatment_api(request, treatment_id):
    """API endpoint for a single treatment"""
    try:
        treatment = Treatment.objects.get(id=treatment_id)
    except Treatment.DoesNotExist:
        return JsonResponse({'error': 'Treatment not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        treatment.name = data['name']
        treatment.description = data['description']
        treatment.save()
        return JsonResponse({
            'id': treatment.id,
            'name': treatment.name,
            'description': treatment.description
        })

    if request.method == 'DELETE':
        treatment.delete()
        return JsonResponse({})

    return JsonResponse({
        'id': treatment.id,
        'name': treatment.name,
        'description': treatment.description
    })


@csrf_exempt
def patient_treatments_api(request):
    """API endpoint for managing PatientTreatment relationships"""
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = Patient.objects.get(id=data['patient_id'])
        treatment = Treatment.objects.get(id=data['treatment_id'])
        patient_treatment = PatientTreatment.objects.create(
            patient=patient,
            treatment=treatment,
            treatment_date=data['treatment_date']
        )
        return JsonResponse({
            'id': patient_treatment.id,
            'patient': patient_treatment.patient.id,
            'treatment': patient_treatment.treatment.id,
            'treatment_date': patient_treatment.treatment_date
        })

    patient_treatments = list(PatientTreatment.objects.values())
    return JsonResponse({'patient_treatments': patient_treatments})


@csrf_exempt
def patient_treatments_api(request):
    """API endpoint for managing PatientTreatment relationships"""
    if request.method == 'POST':
        data = json.loads(request.body)
        patient = Patient.objects.get(id=data['patient_id'])
        treatment = Treatment.objects.get(id=data['treatment_id'])
        patient_treatment = PatientTreatment.objects.create(
            patient=patient,
            treatment=treatment,
            treatment_date=data['treatment_date']
        )
        return JsonResponse({
            'id': patient_treatment.id,
            'patient_id': patient.id,
            'patient_name': patient.name,  # Include patient name
            'treatment_id': treatment.id,
            'treatment_name': treatment.name,  # Include treatment name
            'treatment_date': patient_treatment.treatment_date
        })

    # GET request to return all patient-treatment records with names
    patient_treatments = PatientTreatment.objects.select_related('patient', 'treatment').all()
    response_data = [{
        'id': pt.id,
        'patient_id': pt.patient.id,
        'patient_name': pt.patient.name,  # Patient name for display
        'treatment_id': pt.treatment.id,
        'treatment_name': pt.treatment.name,  # Treatment name for display
        'treatment_date': pt.treatment_date
    } for pt in patient_treatments]
    return JsonResponse({'patient_treatments': response_data})

