/**
 * Weather Dashboard Logic
 * -----------------------
 * This script handles fetching weather data from external APIs and updating the UI.
 * 
 * SECURITY NOTE: The API key is stored in a separate 'config.js' file 
 * which is excluded from version control (git) to prevent unauthorized use.
 */

// ---  DOM Elements ---
const result = document.querySelector('.result');
const searchBtn = document.querySelector('.search');

/**
 * API Key retrieved from the global CONFIG object (loaded via config.js).
 * We use a constant to ensure the key isn't accidentally overwritten.
 */
const KEY = CONFIG.WEATHER_API_KEY;


// ---  Event Listeners ---
searchBtn.addEventListener('click', () => {
    const city = document.querySelector('.city-Input').value;
    getProperlyWeather(city);
})

// ---  Core Logic ---
async function getProperlyWeather(city) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${KEY}&units=metric`;

    try {
        // Send the request and wait for the response header
        const response = await fetch(url);

        // Handle potential errors (e.g., city not found / 404)
        if (!response.ok) throw new Error(`City not found (Status: ${response.status})`);

        // Parse the stream into a readable JSON object
        const data = await response.json();

        // Extract specific data points from the JSON structure
        const temp = data.main.temp;
        const description = data.weather[0].description;

        // Update the DOM with the results
        result.innerText = `In ${city}, it's ${temp}°C with ${description}.`;
        
    }catch (err) {
        /**
         * Error Handling:
         * This block catches network issues OR the errors we 'throw' above.
         */
        console.error("Weather Fetch Error:", err);
        result.innerText = "Failed to fetch.", err;
    }
}


// ---  Alternative/Reference Solutions ---

/**
 * QUICK SOLUTION REFERENCE (Open-Meteo)
 * This is an alternative way to get weather data without needing an API Key.
 * It uses Latitude/Longitude instead of city names.
 */
/*
async function getQuickWeather() {
    const lat = 50.6677;
    const lon = 17.9286;
    const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`;

    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error("Weather service is down!");

        const data = await response.json();
        console.log(`It is currently ${data.current_weather.temperature}°C in Opole.`);
    } catch (error) {
        console.error("Oops:", error);
    }
}
*/