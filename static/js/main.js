document.addEventListener("DOMContentLoaded", function() {
    const searchForm = document.getElementById('global-search-form');

    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault(); // Prevent standard page reload

            const query = document.getElementById('search-input').value;
            const resultsContainer = document.getElementById('search-results-container');

            // Placeholder logic until backend API is ready
            resultsContainer.innerHTML = `<div class="alert alert-info">Searching for "${query}"... (Backend integration pending)</div>`;

            /* Future AJAX call structure:
            fetch(`/search/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    // Update the DOM with the JSON data returned by the backend team
                });
            */
        });
    }
});v