import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


df = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\MODEL-AGRI-SDC.xlsx")
df = df.drop(columns=['Unnamed: 0'])


model = joblib.load("C:\AGRI_PRED\AGRISOL_model.pkl")


area_enc = LabelEncoder()
item_enc = LabelEncoder()

df['Area'] = area_enc.fit_transform(df['Area'])
df['Item'] = item_enc.fit_transform(df['Item'])


features = df[['Area', 'Item', 'Year', 'Avg Rainfall / Year (mm )', 'Pesticides (Tonnes)', 'Avg Temp']]
df['Predicted Yield'] = model.predict(features)


dataset = df
