<template>
    <table class="table">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Computer</th>
                <th scope="col">Price</th>
                <th scope="col">Description</th>
                <th scope="col">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(computer, index) in computers">
                <th scope="row">{{ index+1 }}</th>
                <td>
                    {{ computer.name }}
                </td>
                <td>
                    <span class="badge bg-secondary">
                        £{{ computer.price }}
                    </span>
                </td>
                <td>
                    <i>{{ computer.description }}</i>
                </td>
                <td>
                    <button 
                        class="btn btn-sm btn-primary me-2"
                        @click="editComputer"
                    >
                        <i class="bi bi-pencil-square"></i>
                    </button>
                    <button 
                        class="btn btn-sm btn-danger"
                        @click="$emit('delete-computer', computer)"
                    >
                        <i class="bi bi-trash"></i>
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
    export default {
        emits: ['delete-computer'],
        props: {
            computers: {
                type: Array,
                required: true
            }
        },
        methods: {
            editComputer() {
                alert('Edit computer - not implemented');
            }
        }
    }
</script>

<style scoped>
    td, th {
        vertical-align: middle;
    }
</style>