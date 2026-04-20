# matplotlib deki grafikte kırmızı cızgi ıcın terminalde runla
# pip install statsmodels

import os
from google.cloud import bigquery

from sklearn.ensemble import HistGradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# BAĞLANTI AYARI
# Kendi lokalinizde çalıştırırken JSON anahtarınızın dosya yolunu buraya girin
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "google_cloud_api_key_yolunuzu_buraya_yazin.json"
project_id = "stone-arch-474621-h4"
client = bigquery.Client(project=project_id) # : BigQuery ile konuşacak olan elçiyi oluşturur

# VERİ ÇEKME
print(" Veri BigQuery'den çekiliyor...")

query_train = "SELECT * FROM `stone-arch-474621-h4.airplane_dataset.regresyon_2016_train_dataset_v3`"
df_train = client.query(query_train).to_dataframe()
print(f" {len(df_train)} satır başarıyla yüklendi.")


query_test = "SELECT * FROM `stone-arch-474621-h4.airplane_dataset.regresyon_2017_test_dataset_v3`"
df_test  =client.query(query_test).to_dataframe()
print(f" {len(df_test)} satır başarıyla yüklendi.")



# A. Karışıklığı önlemek için işaret koyalım ve birleştirelim
# burada amac sutun ıcındeki degiskenlerden türedigi ıcın model birinde olup digerinde olmazsa boyut hatası vermesin diye
df_train['is_train'] = 1
df_test['is_train'] = 0
df_combined = pd.concat([df_train, df_test], axis=0)

# B. Kategorik sütunları seçelim
# planned_dest_traffic_load sayısal buradan cıkarttım. bigquery de sutun olusturmustum
categorical_cols = ['carrier', 'ORIGIN', 'month_name', 'day_name', 'flight_period', 'route']

print(f" Encoding öncesi sütun sayısı: {df_combined.shape[1]}")

# C. Tüm kategorikleri 0-1 (Dummy) haline getirelim

df_final = pd.get_dummies(df_combined, columns=categorical_cols, drop_first=True)
# drop_first=True her sutundaki unique veriden 1 eksilerek tahmin yapmak ıcın yazıldı.
# mesela gun 7 adet -1 = 6 gunluk kombinasypn yaptı o gizledigi deger sıfır noktası (baseline) oluyor

# D. Tekrar Train ve Test olarak ayıralım
train_v3 = df_final[df_final['is_train'] == 1].drop(['is_train'], axis=1)
test_v3 = df_final[df_final['is_train'] == 0].drop(['is_train'], axis=1)

# E. Özellik (X) ve Hedef (y) ayırımı
X_train = train_v3.drop(['ARR_DELAY'], axis=1)
y_train = train_v3['ARR_DELAY']

X_test = test_v3.drop(['ARR_DELAY'], axis=1)
y_test = test_v3['ARR_DELAY']

print(f" Encoding sonrası TOPLAM sütun sayısı: {X_train.shape[1]}")


# Modeli tanımla ve eğit
# Not: max_iter değerini 100'den 200'e çıkararak modelin "öğrenme" kapasitesini artırdık
model = HistGradientBoostingRegressor(max_iter=200, random_state=42)

print(" Model eğitiliyor (v3)...")
model.fit(X_train, y_train)

# Tahmin yap
y_pred = model.predict(X_test)



# Metrikler
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"\n--- v3 MODEL PERFORMANSI ---")
print(f" R2 Skoru: {r2:.4f}")
print(f" Ortalama Hata (MAE): {mae:.2f} dakika")
print(f" RMSE: {rmse:.2f} dakika")

# Grafiği çizdirelim (Artık Analizi)
plt.figure(figsize=(10, 6))
sns.residplot(x=y_pred, y=y_test - y_pred, lowess=True, line_kws={'color': 'red'})
plt.title('v3 Model Residual Plot (Hata Dağılımı)')
plt.xlabel('Tahmin Edilen Değerler')
plt.ylabel('Hatalar (Gerçek - Tahmin)')
plt.show()
# --- POWER BI REGRESYON ÇIKTISI OLUŞTURMA ---
# y_test: Gerçek gecikme dakikaları, y_pred: Modelin tahmin ettiği dakikalar
df_regresyon_sonuc = pd.DataFrame({
    'Gercek_Gecikme_Dakika': y_test, 
    'Tahmin_Gecikme_Dakika': y_pred
})

# Dosyayı "Yeni klasör (2)" içine kaydedecek
df_regresyon_sonuc.to_csv('gecikme_tahmin_sonuclari.csv', index=False)

print("\n[BAŞARILI] Power BI için 'gecikme_tahmin_sonuclari.csv' dosyası oluşturuldu.")
