<template>
    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
        <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" id="title" class="form-control" />
        </div>

        <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" id="description" class="form-control" ></textarea>
        </div>

        <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" name="poster" id="poster" class="form-control" accept="image/*"  /> <!--check this in the notes -->
        </div>

        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
</template>

<script setup>


function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }

    })
        .then(function (response) {
        return response.json();
        })
        .then(function (data) {
        // display a success message
        console.log(data);
        })
        .catch(function (error) {
        console.log(error);
        console.log("⚠️ Non-JSON response:");
        });

}

import { ref,onMounted } from "vue";
let csrf_token = ref("");



function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
    // console.log(data);
    csrf_token.value = data.csrf_token;
})
}

onMounted(() => {
    getCsrfToken();
});
</script>