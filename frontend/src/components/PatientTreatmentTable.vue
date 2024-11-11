<template>
    <div>
        <button class="btn btn-primary" @click="$emit('add-patient-treatment')">Add Patient Treatment</button>

        <!-- Patient-Treatments Table -->
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>Patient</th>
                    <th>Treatment</th>
                    <th>Treatment Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="relation in patientTreatments" :key="relation.id">
                    <td>{{ relation.patient_name }}</td>
                    <td>{{ relation.treatment_name }}</td>
                    <td>{{ relation.treatment_date }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary" @click="editPatientTreatment(relation)">Edit</button>
                        <button class="btn btn-sm btn-danger" @click="$emit('delete-patient-treatment', relation.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        patientTreatments: Array,
        patients: Array,
        treatments: Array
    },
    methods: {
        editPatientTreatment(relation) {
            const updatedRelation = {
                ...relation,
                treatment_date: prompt("Treatment Date:", relation.treatment_date)
            };
            this.$emit("update-patient-treatment", updatedRelation);
        }
    }
};
</script>
