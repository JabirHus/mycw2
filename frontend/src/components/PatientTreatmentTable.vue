<template>
    <div>
        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addPatientTreatmentModal">
            <i class="bi bi-plus"></i> Add Patient-Treatment
        </button>

        <!-- Table for displaying patient-treatment relationships -->
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Patient Name</th>
                    <th>Treatment Name</th>
                    <th>Treatment Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(relation, index) in patientTreatments" :key="relation.id">
                    <td>{{ index + 1 }}</td>
                    <td>{{ relation.patient_name }}</td>
                    <td>{{ relation.treatment_name }}</td>
                    <td>{{ relation.treatment_date }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary me-2" @click="openEditModal(relation)">
                            <i class="bi bi-pencil"></i> Edit
                        </button>
                        <button class="btn btn-sm btn-danger" @click="deletePatientTreatment(relation.id)">
                            <i class="bi bi-trash"></i> Delete
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Add Patient-Treatment Modal -->
        <div class="modal fade" id="addPatientTreatmentModal" tabindex="-1" aria-labelledby="addPatientTreatmentModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addPatientTreatmentModalLabel">Add Patient-Treatment</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <select v-model="newRelation.patient_id" class="form-control mb-2">
                            <option disabled value="">Select Patient</option>
                            <option v-for="patient in patients" :key="patient.id" :value="patient.id">
                                {{ patient.name }}
                            </option>
                        </select>
                        <select v-model="newRelation.treatment_id" class="form-control mb-2">
                            <option disabled value="">Select Treatment</option>
                            <option v-for="treatment in treatments" :key="treatment.id" :value="treatment.id">
                                {{ treatment.name }}
                            </option>
                        </select>
                        <input v-model="newRelation.treatment_date" type="date" class="form-control mb-2" placeholder="Treatment Date">
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createPatientTreatment" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Patient-Treatment Modal -->
        <div class="modal fade" id="editPatientTreatmentModal" tabindex="-1" aria-labelledby="editPatientTreatmentModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editPatientTreatmentModalLabel">Edit Patient-Treatment</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <label for="edit-treatment-date" class="form-label">Treatment Date</label>
                        <input v-model="editRelationData.treatment_date" type="date" class="form-control mb-2" id="edit-treatment-date" placeholder="Treatment Date">
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updatePatientTreatment" data-bs-dismiss="modal">Save Changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js'; // Ensure Bootstrap is imported

const baseUrl = 'http://localhost:8000';

export default {
    data() {
        return {
            patientTreatments: [],
            patients: [],
            treatments: [],
            newRelation: {
                patient_id: '',
                treatment_id: '',
                treatment_date: ''
            },
            editRelationData: {}
        }
    },
    async mounted() {
        await this.fetchPatientTreatments();
        await this.fetchPatients();
        await this.fetchTreatments();
    },
    methods: {
        async fetchPatientTreatments() {
            const response = await fetch(`${baseUrl}/api/patient-treatments/`);
            const data = await response.json();
            this.patientTreatments = data.patient_treatments;
        },
        async fetchPatients() {
            const response = await fetch(`${baseUrl}/api/patients/`);
            const data = await response.json();
            this.patients = data.patients;
        },
        async fetchTreatments() {
            const response = await fetch(`${baseUrl}/api/treatments/`);
            const data = await response.json();
            this.treatments = data.treatments;
        },
        async createPatientTreatment() {
            const response = await fetch(`${baseUrl}/api/patient-treatments/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(this.newRelation)
            });
            const newRelation = await response.json();
            this.patientTreatments.push(newRelation);
            this.newRelation = { patient_id: '', treatment_id: '', treatment_date: '' };
        },
        async deletePatientTreatment(id) {
            const response = await fetch(`${baseUrl}/api/patient-treatment/${id}/`, {
                method: 'DELETE'
            });
            if (response.ok) {
                this.patientTreatments = this.patientTreatments.filter(relation => relation.id !== id);
            }
        },
        openEditModal(relation) {
            this.editRelationData = { ...relation };
            const modal = new bootstrap.Modal(document.getElementById('editPatientTreatmentModal'));
            modal.show();
        },
        async updatePatientTreatment() {
            const response = await fetch(`${baseUrl}/api/patient-treatment/${this.editRelationData.id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ treatment_date: this.editRelationData.treatment_date })
            });
            if (response.ok) {
                const updatedRelation = await response.json();
                const index = this.patientTreatments.findIndex(rel => rel.id === updatedRelation.id);
                this.patientTreatments[index] = updatedRelation;
            }
        }
    }
}
</script>

<style scoped>
</style>
