<template>
    <div>
        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addPatientModal">
            <i class="bi bi-plus"></i> Add Patient
        </button>

        <!-- Patient Table -->
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Date of Birth</th>
                    <th>Contact Info</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(patient, index) in patients" :key="patient.id">
                    <th>{{ index + 1 }}</th>
                    <td>{{ patient.name }}</td>
                    <td>{{ patient.date_of_birth }}</td>
                    <td>{{ patient.contact_info }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary me-2" @click="openEditModal(patient)">Edit</button>
                        <button class="btn btn-sm btn-danger" @click="deletePatient(patient.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Add Patient Modal -->
        <div class="modal fade" id="addPatientModal" tabindex="-1" aria-labelledby="addPatientModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addPatientModalLabel">Add Patient</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newPatient.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="date_of_birth" class="form-label">Date of Birth</label>
                            <input v-model="newPatient.date_of_birth" type="date" class="form-control" id="date_of_birth">
                        </div>
                        <div class="mb-3">
                            <label for="contact_info" class="form-label">Contact Info</label>
                            <input v-model="newPatient.contact_info" type="text" class="form-control" id="contact_info">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createPatient" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Patient Modal -->
        <div class="modal fade" id="editPatientModal" tabindex="-1" aria-labelledby="editPatientModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editPatientModalLabel">Edit Patient</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="edit_name" class="form-label">Name</label>
                            <input v-model="editPatientData.name" type="text" class="form-control" id="edit_name">
                        </div>
                        <div class="mb-3">
                            <label for="edit_date_of_birth" class="form-label">Date of Birth</label>
                            <input v-model="editPatientData.date_of_birth" type="date" class="form-control" id="edit_date_of_birth">
                        </div>
                        <div class="mb-3">
                            <label for="edit_contact_info" class="form-label">Contact Info</label>
                            <input v-model="editPatientData.contact_info" type="text" class="form-control" id="edit_contact_info">
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updatePatient" data-bs-dismiss="modal">Save Changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js';  // Import Bootstrap JavaScript

const baseUrl = 'http://localhost:8000';

export default {
    data() {
        return {
            patients: [],
            newPatient: {
                name: '',
                date_of_birth: '',
                contact_info: ''
            },
            editPatientData: {
                id: null,
                name: '',
                date_of_birth: '',
                contact_info: ''
            }
        };
    },
    async mounted() {
        await this.fetchPatients();
    },
    methods: {
        async fetchPatients() {
            const response = await fetch(`${baseUrl}/api/patients/`);
            const data = await response.json();
            this.patients = data.patients;
        },
        async createPatient() {
            const response = await fetch(`${baseUrl}/api/patients/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newPatient)
            });
            const newPatient = await response.json();
            this.patients.push(newPatient);
            this.resetNewPatientForm();
        },
        async deletePatient(patientId) {
            if (confirm('Are you sure you want to delete this patient?')) {
                await fetch(`${baseUrl}/api/patient/${patientId}/`, { method: 'DELETE' });
                this.patients = this.patients.filter(patient => patient.id !== patientId);
            }
        },
        openEditModal(patient) {
            this.editPatientData = { ...patient };
            const editModalElement = document.getElementById('editPatientModal');
            const modalInstance = new bootstrap.Modal(editModalElement);
            modalInstance.show();
        },
        async updatePatient() {
            const response = await fetch(`${baseUrl}/api/patient/${this.editPatientData.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.editPatientData)
            });
            const updatedPatient = await response.json();

            // Find the index and directly modify the patient in the array
            const index = this.patients.findIndex(patient => patient.id === updatedPatient.id);
            if (index !== -1) {
                this.patients[index] = updatedPatient;
            }
        },
        resetNewPatientForm() {
            this.newPatient = { name: '', date_of_birth: '', contact_info: '' };
        }
    }
};
</script>

<style scoped>
</style>
