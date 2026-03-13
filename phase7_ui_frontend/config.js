const CONFIG = {
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
        ? "http://localhost:8000" 
        : "https://dinesmart-backend.onrender.com",
    DEFAULT_RATING: 4.0,
    TOP_CUISINES: ["North Indian", "Chinese", "South Indian", "Fast Food", "Biryani"]
};
