

# Flask Weather App

## Overview

This Flask Weather App is a simple web application that retrieves real-time weather information using the OpenWeatherAPI. The backend is built with Flask, while the frontend leverages Bootstrap for a clean and responsive user interface.

## Features

- **Weather Information:** Fetches and displays current weather details for a specified location.
- **OpenWeatherAPI Integration:** Utilizes the OpenWeatherAPI to retrieve accurate and up-to-date weather data.
- **Flask Backend:** Employs Flask as the backend framework for efficient data processing.
- **Bootstrap Frontend:** The user interface is designed with Bootstrap, ensuring a sleek and user-friendly experience.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mishra-krishna/webappusingflask
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd flask-weather-app
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

   The app will be accessible at `http://localhost:5000` by default.

## Configuration

- Add your OpenWeatherAPI key in a `.env` file:
  ```python
  API_KEY = "your_api_key_here"
  ```

## Contributing

Contributions are welcome! Feel free to open issues and pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
