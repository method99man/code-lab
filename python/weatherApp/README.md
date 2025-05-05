# 🌦️ Python Weather

An interactive desktop application written in Python using **OpenWeatherMap API**.  
It allows you to check the current weather in a selected city.

---

## 🚀 Features

- ☁️ Weather data for any city (temperature, humidity, wind speed, general conditions)
- 📦 Handles API errors and empty results


---

## 📦 Requirements

- Python 3.9+
- Libraries:
  - `requests`
  - `tkinter` (included with Python)


Install dependencies:

```bash
pip install -r requirements.txt
```

🛠️ How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```
2. Add your weather API key (OpenWeatherMap) to the code:
    Create a file named config.py and add:
    ```python
       MY_API_KEY = "your_api_key_here"
    ```
3. Run the app:
    ```bash
    python app.py
    ```