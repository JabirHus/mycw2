<template>
    <div>
        <h1>Healthcare Management System</h1>

        <!-- Bootstrap Tabs for Navigation -->
        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="patients-tab" data-bs-toggle="tab" data-bs-target="#patients" type="button" role="tab" aria-controls="patients" aria-selected="true">
                    Patients
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="treatments-tab" data-bs-toggle="tab" data-bs-target="#treatments" type="button" role="tab" aria-controls="treatments" aria-selected="false">
                    Treatments
                </button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="patient-treatments-tab" data-bs-toggle="tab" data-bs-target="#patient-treatments" type="button" role="tab" aria-controls="patient-treatments" aria-selected="false">
                    Patient-Treatments
                </button>
            </li>
        </ul>

        <div class="tab-content" id="myTabContent">
            <!-- Patients Tab -->
            <div class="tab-pane fade show active" id="patients" role="tabpanel" aria-labelledby="patients-tab">
                <PatientTable
                    :patients="patients"
                    @delete-patient="deletePatient"
                    @update-patient="openEditPatientModal"
                    @add-patient="openAddPatientModal"
                />
            </div>

            <!-- Treatments Tab -->
            <div class="tab-pane fade" id="treatments" role="tabpanel" aria-labelledby="treatments-tab">
                <TreatmentTable
                    :treatments="treatments"
                    @delete-treatment="deleteTreatment"
                    @update-treatment="openEditTreatmentModal"
                    @add-treatment="openAddTreatmentModal"
                />
            </div>

            <!-- Patient-Treatments Tab -->
            <div class="tab-pane fade" id="patient-treatments" role="tabpanel" aria-labelledby="patient-treatments-tab">
                <PatientTreatmentTable
                    :patient-treatments="patientTreatments"
                    :patients="patients"
                    :treatments="treatments"
                    @delete-patient-treatment="deletePatientTreatment"
                    @update-patient-treatment="openEditPatientTreatmentModal"
                    @add-patient-treatment="openAddPatientTreatmentModal"
                />
            </div>
        </div>

        <!-- Add and Edit Modals for Patients, Treatments, and Patient-Treatments -->
        <!-- Example for Add and Edit Patient Modals -->
        <!-- Add similar modals for Treatments and Patient-Treatments -->
        <div class="modal fade" id="addPatientModal" tabindex="-1" aria-labelledby="addPatientModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addPatientModalLabel">Add Patient</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="newPatient.name" placeholder="Name" class="form-control mb-2" />
                        <input v-model="newPatient.date_of_birth" placeholder="Date of Birth" type="date" class="form-control mb-2" />
                        <input v-model="newPatient.contact_info" placeholder="Contact Info" class="form-control mb-2" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createPatient" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="modal fade" id="editPatientModal" tabindex="-1" aria-labelledby="editPatientModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editPatientModalLabel">Edit Patient</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <input v-model="editPatient.name" placeholder="Name" class="form-control mb-2" />
                        <input v-model="editPatient.date_of_birth" placeholder="Date of Birth" type="date" class="form-control mb-2" />
                        <input v-model="editPatient.contact_info" placeholder="Contact Info" class="form-control mb-2" />
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updatePatient" data-bs-dismiss="modal">Save Changes</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Similar add and edit modals for Treatments and Patient-Treatments -->

    </div>
</template>

<script>
import { nextTick } from 'vue';
import PatientTable from './components/PatientTable.vue';
import TreatmentTable from './components/TreatmentTable.vue';
import PatientTreatmentTable from './components/PatientTreatmentTable.vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js';

const baseUrl = 'http://localhost:8000';

