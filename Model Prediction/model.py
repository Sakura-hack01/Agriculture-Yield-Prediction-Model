import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


ag = pd.read_excel(r"C:\Users\hp\OneDrive\Documents\MODEL-AGRI-SDC.xlsx")
ag = ag.drop(columns=['Unnamed: 0'])

Q1 = ag['Yield (Tonnes / Hectre)'].quantile(0.25)
Q3 = ag['Yield (Tonnes / Hectre)'].quantile(0.75)
IQR = Q3 - Q1

lb = Q1 - 1.5 * IQR
ub = Q3 + 1.5 * IQR

outliers = ag[(ag['Yield (Tonnes / Hectre)'] < lb) | (ag['Yield (Tonnes / Hectre)'] > ub)]

out_rem = ag[(ag['Yield (Tonnes / Hectre)'] >= lb) & (ag['Yield (Tonnes / Hectre)'] <= ub)]



l_area = LabelEncoder()
l_item = LabelEncoder()

ag['Area'] = l_area.fit_transform(ag['Area'])
ag['Item'] = l_item.fit_transform(ag['Item'])


x = ag[['Area','Item','Year','Avg Rainfall / Year (mm )', 'Pesticides (Tonnes)', 'Avg Temp']]
y = ag['Yield (Tonnes / Hectre)']

x_tr, x_te, y_tr, y_te = train_test_split(x, y, random_state = 42, test_size=0.2)

model = RandomForestRegressor(random_state=42)
model.fit(x_tr, y_tr)

joblib.dump(model,'AGRISOL_model.pkl')
