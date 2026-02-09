# 🌦️ Simple Weather Dashboard

A lightweight, responsive weather application built with Vanilla JavaScript and the OpenWeatherMap API. This project demonstrates asynchronous programming, error handling, and secure API key management.

## 🚀 Features
- **Real-time Data:** Fetches current temperature and weather conditions.
- **Dynamic Search:** Search for weather data by city name.
- **Asynchronous Logic:** Uses `async/await` and the Fetch API for smooth performance.
- **Error Handling:** Includes checks for invalid city names and network issues.
- **Security Best Practices:** Implements a configuration pattern to keep API keys private.

## 🛠️ Technologies Used
- **JavaScript (ES6+):** Core logic and API interaction.
- **HTML5/CSS3:** Structure and basic styling.
- **OpenWeatherMap API:** Source of global weather data.

## 📦 Installation & Setup

Since this project uses a private API key, follow these steps to run it locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```

2. Get your API Key:
 - Sign up for a free account at OpenWeatherMap.
 - Generate your API key from the dashboard.

3. Configure the project:
 - In the root folder, create a file named config.js.
 - Copy the following code into config.js and replace the placeholder with your key:
 ```bash
 const CONFIG = {
    WEATHER_API_KEY: "YOUR_ACTUAL_API_KEY_HERE"
    };
 ```

4. Launch the App:
 - Simply open index.html browser.