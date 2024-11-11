<template>
    <div>
        <button class="btn btn-primary" @click="$emit('add-patient')">Add Patient</button>

        <!-- Patients Table -->
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Date of Birth</th>
                    <th>Contact Info</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="patient in patients" :key="patient.id">
                    <td>{{ patient.name }}</td>
                    <td>{{ patient.date_of_birth }}</td>
                    <td>{{ patient.contact_info }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary" @click="editPatient(patient)">Edit</button>
                        <button class="btn btn-sm btn-danger" @click="$emit('delete-patient', patient.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        patients: Array
    },
    methods: {
        editPatient(patient) {
            const updatedPatient = {
                ...patient,
                name: prompt("Name:", patient.name),
                date_of_birth: prompt("Date of Birth:", patient.date_of_birth),
                contact_info: prompt("Contact Info:", patient.contact_info)
            };
            this.$emit("update-patient", updatedPatient);
        }
    }
};
</script>
