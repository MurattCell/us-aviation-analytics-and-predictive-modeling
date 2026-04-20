# us-aviation-analytics-and-predictive-modeling
End-to-End US Flight Delay Prediction &amp; Data Analytics Project (2016-2017) using BigQuery, Power BI, and Machine Learning
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

