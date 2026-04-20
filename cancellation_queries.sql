/*
DEP_DELAY, ARR_DELAY, AIR_TIME gibi sütunları sildik: Çünkü eğer bir uçuş iptal edildiyse, bu değerler zaten oluşmamıştır (veya NULL'dur). Bu verileri modele verirsen model "Eğer rötar NULL ise uçuş iptaldir" gibi çok basit ve anlamsız bir kural öğrenir. Buna Target Leakage (Hedef Sızıntısı) denir.

CRS_DEP_TIME (Planlanan Saat) bıraktık: İptaller genelde günün yoğun saatlerinde veya hava muhalefetinin arttığı saatlerde kümelenir.


*/

CREATE OR REPLACE VIEW `stone-arch-474621-h4.airplane_dataset.cancelled_dataset_2016_train` AS
SELECT 
  -- HEDEF DEĞİŞKEN
  CAST(CANCELLED AS INT64) as is_cancelled,
  
  -- KATEGORİK ÖZELLİKLER (UDF Destekli)
  OP_CARRIER as carrier,
  ORIGIN as origin,
  DEST as destination,
  
  -- Senin UDF Fonksiyonların
  `stone-arch-474621-h4.udf_library.fn_month_name`(FL_DATE) as month_name,
  `stone-arch-474621-h4.udf_library.fn_day_name`(FL_DATE) as day_name,
  -- Planlanan saate göre günün dilimi (Morning, Afternoon vb.)
  `stone-arch-474621-h4.udf_library.fn_time_slice`(CAST(CRS_DEP_TIME AS STRING)) as flight_period,
  -- Rota birleşimi (Origin-Dest)
  `stone-arch-474621-h4.udf_library.fn_create_route`(ORIGIN, DEST) as route,
  
  -- SAYISAL ÖZELLİKLER
  DISTANCE as distance,
  CRS_DEP_TIME as planned_dep_time -- Modelin saat bazlı ince ayar yapabilmesi için ham hali

FROM `stone-arch-474621-h4.airplane_dataset.sample100k_2016`
WHERE DIVERTED = 0 -- Sadece net sonuçlara odaklanıyoruz
;
--TEST 
----------------------------------------------------------------------------------------------------------------

CREATE OR REPLACE VIEW `stone-arch-474621-h4.airplane_dataset.cancelled_dataset_2017_test` AS
SELECT 
  CAST(CANCELLED AS INT64) as is_cancelled,
  OP_CARRIER as carrier,
  ORIGIN as origin,
  DEST as destination,
  `stone-arch-474621-h4.udf_library.fn_month_name`(FL_DATE) as month_name,
  `stone-arch-474621-h4.udf_library.fn_day_name`(FL_DATE) as day_name,
  `stone-arch-474621-h4.udf_library.fn_time_slice`(CAST(CRS_DEP_TIME AS STRING)) as flight_period,
  `stone-arch-474621-h4.udf_library.fn_create_route`(ORIGIN, DEST) as route,
  DISTANCE as distance,
  CRS_DEP_TIME as planned_dep_time

FROM `stone-arch-474621-h4.airplane_dataset.sample25k_2017`
WHERE DIVERTED = 0
