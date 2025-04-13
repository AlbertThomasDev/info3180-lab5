<template>
  <div class="movies-container">
    <div v-for="movie in movies" :key="movie.id" class="movie-card">
      <img :src="movie.poster" alt="Movie Poster" class="poster" />
      <div class="movie-details">
        <h2>{{ movie.title }}</h2>
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);
function fetchMovies() {
  fetch("/api/v1/movies")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      movies.value = data.movies;
    })
    .catch((error) => {
      console.error("Error fetching movies:", error);
    });
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding: 20px;
  align-items: center;
}

.movie-card {
  display: flex;
  width: 600px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #fdfdfd;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  overflow: hidden;
}

.poster {
  width: 200px;
  height: 300px;
  object-fit: cover;
}

.movie-details {
  padding: 16px;
  flex-grow: 1;
}

.movie-details h2 {
  font-size: 1.4rem;
  margin-bottom: 10px;
}

.movie-details p {
  font-size: 1rem;
  color: #333;
}
</style>