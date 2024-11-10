<template>
    <div class="container pt-3">
        <div class="h1 text-center border rounded bg-light p-2 mb-3">Healthcare Management</div>

        <!-- Tabs for Patients, Treatments, and Patient-Treatments -->
        <ul class="nav nav-tabs mb-3" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="patients-tab" data-bs-toggle="tab" data-bs-target="#patients" type="button" role="tab" aria-controls="patients" aria-selected="true">Patients</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="treatments-tab" data-bs-toggle="tab" data-bs-target="#treatments" type="button" role="tab" aria-controls="treatments" aria-selected="false">Treatments</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="patient-treatments-tab" data-bs-toggle="tab" data-bs-target="#patient-treatments" type="button" role="tab" aria-controls="patient-treatments" aria-selected="false">Patient-Treatments</button>
            </li>
        </ul>

        <div class="tab-content">
            <div class="tab-pane fade show active" id="patients" role="tabpanel" aria-labelledby="patients-tab">
                <PatientTable />
            </div>
            <div class="tab-pane fade" id="treatments" role="tabpanel" aria-labelledby="treatments-tab">
                <TreatmentTable />
            </div>
            <div class="tab-pane fade" id="patient-treatments" role="tabpanel" aria-labelledby="patient-treatments-tab">
                <PatientTreatmentTable />
            </div>
        </div>
    </div>
</template>

<script>
import PatientTable from './components/PatientTable.vue';
import TreatmentTable from './components/TreatmentTable.vue';
import PatientTreatmentTable from './components/PatientTreatmentTable.vue';

export default {
    components: {
        PatientTable,
        TreatmentTable,
        PatientTreatmentTable
    }
};
</script>

<style scoped>
</style>
