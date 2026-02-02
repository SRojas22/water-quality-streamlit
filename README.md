# Water Quality Dashboard (Streamlit)

## Overview
This project is an interactive Streamlit web application that visualizes water quality data from Biscayne Bay.  
The goal of the app is to allow users to explore environmental measurements through interactive charts and gain insights using data visualization techniques.

## Dataset
- **File:** `biscayneBay_waterquality.csv`
- **Description:** The dataset contains water quality measurements collected from Biscayne Bay.
- **Example attributes:**
  - Time
  - Temperature (°C)
  - pH
  - Dissolved Oxygen (ODO mg/L)
  - Latitude
  - Longitude
  - Total Water Column Depth (m)

## Features
- Interactive data table and descriptive statistics
- Plotly-powered visualizations:
  - Line chart with selectable metric (temperature, pH, dissolved oxygen)
  - Scatter plot showing dissolved oxygen vs temperature, colored by pH
  - 3D scatter plot visualizing geographic location and water column depth
- External API integration using NASA’s Astronomy Picture of the Day (APOD)

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- Requests

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/SRojas22/water-quality-streamlit.git
   cd water-quality-streamlit
2. Create and activate a virtual environment.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Create a .env file (do not commit it) with:
    ```bash
    NASA_API_KEY=your_api_key_here
5. Run the app:
    ```bash
    streamlit run dashboard.py
