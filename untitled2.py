# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kpCu_n92FEHnaF59ecT1JhBJ_U-c5nFN
"""

# Anomaliyalarni aniqlash uchun kerakli kutubxonalarni o'rnatamiz
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor

# 1. Sintetik ma'lumotlar yaratish
np.random.seed(42)
# Normal ma'lumotlar
normal_data = np.random.normal(0, 1, size=(100, 2))

# Anomaliyalar
anomalies = np.random.uniform(low=-6, high=6, size=(10, 2))

# Hammasini birlashtiramiz
data = np.vstack([normal_data, anomalies])
labels = np.array([0]*100 + [1]*10)  # 0 = normal, 1 = anomaly

# Ma'lumotlarni DataFrame shaklida saqlaymiz
df = pd.DataFrame(data, columns=['Feature1', 'Feature2'])
df['Label'] = labels

# 2. Ma'lumotlarni vizualizatsiya qilish
plt.figure(figsize=(8, 6))
plt.scatter(df['Feature1'], df['Feature2'], c=df['Label'], cmap='coolwarm', s=50, edgecolor='k')
plt.title("Ma'lumotlar (Normal va Anomaliyalar)")
plt.xlabel("Xususiyat 1")
plt.ylabel("Xususiyat 2")
plt.show()

# 3. Anomaliyalarni aniqlash usullari
## a. Isolation Forest
isolation_forest = IsolationForest(contamination=0.1, random_state=42)
df['IF_Prediction'] = isolation_forest.fit_predict(df[['Feature1', 'Feature2']])

## b. Local Outlier Factor (LOF)
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
df['LOF_Prediction'] = lof.fit_predict(df[['Feature1', 'Feature2']])

# Predictionlarni -1 (anomaliya) va 1 (normal) dan ko'rinishda keltiramiz
df['IF_Anomaly'] = df['IF_Prediction'] == -1
df['LOF_Anomaly'] = df['LOF_Prediction'] == -1

# 4. Anomaliyalarni vizualizatsiya qilish
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Isolation Forest natijalari
ax[0].scatter(df['Feature1'], df['Feature2'], c=df['IF_Anomaly'], cmap='coolwarm', s=50, edgecolor='k')
ax[0].set_title("Isolation Forest Anomaliyalar")
ax[0].set_xlabel("Xususiyat 1")
ax[0].set_ylabel("Xususiyat 2")

# LOF natijalari
ax[1].scatter(df['Feature1'], df['Feature2'], c=df['LOF_Anomaly'], cmap='coolwarm', s=50, edgecolor='k')
ax[1].set_title("LOF Anomaliyalar")
ax[1].set_xlabel("Xususiyat 1")
ax[1].set_ylabel("Xususiyat 2")

plt.show()