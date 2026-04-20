# us-aviation-analytics-and-predictive-modeling
End-to-End US Flight Delay Prediction &amp; Data Analytics Project (2016-2017) using BigQuery, Power BI, and Machine Learning
# ✈️ US Flight Analytics & Predictive Modeling (2016-2017)

[🇹🇷 Türkçe versiyon için aşağıya kaydırın](#türkçe-versiyon)

This repository contains an end-to-end data analytics and machine learning project based on over 11 million domestic US flights from 2016 and 2017. The main goal of this project is not just to report historical data, but to predict future flight cancellations and delay durations using machine learning models.

## 🛠️ Tech Stack & Workflow
* **Data Extraction & Transformation:** Processed 11+ million rows of raw aviation data using **Google BigQuery**. Cleaned and prepared the dataset for modeling.
* **Machine Learning:** Built classification models to predict flight cancellations and regression models to estimate delay times in minutes.
* **Data Visualization & BI:** Designed an interactive, dark-themed **Power BI** dashboard. Used DAX and bookmarks to create a web-app-like user experience for executive reporting.

## 📊 Key Findings & Model Performance
* **Historical Insight:** The overall On-Time Performance (OTP) is 81.52%. The most significant cause of delays is "Late Aircraft" (cascading delays), accounting for 37% of all issues.
* **Cancellation Prediction:** The classification model achieved an **82% Accuracy** rate in identifying flights with a high risk of cancellation.
* **Delay Prediction:** The regression model forecasts actual delay times with a Mean Absolute Error (**MAE**) of only **10.2 minutes**.

## 📸 Dashboard Previews

### 1. Executive Performance Overview
A high-level view of airline OTP, delay causes, and the busiest airports.
<img width="720" height="544" alt="1" src="https://github.com/user-attachments/assets/5568776e-23bd-48bb-864d-f44295cf1e78" />


### 2. Machine Learning: Cancellation Radar
Confusion matrix and prediction distribution showing how the model flags high-risk flights.
<img width="1275" height="719" alt="3 5" src="https://github.com/user-attachments/assets/1e0afbce-394b-4e41-ac90-839a48649bcc" />

### 3. Predictive Delay Analysis
Comparing actual historical delays (gray bars) against the machine learning model's predictions (red line).
<img width="719" height="403" alt="4" src="https://github.com/user-attachments/assets/4e72c7da-8bce-4562-9ee8-f8d836cc5c4f" />

---
# 🇹🇷 ABD Uçuş Analitiği ve Gecikme Tahmini (2016-2017)

Bu depo, 2016 ve 2017 yıllarına ait 11 milyondan fazla ABD iç hat uçuş verisi kullanılarak geliştirilmiş uçtan uca bir veri bilimi projesini içermektedir. Projenin temel amacı sadece geçmiş verileri raporlamak değil; makine öğrenmesi kullanarak gelecekteki uçuş iptallerini ve olası gecikme sürelerini önceden tahmin edebilmektir.

## 🛠️ Kullanılan Araçlar ve İş Akışı
* **Veri İşleme (ETL):** 11 milyon satırlık ham veri **Google BigQuery** üzerinde SQL ile işlendi, temizlendi ve modellemeye hazır hale getirildi.
* **Makine Öğrenmesi:** İptal risklerini tespit etmek için sınıflandırma (classification) ve gecikme sürelerini hesaplamak için regresyon (regression) modelleri kuruldu.
* **İş Zekası (BI):** Karar vericiler için **Power BI** kullanılarak interaktif ve "Dark Mode" temalı bir yönetici paneli tasarlandı. Sayfalar arası geçiş için Bookmark (Yer İşareti) mimarisi kullanıldı.

## 📊 Temel Çıktılar ve Model Başarısı
* **Mevcut Durum:** Uçuşların zamanında kalkış oranı (OTP) %81.52 olarak ölçüldü. Rötarların en büyük sebebi (%37) önceki uçağın geç gelmesiyle oluşan zincirleme gecikmeler.
* **İptal Tahmini:** Kurulan makine öğrenmesi modeli, uçuş iptallerini **%82 doğruluk payı (Accuracy)** ile önceden tespit edebiliyor.
* **Gecikme Tahmini:** Gecikme süresi tahminleme modelimiz, gerçek rötar sürelerini sadece **10.2 dakikalık bir sapma (MAE)** ile öngörüyor.

## 📸 Dashboard Ekran Görüntüleri

### 1. Genel Performans Özeti
Havayolu başarı oranları, gecikme nedenleri ve yoğunluk haritası.
<img width="720" height="544" alt="1" src="https://github.com/user-attachments/assets/5568776e-23bd-48bb-864d-f44295cf1e78" />

### 2. Makine Öğrenmesi: İptal Radarı
Modelin riskli uçuşları nasıl sınıflandırdığını gösteren doğruluk analizi ve karmaşıklık matrisi.
<img width="720" height="404" alt="3" src="https://github.com/user-attachments/assets/128917a0-2b93-4498-890d-4e7baad27d25" />


### 3. Gecikme Tahmini Analizi
Gerçekleşen gecikme süreleri (gri sütunlar) ile yapay zeka modelinin tahminlerinin (kırmızı çizgi) karşılaştırması.
<img width="719" height="403" alt="4" src="https://github.com/user-attachments/assets/29215f01-b3b3-4e37-a8ff-f1b4b5e9791e" />


### 🗄️ Veri Kaynağı (Dataset)
Bu projenin analizinde kullanılan orijinal veri setine Kaggle profilim üzerinden ulaşabilirsiniz:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/murattcell/)
[![Kaggle Dataset](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white)](https://www.kaggle.com/datasets/yuanyuwendymu/airline-delay-and-cancellation-data-2009-2018?select=2016.csv)


![Google BigQuery](https://img.shields.io/badge/Google_BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)
