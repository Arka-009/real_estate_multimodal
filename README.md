# Real Estate Multimodal Valuation

## Overview
Predict property prices using tabular data + satellite imagery embeddings (ResNet-18).

## Structure
- `data/raw/` → original datasets
- `images/` → downloaded satellite images
- `preprocessing.ipynb` → data cleaning and feature engineering
- `model_training.ipynb` → model training and prediction
- `data_fetcher.py` → script to download images from Google Maps API
- `submission.csv` → final price predictions

## How to Run
1. Install dependencies:
   pip install pandas numpy torch torchvision matplotlib scikit-learn pillow

2. Run preprocessing:
   Open `preprocessing.ipynb` and run all cells

3. Run model training:
   Open `model_training.ipynb` and run all cells

4. Submission:
   `submission.csv` will be generated automatically in project root
