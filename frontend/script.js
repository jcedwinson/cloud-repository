const apiUrl = "https://drf-app-829853977033.asia-southeast1.run.app/api/movies/";

async function fetchMovies() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) throw new Error("Failed to fetch movies");
    const movies = await response.json();

    const container = document.getElementById("movie-list");
    container.innerHTML = "";

    movies.forEach(movie => {
      const card = document.createElement("div");
      card.className = "movie-card";
      card.innerHTML = `
        <h3>${movie.name}</h3>
        <p><strong>Actor:</strong> ${movie.actor}</p>
        <p><strong>Actress:</strong> ${movie.actress}</p>
        <p><strong>Genre:</strong> ${movie.genre}</p>
        <p><strong>Rating:</strong> ⭐ ${movie.rating}</p>
      `;
      container.appendChild(card);
    });
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("movie-list").innerHTML = "<p>Unable to load movies.</p>";
  }
}

fetchMovies();
