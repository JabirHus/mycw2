<template>
    <div>
        <button class="btn btn-sm btn-success mb-3" data-bs-toggle="modal" data-bs-target="#addTreatmentModal">
            <i class="bi bi-plus"></i> Add Treatment
        </button>

        <!-- Treatment Table -->
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(treatment, index) in treatments" :key="treatment.id">
                    <th>{{ index + 1 }}</th>
                    <td>{{ treatment.name }}</td>
                    <td>{{ treatment.description }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary me-2" @click="openEditModal(treatment)">Edit</button>
                        <button class="btn btn-sm btn-danger" @click="deleteTreatment(treatment.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>

        <!-- Add Treatment Modal -->
        <div class="modal fade" id="addTreatmentModal" tabindex="-1" aria-labelledby="addTreatmentModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="addTreatmentModalLabel">Add Treatment</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="newTreatment.name" type="text" class="form-control" id="name">
                        </div>
                        <div class="mb-3">
                            <label for="description" class="form-label">Description</label>
                            <textarea v-model="newTreatment.description" class="form-control" id="description"></textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="createTreatment" data-bs-dismiss="modal">Save</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Edit Treatment Modal -->
        <div class="modal fade" id="editTreatmentModal" tabindex="-1" aria-labelledby="editTreatmentModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="editTreatmentModalLabel">Edit Treatment</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="mb-3">
                            <label for="edit_name" class="form-label">Name</label>
                            <input v-model="editTreatmentData.name" type="text" class="form-control" id="edit_name">
                        </div>
                        <div class="mb-3">
                            <label for="edit_description" class="form-label">Description</label>
                            <textarea v-model="editTreatmentData.description" class="form-control" id="edit_description"></textarea>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" @click="updateTreatment" data-bs-dismiss="modal">Save Changes</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.min.js';

const baseUrl = 'http://localhost:8000';

export default {
    data() {
        return {
            treatments: [],
            newTreatment: {
                name: '',
                description: ''
            },
            editTreatmentData: {
                id: null,
                name: '',
                description: ''
            }
        };
    },
    async mounted() {
        await this.fetchTreatments();
    },
    methods: {
        async fetchTreatments() {
            const response = await fetch(`${baseUrl}/api/treatments/`);
            const data = await response.json();
            this.treatments = data.treatments;
        },
        async createTreatment() {
            const response = await fetch(`${baseUrl}/api/treatments/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.newTreatment)
            });
            const newTreatment = await response.json();
            this.treatments.push(newTreatment);
            this.resetNewTreatmentForm();
        },
        async deleteTreatment(treatmentId) {
            if (confirm('Are you sure you want to delete this treatment?')) {
                await fetch(`${baseUrl}/api/treatment/${treatmentId}/`, { method: 'DELETE' });
                this.treatments = this.treatments.filter(treatment => treatment.id !== treatmentId);
            }
        },
        openEditModal(treatment) {
            this.editTreatmentData = { ...treatment };
            const editModalElement = document.getElementById('editTreatmentModal');
            const modalInstance = new bootstrap.Modal(editModalElement);
            modalInstance.show();
        },
        async updateTreatment() {
            const response = await fetch(`${baseUrl}/api/treatment/${this.editTreatmentData.id}/`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.editTreatmentData)
            });
            const updatedTreatment = await response.json();

            // Update the treatment in the array
            const index = this.treatments.findIndex(treatment => treatment.id === updatedTreatment.id);
            if (index !== -1) {
                this.treatments[index] = updatedTreatment;
            }
        },
        resetNewTreatmentForm() {
            this.newTreatment = { name: '', description: '' };
        }
    }
};
</script>

<style scoped>
</style>
