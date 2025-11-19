// API Configuration
const API_CONFIG = {
    BASE_URL: 'http://localhost:8000',
    ENDPOINTS: {
        LOGIN: '/api/auth/login',
        COMPLAINTS: '/api/complaints',
        FORWARD: '/api/complaints/forward',
        BATCH_FORWARD: '/api/complaints/forward/batch',
        HEALTH: '/health'
    }
};

// Helper function to build full URL
function getApiUrl(endpoint) {
    return API_CONFIG.BASE_URL + endpoint;
}
