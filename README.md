# Real Estate Price Prediction using Multimodal Learning

## Overview
This project predicts residential property prices by combining structured tabular data with satellite imagery embeddings extracted using a pretrained ResNet-18 model. The objective is to demonstrate how multimodal learning (numerical + visual data) improves real-estate price estimation.

## Approach

### Tabular Features
The following attributes are used:
- bedrooms
- bathrooms
- sqft_living
- sqft_lot
- floors
- waterfront
- view
- condition
- grade

All tabular features are standardized using StandardScaler.

### Satellite Imagery
- Satellite images are downloaded using latitude and longitude coordinates.
- Images are resized to 224×224.
- A pretrained ResNet-18 model is used as a fixed feature extractor.
- The final fully connected layer is removed to obtain 512-dimensional image embeddings.

### Multimodal Fusion
Tabular features and image embeddings are concatenated to form a combined feature representation used for regression.

### Model
Ridge Regression is used for price prediction. Model performance is evaluated using RMSE and R² on a validation split.

## Project Structure

real_estate_multimodal/
│
├── data/
│   └── raw/
│       ├── train.xlsx
│       └── test.xlsx
│
├── images/
│   ├── train/
│   └── test/
│
├── preprocessing.ipynb
├── model_training.ipynb
├── data_fetcher.py
├── submission.csv
├── requirements.txt
└── README.md

## File Descriptions

data_fetcher.py  
Script to download satellite images using latitude and longitude via the Mapbox Static Images API.

preprocessing.ipynb  
Loads raw data, performs cleaning and feature selection, downloads satellite images, defines image transforms, and extracts CNN embeddings.

model_training.ipynb  
Combines tabular and image features, splits data into training and validation sets, trains the regression model, evaluates performance, and generates predictions.

submission.csv  
Contains predicted property prices for the test dataset.

## How to Run

1. Install dependencies  
pip install -r requirements.txt

2. Run preprocessing  
Open preprocessing.ipynb and run all cells.

3. Run model training  
Open model_training.ipynb and run all cells.  
submission.csv will be generated automatically.

## Results
The multimodal model outperforms tabular-only baselines. Satellite imagery provides additional contextual information such as neighborhood quality and surroundings.

## Notes
Satellite images are cached locally to avoid repeated API calls. CNN weights are frozen to reduce computational cost. The project is structured for reproducibility and clarity.
