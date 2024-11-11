<template>
    <div>
        <button class="btn btn-primary" @click="$emit('add-treatment')">Add Treatment</button>

        <!-- Treatments Table -->
        <table class="table mt-3">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="treatment in treatments" :key="treatment.id">
                    <td>{{ treatment.name }}</td>
                    <td>{{ treatment.description }}</td>
                    <td>
                        <button class="btn btn-sm btn-primary" @click="editTreatment(treatment)">Edit</button>
                        <button class="btn btn-sm btn-danger" @click="$emit('delete-treatment', treatment.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        treatments: Array
    },
    methods: {
        editTreatment(treatment) {
            const updatedTreatment = {
                ...treatment,
                name: prompt("Name:", treatment.name),
                description: prompt("Description:", treatment.description)
            };
            this.$emit("update-treatment", updatedTreatment);
        }
    }
};
</script>