export default {
    components: { PatientTable, TreatmentTable, PatientTreatmentTable },
    data() {
        return {
            patients: [],
            treatments: [],
            patientTreatments: [],
            newPatient: { name: '', date_of_birth: '', contact_info: '' },
            editPatient: { id: '', name: '', date_of_birth: '', contact_info: '' },
            newTreatment: { name: '', description: '' },
            editTreatment: { id: '', name: '', description: '' },
            newPatientTreatment: { patient_id: '', treatment_id: '', treatment_date: '' },
            editPatientTreatment: { id: '', patient_id: '', treatment_id: '', treatment_date: '' },
        };
    },
    async mounted() {
        await this.fetchPatients();
        await this.fetchTreatments();
        await this.fetchPatientTreatments();
    },
    methods: {
        // Fetch methods for initializing data
        async fetchPatients() {
            try {
                const response = await fetch(`${baseUrl}/api/patients/`);
                const data = await response.json();
                this.patients = data.patients;
            } catch (error) {
                console.error('Error fetching patients:', error);
            }
        },
        async fetchTreatments() {
            try {
                const response = await fetch(`${baseUrl}/api/treatments/`);
                const data = await response.json();
                this.treatments = data.treatments;
            } catch (error) {
                console.error('Error fetching treatments:', error);
            }
        },
        async fetchPatientTreatments() {
            try {
                const response = await fetch(`${baseUrl}/api/patient-treatments/`);
                const data = await response.json();
                this.patientTreatments = data.patient_treatments;
            } catch (error) {
                console.error('Error fetching patient-treatments:', error);
            }
        },

        // Methods for creating records
        async createPatient() {
            try {
                const response = await fetch(`${baseUrl}/api/patients/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newPatient)
                });
                const patient = await response.json();
                this.patients.push(patient);
                this.newPatient = { name: '', date_of_birth: '', contact_info: '' };
            } catch (error) {
                console.error('Error adding patient:', error);
            }
        },
        async createTreatment() {
            try {
                const response = await fetch(`${baseUrl}/api/treatments/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newTreatment)
                });
                const treatment = await response.json();
                this.treatments.push(treatment);
                this.newTreatment = { name: '', description: '' };
            } catch (error) {
                console.error('Error adding treatment:', error);
            }
        },
        async createPatientTreatment() {
            try {
                const response = await fetch(`${baseUrl}/api/patient-treatments/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.newPatientTreatment)
                });
                const relation = await response.json();
                this.patientTreatments.push(relation);
                this.newPatientTreatment = { patient_id: '', treatment_id: '', treatment_date: '' };
            } catch (error) {
                console.error('Error adding patient treatment:', error);
            }
        },

        // Methods for updating records
        async updatePatient() {
            try {
                const response = await fetch(`${baseUrl}/api/patients/${this.editPatient.id}/`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.editPatient)
                });
                const updatedPatient = await response.json();
                const index = this.patients.findIndex(patient => patient.id === updatedPatient.id);
                if (index !== -1) this.patients.splice(index, 1, updatedPatient);
            } catch (error) {
                console.error('Error updating patient:', error);
            }
        },
        async updateTreatment() {
            try {
                const response = await fetch(`${baseUrl}/api/treatments/${this.editTreatment.id}/`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.editTreatment)
                });
                const updatedTreatment = await response.json();
                const index = this.treatments.findIndex(treatment => treatment.id === updatedTreatment.id);
                if (index !== -1) this.treatments.splice(index, 1, updatedTreatment);
            } catch (error) {
                console.error('Error updating treatment:', error);
            }
        },
        async updatePatientTreatment() {
            try {
                const response = await fetch(`${baseUrl}/api/patient-treatments/${this.editPatientTreatment.id}/`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.editPatientTreatment)
                });
                const updatedRelation = await response.json();
                const index = this.patientTreatments.findIndex(rel => rel.id === updatedRelation.id);
                if (index !== -1) this.patientTreatments.splice(index, 1, updatedRelation);
            } catch (error) {
                console.error('Error updating patient treatment:', error);
            }
        },

        // Methods for deleting records
        async deletePatient(id) {
            try {
                await fetch(`${baseUrl}/api/patients/${id}/`, { method: 'DELETE' });
                this.patients = this.patients.filter(patient => patient.id !== id);
            } catch (error) {
                console.error('Error deleting patient:', error);
            }
        },
        async deleteTreatment(id) {
            try {
                await fetch(`${baseUrl}/api/treatments/${id}/`, { method: 'DELETE' });
                this.treatments = this.treatments.filter(treatment => treatment.id !== id);
            } catch (error) {
                console.error('Error deleting treatment:', error);
            }
        },
        async deletePatientTreatment(id) {
            try {
                await fetch(`${baseUrl}/api/patient-treatments/${id}/`, { method: 'DELETE' });
                this.patientTreatments = this.patientTreatments.filter(rel => rel.id !== id);
            } catch (error) {
                console.error('Error deleting patient treatment:', error);
            }
        },

        // Modal management methods
        openAddPatientModal() {
            nextTick(() => new bootstrap.Modal(document.getElementById('addPatientModal')).show());
        },
        openEditPatientModal(patient) {
            this.editPatient = { ...patient };
            nextTick(() => new bootstrap.Modal(document.getElementById('editPatientModal')).show());
        },
        openAddTreatmentModal() {
            nextTick(() => new bootstrap.Modal(document.getElementById('addTreatmentModal')).show());
        },
        openEditTreatmentModal(treatment) {
            this.editTreatment = { ...treatment };
            nextTick(() => new bootstrap.Modal(document.getElementById('editTreatmentModal')).show());
        },
        openAddPatientTreatmentModal() {
            nextTick(() => new bootstrap.Modal(document.getElementById('addPatientTreatmentModal')).show());
        },
        openEditPatientTreatmentModal(relation) {
            this.editPatientTreatment = { ...relation };
            nextTick(() => new bootstrap.Modal(document.getElementById('editPatientTreatmentModal')).show());
        }
    }
};
</script>
