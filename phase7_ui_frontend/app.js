document.addEventListener('DOMContentLoaded', () => {
    const apiClient = new APIClient(CONFIG.API_BASE_URL);
    
    // UI Elements
    const localitySelect = document.getElementById('locality-select');
    const priceRange = document.getElementById('price-range');
    const cuisineInput = document.getElementById('cuisine-input');
    const selectedCuisinesContainer = document.getElementById('selected-cuisines');
    const suggestionsContainer = document.getElementById('cuisine-suggestions');
    const ratingValue = document.getElementById('rating-value');
    const ratingMinus = document.getElementById('rating-minus');
    const ratingPlus = document.getElementById('rating-plus');
    const getRecommendationsBtn = document.getElementById('get-recommendations');
    const loader = document.getElementById('loader');
    const resultsSection = document.getElementById('results-section');
    const restaurantGrid = document.getElementById('restaurant-grid');
    const resultsCount = document.getElementById('results-count');
    const topCuisineTagsContainer = document.getElementById('top-cuisine-tags');
    const localityCount = document.getElementById('locality-count');
    const cuisineCount = document.getElementById('cuisine-count');
    const sortBy = document.getElementById('sort-by');

    let allCuisines = [];
    let selectedCuisines = new Set();
    let currentResults = [];

    // Initialize Page
    async function init() {
        try {
            // Load Metadata
            const locResponse = await fetch('../data/metadata/location_index.json');
            const locations = await locResponse.json();
            
            const cuiResponse = await fetch('../data/metadata/cuisine_index.json');
            allCuisines = await cuiResponse.json();

            localityCount.textContent = locations.length;
            cuisineCount.textContent = allCuisines.length;

            // Populate Localities
            locations.filter(loc => loc !== "unknown").forEach(loc => {
                const option = document.createElement('option');
                option.value = loc;
                option.textContent = loc.charAt(0).toUpperCase() + loc.slice(1);
                localitySelect.appendChild(option);
            });

            // Populate Top Cuisines
            CONFIG.TOP_CUISINES.forEach(cuisine => {
                const pill = document.createElement('div');
                pill.className = 'cuisine-pill';
                pill.textContent = cuisine;
                pill.onclick = () => addCuisine(cuisine);
                topCuisineTagsContainer.appendChild(pill);
            });

        } catch (error) {
            console.error("Failed to load metadata:", error);
        }
    }

    // Rating Controls
    ratingMinus.onclick = () => {
        let val = parseFloat(ratingValue.value);
        if (val > 0) ratingValue.value = (val - 0.1).toFixed(1);
    };

    ratingPlus.onclick = () => {
        let val = parseFloat(ratingValue.value);
        if (val < 5.0) ratingValue.value = (val + 0.1).toFixed(1);
    };

    // Cuisine Multi-select
    function filterCuisines(val = '') {
        const filtered = allCuisines.filter(c => 
            c.toLowerCase().includes(val.toLowerCase()) && !selectedCuisines.has(c)
        ).slice(0, 50); // Show more in the "dropdown" mode

        suggestionsContainer.innerHTML = '';
        if (filtered.length > 0) {
            filtered.forEach(c => {
                const item = document.createElement('div');
                item.className = 'suggestion-item';
                item.textContent = c;
                item.onclick = (e) => {
                    e.stopPropagation();
                    addCuisine(c);
                };
                suggestionsContainer.appendChild(item);
            });
            
            // Allow adding as custom if not in list
            if (val && !allCuisines.some(c => c.toLowerCase() === val.toLowerCase())) {
                const custom = document.createElement('div');
                custom.className = 'suggestion-item custom-add';
                custom.innerHTML = `+ Add "<strong>${val}</strong>"`;
                custom.onclick = (e) => {
                    e.stopPropagation();
                    addCuisine(val);
                };
                suggestionsContainer.appendChild(custom);
            }

            suggestionsContainer.style.display = 'block';
        } else if (val) {
             // Show "Add Custom" even if no matches
             suggestionsContainer.innerHTML = '';
             const custom = document.createElement('div');
             custom.className = 'suggestion-item custom-add';
             custom.innerHTML = `+ Add "<strong>${val}</strong>"`;
             custom.onclick = (e) => {
                 e.stopPropagation();
                 addCuisine(val);
             };
             suggestionsContainer.appendChild(custom);
             suggestionsContainer.style.display = 'block';
        } else {
            suggestionsContainer.style.display = 'none';
        }
    }

    cuisineInput.oninput = (e) => filterCuisines(e.target.value);
    
    cuisineInput.onfocus = () => filterCuisines(cuisineInput.value);

    // Close dropdown on outside click
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.multi-select-container')) {
            suggestionsContainer.style.display = 'none';
        }
    });

    function addCuisine(cuisine) {
        if (!selectedCuisines.has(cuisine)) {
            selectedCuisines.add(cuisine);
            renderCuisineTags();
        }
        cuisineInput.value = '';
        suggestionsContainer.style.display = 'none';
    }

    function removeCuisine(cuisine) {
        selectedCuisines.delete(cuisine);
        renderCuisineTags();
    }

    function renderCuisineTags() {
        selectedCuisinesContainer.innerHTML = '';
        selectedCuisines.forEach(c => {
            const tag = document.createElement('div');
            tag.className = 'tag';
            tag.innerHTML = `${c} <span onclick="event.stopPropagation(); this.parentElement.removeCuisineTag('${c}')">×</span>`;
            // Add custom property to tag element to handle click
            tag.removeCuisineTag = (val) => removeCuisine(val);
            tag.querySelector('span').onclick = () => removeCuisine(c);
            selectedCuisinesContainer.appendChild(tag);
        });
    }

    // Recommendations
    getRecommendationsBtn.onclick = async () => {
        const location = localitySelect.value;
        if (!location) {
            alert("Please select a locality");
            return;
        }

        const payload = {
            location: location,
            cuisines: Array.from(selectedCuisines),
            max_price: parseInt(priceRange.value) || 5000,
            min_rating: parseFloat(ratingValue.value)
        };

        // UI State
        loader.style.display = 'block';
        resultsSection.style.display = 'none';
        getRecommendationsBtn.disabled = true;

        try {
            const result = await apiClient.getRecommendations(payload);
            
            if (result.status === "success") {
                currentResults = result.recommendations;
                renderResults();
            } else {
                alert(result.message || "An error occurred");
            }
        } catch (error) {
            alert(`Error: ${error.message}`);
        } finally {
            loader.style.display = 'none';
            getRecommendationsBtn.disabled = false;
        }
    };

    function renderResults() {
        const sorted = sortResults(currentResults, sortBy.value);
        
        restaurantGrid.innerHTML = '';
        resultsCount.textContent = `${sorted.length} results found`;
        
        if (sorted.length === 0) {
            restaurantGrid.innerHTML = '<p class="no-results">Sorry, no restaurants matched your exact criteria. Try broadening your filters!</p>';
        } else {
            sorted.forEach(res => {
                const card = createRestaurantCard(res);
                restaurantGrid.appendChild(card);
            });
        }
        
        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function sortResults(results, criteria) {
        const items = [...results];
        switch(criteria) {
            case 'rating-desc': return items.sort((a, b) => b.rating - a.rating);
            case 'rating-asc': return items.sort((a, b) => a.rating - b.rating);
            case 'price-desc': return items.sort((a, b) => b.price_range - a.price_range);
            case 'price-asc': return items.sort((a, b) => a.price_range - b.price_range);
            default: return items;
        }
    }

    sortBy.onchange = () => renderResults();

    function createRestaurantCard(res) {
        const div = document.createElement('div');
        div.className = 'restaurant-card';
        
        div.innerHTML = `
            <div class="card-header">
                <h3>${res.restaurant_name}</h3>
                <div class="rating-badge">
                    <span class="rating-value">${res.rating} ⭐</span>
                    <span class="rating-divider">•</span>
                    <span class="votes-count">${res.votes.toLocaleString()} ratings</span>
                </div>
            </div>
            <div class="card-info">
                <div class="info-item">
                    <span class="icon">🍽️</span> ${res.cuisines.join(', ')}
                </div>
                <div class="info-item">
                    <span class="icon">💰</span> Avg ₹${res.price_range} for two
                </div>
                <div class="info-item">
                    <span class="icon">📍</span> ${res.location}, Bangalore
                </div>
            </div>
            <div class="ai-section">
                <div class="ai-header">Why you'll like it</div>
                <div class="ai-explanation">
                    "${res.explanation}"
                </div>
            </div>
            <div class="card-footer">
                <a href="${res.url}" target="_blank" class="restaurant-link">Explore This Restaurant on Zomato 📍</a>
            </div>
        `;
        return div;
    }

    init();
});
