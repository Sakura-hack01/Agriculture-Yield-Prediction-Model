# Crop Prediction on Agro Environmental Data


## Project Overview

This project aimed to forecast crop yields using machine learning techniques and visualize the results through interactive dashboards. The focus was on identifying key environmental and agricultural factors such as rainfall, temperature, fertilizer usage, that influence crop productivity. A structured methodology was followed starting from data collection, cleaning, and preprocessing to model development using Random Forest Regression, which demonstrated high predictive accuracy. The model also provided insights into feature importance, helping to identify the most influential factors affecting crop yields. To make the results easily interpretable and useful for decision-making, Power BI was used to build interactive dashboards. These visualizations enabled comparison across regions, evaluation of trends, and support for data-driven agricultural policy and planning.
This helps to assist farmers, agronomists, and policymakers in decision-making and yield improvement.


## Table of Contents

• [Project Overview](#project-overview)

• [Dataset Description](#dataset-description)

• [Technologies](#technologies)

• [Architecture](#architecture)

• [Installation Guide](#installation-guide)

• [Usage Instuction](#usage-instruction)

• [Folder Structure](#folder-structure)


## Dataset Description

This dataset includes historical crop production records along with corresponding environmental parameters. Key columns incudes :-

• Area

• Item (Crop Type)

• Year

• Pesticides (tonnes)

• Yield (tonnes/hectare) [Target variable]

• Average Temperature (°C)

• Average Rainfall/Year (mm)

### Dataset :- https://www.kaggle.com/datasets/mrigaankjaswal/crop-yield-prediction-dataset


## Technologies

• Python (Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, flask)

• PowerBI (for interactive dashboard and visualizations)

• VS Code

• Joblib (for serialization of model)


## Architecture

• Data Collection and cleaning

• Outlier detection and removal (IQR method)

• Feature Encoding (LabelEncoder)

• Feature Selection and splitting

• Model training (RandomForest)

• Model Evaluation and saving

• Prediction on new data

• PowerBI dashboard visualization


## Installation Guide

### Prerequisites 

• Python : 3.9 - 3.11

• PowerBI

• Microsoft Excel

• Git

• IDE : VS Code/ Jupyter Notebook/ Cursor Studio

### Clone repository

`git clone https://github.com/Sakura-hack01/Agriculture-Yield-Prediction-Dashboard.git`

`cd Agriculture-Yield-Prediction-Dashboard`

### Install Dependies

`pip install numpy pandas matplotlib seaborn scikit-learn joblib flask`

### Train model

For training the model run the following command :-

`python train model.py`

### Flask Web application

To see the web page for the dashboard you need to run :-

`python app.py`


## Usage Instuction

As the flask application starts on the webpage, enter the following values :-

• Average Rainfall(mm)

• Average Rainfall (mm)

• Average Temperature (°C)

• Pesticide Usage (kg/ha)

• Crop Type (e.g., Wheat, Rice)

• Area/Region

Click predict, the model will output the predicted yield and confidence metrices.

### View Analytics in PowerBI

• Open PowerBI.

• Load the provided `.pbix` file.

• Ensure it is connected to `PowerBI Import.py` which will predict and then through visualization shows the result.


## Folder Structure
```
Agriculture Yield Prediction Dashboard
|
|__ .gitignore
|
|__ AGRISOL-Jupyter-Notebook.ipynb
|
|__ LICENSE
|
|__ MODEL-AGRI-SDC.xlsx
|
|__ SDC-PROJECT-AGRI.pbix
|
|__ Model Prediction
         |
         |__ model.py
         |
         |__ app.py
         |
         |__ PowerBI-Import.py
         |
         |__ templates
             |
             |__ index.html
             |
             |__ result.html
```


## LICENSE

This project is licensed under MIT License - see the [LICENSE](LICENSE) file for details.
