# 🌾 Satellite-Based Crop Yield Analysis System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Google Earth Engine](https://img.shields.io/badge/Google%20Earth%20Engine-Geospatial-green)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn)
![Status](https://img.shields.io/badge/Project-Final%20Year-success)

A web-based crop yield prediction system that utilizes **Sentinel-2 satellite imagery**, **Google Earth Engine**, **NDVI analysis**, and **Machine Learning** to estimate crop yield through an interactive map interface.

---

## 📖 Overview

Traditional crop yield estimation relies heavily on manual field surveys, making the process time-consuming, expensive, and difficult to scale. This project introduces an automated approach that combines satellite remote sensing with machine learning to monitor vegetation health and predict crop yield.

Users can select any agricultural location on an interactive map, after which the system retrieves Sentinel-2 satellite imagery, calculates NDVI values, analyzes vegetation trends, and predicts crop yield.

---

## ✨ Features

- 🗺️ Interactive map for selecting agricultural land
- 🛰️ Retrieves Sentinel-2 satellite imagery using Google Earth Engine
- 🌿 Calculates Normalized Difference Vegetation Index (NDVI)
- ☁️ Cloud filtering for improved satellite image quality
- 📈 Five-year vegetation health trend visualization
- 🤖 Crop yield prediction using Linear Regression
- 📊 Interactive graphs and result dashboard
- ⚡ Automated end-to-end processing pipeline

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Leaflet.js

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Linear Regression
- Joblib

### Data Processing
- Google Earth Engine
- Sentinel-2 Satellite Imagery
- NumPy
- Pandas

---

## 🏗️ System Architecture

```
User
   │
   ▼
Interactive Map (Leaflet.js)
   │
   ▼
Flask Backend
   │
   ▼
Google Earth Engine
   │
   ▼
Sentinel-2 Satellite Data
   │
   ▼
Cloud Filtering
   │
   ▼
NDVI Calculation
   │
   ▼
Machine Learning Model
   │
   ▼
Yield Prediction
   │
   ▼
Dashboard & Graphs
```

---

## 🔄 Workflow

1. User selects a location using the interactive map.
2. Coordinates are sent to the Flask backend.
3. Google Earth Engine retrieves Sentinel-2 imagery.
4. Cloud filtering removes noisy images.
5. NDVI is calculated using:
   
   **NDVI = (NIR − Red) / (NIR + Red)**

6. Maximum NDVI values are extracted.
7. The trained Linear Regression model predicts crop yield.
8. Results and vegetation trends are displayed on the dashboard.

---

## 📂 Project Structure

```
Satellite-Based-Crop-Yield-Analysis-System/
│
├── app.py
├── crop_yield_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
├── requirements.txt
└── screenshots/
```

---

## 📊 Machine Learning Model

| Model | Linear Regression |
|--------|-------------------|
| Input | Peak NDVI |
| Output | Crop Yield (Tonnes/Hectare) |
| Train/Test Split | 70/30 |
| R² Score | 0.87 |

---

## 📈 Results

- Accurate NDVI trend visualization
- Interactive location selection
- Automated satellite image processing
- Reliable crop yield prediction
- R² Score of **0.87**, demonstrating a strong relationship between vegetation health and predicted crop yield.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/99DevMridul/Satellite-Based-Crop-Yield-Analysis-System.git
```

Move into the project directory:

```bash
cd Satellite-Based-Crop-Yield-Analysis-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 📌 Future Improvements

- Support for multiple crop types
- Integration of weather and rainfall data
- Soil quality analysis
- Advanced Machine Learning models (Random Forest, XGBoost, Deep Learning)
- Mobile application for farmers
- Region-specific training datasets
- Real-time monitoring and alerts

---

## ⚠️ Limitations

- Model is currently trained using region-specific data.
- Prediction quality depends on the availability of cloud-free satellite imagery.
- Weather, soil conditions, and fertilizer usage are not included in the current model.
- Linear Regression may not capture complex agricultural patterns.

---

## 📚 References

- Google Earth Engine
- Sentinel-2 (Copernicus)
- Scikit-Learn
- FAO Earth Observation
- NASA Earth Observatory
- Leaflet.js Documentation

---

## 👨‍💻 Author

**Mridul Manjhi**

Bachelor of Computer Applications (BCA)

Institute of Engineering & Management, Kolkata

GitHub: https://github.com/99DevMridul

---

## 📄 License

This project is developed for academic and educational purposes as part of the Final Year BCA Project.

---

⭐ If you found this project useful, consider giving it a star on GitHub!
