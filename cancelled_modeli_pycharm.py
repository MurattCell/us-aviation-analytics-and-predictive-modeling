
import os
from google.cloud import bigquery

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


# BAĞLANTI AYARI
#os.environ[...]: key.json Google servislerine tanıtarak "Ben bu projeye erişmeye yetkiliyim" demek
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\halil\OneDrive\Desktop\key.json"
project_id = "stone-arch-474621-h4"
client = bigquery.Client(project=project_id) # : BigQuery ile konuşacak olan elçiyi oluşturur

# VERİ ÇEKME
print(" Veri BigQuery'den çekiliyor...")

query_train = "SELECT * FROM `stone-arch-474621-h4.airplane_dataset.cancelled_dataset_2016_train`"
df_train = client.query(query_train).to_dataframe()
print(f" {len(df_train)} satır başarıyla yüklendi.")


query_test = "SELECT * FROM `stone-arch-474621-h4.airplane_dataset.cancelled_dataset_2017_test`"
df_test  =client.query(query_test).to_dataframe()
print(f" {len(df_test)} satır başarıyla yüklendi.")


# 1. ETİKETLE VE BİRLEŞTİR
# Veri çekme kısmından hemen sonra burası başlar
df_train['is_train'] = 1
df_test['is_train'] = 0
df_combined = pd.concat([df_train, df_test], axis=0)

# Sütun isimlerini küçük harfe sabitleyelim (BigQuery bazen büyük harf döndürebilir)
df_combined.columns = [col.lower() for col in df_combined.columns]

# 2. KATEGORİK SÜTUNLARI GÜNCELLE
# Yeni eklediğimiz 'flight_period' ve 'route' özelliklerini buraya dahil ettik
categorical_cols = ['carrier', 'origin', 'destination', 'month_name', 'day_name', 'flight_period', 'route']

# One-Hot Encoding (Aynı dili konuşmalarını sağlama)
df_final = pd.get_dummies(df_combined, columns=categorical_cols, drop_first=True)

# 3. TEKRAR AYIR VE HEDEF DEĞİŞKENLERİ BELİRLE
X_train = df_final[df_final['is_train'] == 1].drop(['is_train', 'is_cancelled'], axis=1)
y_train = df_final[df_final['is_train'] == 1]['is_cancelled']

X_test = df_final[df_final['is_train'] == 0].drop(['is_train', 'is_cancelled'], axis=1)
y_test = df_final[df_final['is_train'] == 0]['is_cancelled']

print(f"--- Hazırlık Tamam ---")
print(f"Toplam Özellik Sayısı: {X_train.shape[1]}")

# 4. RANDOM FOREST MODELİNİ KUR VE EĞİT
# class_weight='balanced' sayesinde azınlıktaki iptalleri daha ciddiye alacak
model_rf = RandomForestClassifier(
    n_estimators=150,      # Ağaç sayısını biraz artırdık (Daha fazla tecrübe)
    max_depth=15,          # Derinliği biraz artırdık (Yeni özellikleri iyice kavrasın)
    class_weight='balanced',
    random_state=42,
    n_jobs=-1              # İşlemciyi tam performans kullan (Hızlı eğitim için)
)

print("\nModel Eğitiliyor (İptal Tahmini v2)...")
model_rf.fit(X_train, y_train)

# 5. TAHMİN VE PERFORMANS ANALİZİ
y_pred = model_rf.predict(X_test)

print("\n--- SINIFLANDIRMA PERFORMANSI (v2) ---")
print(classification_report(y_test, y_pred))

# 6. KARMAŞIKLIK MATRİSİ (CONFUSION MATRIX)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges')
plt.title('İptal Tahmini (v2) - Karmaşıklık Matrisi')
plt.xlabel('Tahmin (0: Uçtu, 1: İptal)')
plt.ylabel('Gerçek (0: Uçtu, 1: İptal)')
plt.show()

