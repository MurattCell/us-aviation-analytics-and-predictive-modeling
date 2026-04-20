CREATE OR REPLACE VIEW `stone-arch-474621-h4.airplane_dataset.regresyon_2016_train_dataset_v3` AS
WITH limits AS (
  -- Modelin kafasını karıştırmamak için uç değerleri (Outlier) %0.5'lik dilimle sınırlıyoruz
  SELECT 
    APPROX_QUANTILES(ARR_DELAY, 1000)[OFFSET(5)] AS lower_limit,
    APPROX_QUANTILES(ARR_DELAY, 1000)[OFFSET(995)] AS upper_limit 
  FROM `stone-arch-474621-h4.airplane_dataset.sample100k_2016`
  WHERE CANCELLED = 0 AND DIVERTED = 0 AND ARR_DELAY IS NOT NULL
)
SELECT 
  t.ARR_DELAY,        -- Hedef değişken (Tahmin edilecek değer)
  t.DEP_DELAY,        -- En temel tahmin edici (Kalkış rötarı)
  t.DISTANCE,         -- Yol mesafesi
  t.OP_CARRIER as carrier, -- Havayolu şirketi etkisi
  t.ORIGIN,           -- Kalkış havaalanı karakteristiği
  
  -- ZAMAN ÖZELLİKLERİ (Mevsimsellik ve gün içi döngü)
  `stone-arch-474621-h4.udf_library.fn_month_name`(FL_DATE) as month_name,
  `stone-arch-474621-h4.udf_library.fn_day_name`(FL_DATE) as day_name,
  `stone-arch-474621-h4.udf_library.fn_time_slice`(cast(DEP_TIME as string)) as flight_period,
  
  -- ROTA ÖZELLİĞİ (Senin yöntemin: Origin-Dest birleşimi)
  `stone-arch-474621-h4.udf_library.fn_create_route`(ORIGIN, DEST) as route,
  
  -- TRAFİK YOĞUNLUĞU (Fıskiyeyi kapatacak olan gizli silah)
  -- Varış meydanına senin planlanan iniş saat diliminde kaç uçak daha inecek?
  COUNT(*) OVER(
    PARTITION BY t.DEST, t.FL_DATE, 
    `stone-arch-474621-h4.udf_library.fn_time_slice_crs_arr_time`(cast(t.CRS_ARR_TIME as string))
  ) as planned_dest_traffic_load

FROM `stone-arch-474621-h4.airplane_dataset.sample100k_2016` as t, limits
WHERE t.CANCELLED = 0 
  AND t.DIVERTED = 0 
  AND t.ARR_DELAY IS NOT NULL
  -- Sadece bilimsel sınırların içindeki verileri modele öğretiyoruz
  AND t.ARR_DELAY BETWEEN limits.lower_limit AND limits.upper_limit;

---------------------------------------------------------------------------------------------------------------------------------------


  CREATE OR REPLACE VIEW `stone-arch-474621-h4.airplane_dataset.regresyon_2017_test_dataset_v3` AS
SELECT 
  t.ARR_DELAY,        -- Gerçek sonuç (Başarıyı ölçmek için)
  t.DEP_DELAY,
  t.DISTANCE,
  t.OP_CARRIER as carrier,
  t.ORIGIN,
  
  -- Eğitim setiyle birebir aynı özellikler (Features)
  `stone-arch-474621-h4.udf_library.fn_month_name`(FL_DATE) as month_name,
  `stone-arch-474621-h4.udf_library.fn_day_name`(FL_DATE) as day_name,
  `stone-arch-474621-h4.udf_library.fn_time_slice`(cast(DEP_TIME as string)) as flight_period,
  `stone-arch-474621-h4.udf_library.fn_create_route`(ORIGIN, DEST) as route,
  
  -- Test setinin kendi içindeki (2017 trafiği) yoğunluk hesaplaması
  COUNT(*) OVER(
    PARTITION BY t.DEST, t.FL_DATE, 
    `stone-arch-474621-h4.udf_library.fn_time_slice_crs_arr_time`(cast(t.CRS_ARR_TIME as string))
  ) as planned_dest_traffic_load

FROM `stone-arch-474621-h4.airplane_dataset.sample25k_2017` as t
WHERE t.CANCELLED = 0 
  AND t.DIVERTED = 0 
  AND t.ARR_DELAY IS NOT NULL;
