from flask import Flask, request, render_template
import ee
import pandas as pd
import joblib

app = Flask(__name__)

# --- 1. Google Earth Engine Initialization ---
# Ensure this matches your Google Cloud Project ID
GEE_PROJECT_ID = 'my-crop-yield-project-******'

try:
    ee.Initialize(project=GEE_PROJECT_ID)
except Exception:
    ee.Authenticate()
    ee.Initialize(project=GEE_PROJECT_ID)

# --- 2. Load the AI Model ---
try:
    # Using Scikit-Learn for the predictive model [cite: 47, 60]
    model = joblib.load('crop_yield_model.pkl')
    print("AI Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# --- 3. Satellite Data Helper ---
def get_ndvi_for_year(lat, lon, year):
    """Fetches the peak NDVI for a specific location and year."""
    geometry = ee.Geometry.Point([lon, lat])
    
    # Utilizing Copernicus Sentinel-2 multispectral imagery [cite: 37]
    # Filtering for cloud cover less than 40% to ensure data quality [cite: 41]
    s2_col = ee.ImageCollection('COPERNICUS/S2') \
                .filterBounds(geometry) \
                .filterDate(f'{year}-01-01', f'{year}-12-31') \
                .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 40))
    
    if s2_col.size().getInfo() == 0:
        return None
    
    # NDVI Calculation using NIR (B8) and Red (B4) bands [cite: 34, 39]
    def add_ndvi(img):
        return img.normalizedDifference(['B8', 'B4']).rename('NDVI')
    
    max_ndvi_image = s2_col.map(add_ndvi).max()
    
    try:
        # Extract the mean NDVI value for the target coordinate
        stats = max_ndvi_image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=geometry,
            scale=10 # Sentinel-2 has 10m spatial resolution 
        ).get('NDVI').getInfo()
        return stats
    except:
        return None

# --- 4. Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Support for both manual entry and map-click coordinates [cite: 48, 49]
        lat = float(request.form['latitude'])
        lon = float(request.form['longitude'])

        # Analyze 5-year historical trend (2021-2025) [cite: 38, 40]
        history_results = {}
        for y in [2021, 2022, 2023, 2024, 2025]:
            val = get_ndvi_for_year(lat, lon, y)
            history_results[str(y)] = round(val, 3) if val else 0

        # Select prediction base (2025 or 2024 fallback)
        prediction_ndvi = history_results['2025'] if history_results['2025'] > 0 else history_results['2024']
        
        if prediction_ndvi == 0:
            return render_template('index.html', 
                                 prediction_text="Error: Satellite imagery not available for this location.",
                                 analyzed_lat=lat, 
                                 analyzed_lon=lon)

        # Machine Learning Inference using Linear Regression [cite: 52, 71]
        input_df = pd.DataFrame({'Max_NDVI': [prediction_ndvi]})
        yield_pred = model.predict(input_df)[0]
        
        result_string = f"Predicted Yield: {yield_pred:.2f} tonnes/ha (Based on Peak NDVI: {prediction_ndvi})"
        
        # Pass coordinates back to the UI for display [cite: 53, 58]
        return render_template('index.html', 
                               prediction_text=result_string, 
                               history=history_results,
                               analyzed_lat=lat, 
                               analyzed_lon=lon)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Process Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
