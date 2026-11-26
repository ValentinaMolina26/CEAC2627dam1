INSERT INTO vehiculos (marca, modelo, version, categoria, descripcion, anio_fabricacion, fecha_matriculacion, matricula, pais, color, combustible, potencia, cilindrada, kilometraje, numero_puertas, numero_plazas, consumo_medio, automatico, disponible, segunda_mano, imagen, url_fabricante, precio_original, precio_venta, garantia_vigente)
VALUES
('BMW', 'Serie 1', '118i', 'Compacto', 'Coche compacto deportivo de cinco plazas', 2022, '2022-03-12', '2345 KLP', 'Alemania', 'Negro', 'Gasolina', 136, 1499, 32000, 5, 5, 5.8, 1, 1, 1, 'bmw_serie1.jpg', 'https://www.bmw.es', 32000.00, 26900.00, 0),

('Volkswagen', 'Golf', '1.5 TSI', 'Compacto', 'Vehiculo compacto de diseño moderno', 2023, '2023-06-20', '3456 MNP', 'Alemania', 'Azul', 'Gasolina', 150, 1498, 18000, 5, 5, 5.6, 0, 1, 1, 'golf.jpg', 'https://www.volkswagen.es', 29000.00, 25500.00, 1),

('Seat', 'Leon', 'FR 2.0 TDI', 'Compacto', 'Vehiculo deportivo con motor diesel', 2021, '2021-09-10', '4567 LRS', 'Espana', 'Rojo', 'Diesel', 150, 1968, 65000, 5, 5, 4.8, 1, 1, 1, 'seat_leon.jpg', 'https://www.seat.es', 28000.00, 21500.00, 0),

('Hyundai', 'Tucson', 'Hybrid Tecno', 'SUV', 'SUV familiar con tecnologia hibrida', 2024, '2024-02-18', '5678 NBT', 'Corea del Sur', 'Gris', 'Hibrido', 215, 1598, 12000, 5, 5, 5.3, 1, 1, 0, 'tucson.jpg', 'https://www.hyundai.com/es', 38000.00, 34500.00, 1),

('Kia', 'Sportage', '1.6 T-GDI', 'SUV', 'SUV espacioso ideal para viajes familiares', 2022, '2022-11-05', '6789 MCV', 'Corea del Sur', 'Blanco', 'Gasolina', 150, 1598, 41000, 5, 5, 6.5, 1, 1, 1, 'sportage.jpg', 'https://www.kia.com/es', 33000.00, 27900.00, 0),

('Mercedes-Benz', 'Clase A', 'A200', 'Compacto', 'Compacto premium con acabado elegante', 2023, '2023-04-14', '7890 LDF', 'Alemania', 'Negro', 'Gasolina', 163, 1332, 22000, 5, 5, 6.1, 1, 1, 1, 'clase_a.jpg', 'https://www.mercedes-benz.es', 39000.00, 33500.00, 1),

('Audi', 'A3', '35 TFSI', 'Berlina', 'Berlina compacta de alta calidad', 2022, '2022-07-22', '8901 KGH', 'Alemania', 'Gris', 'Gasolina', 150, 1498, 37000, 5, 5, 5.9, 1, 1, 1, 'audi_a3.jpg', 'https://www.audi.es', 36000.00, 29900.00, 0),

('Renault', 'Clio', 'Techno TCe', 'Utilitario', 'Coche urbano economico y manejable', 2024, '2024-01-16', '9012 MJK', 'Francia', 'Azul', 'Gasolina', 90, 999, 8000, 5, 5, 5.2, 0, 1, 0, 'clio.jpg', 'https://www.renault.es', 21000.00, 19500.00, 1),

('Peugeot', '208', 'Allure PureTech', 'Utilitario', 'Vehiculo urbano de diseño moderno', 2023, '2023-08-09', '1122 LBC', 'Francia', 'Amarillo', 'Gasolina', 100, 1199, 15000, 5, 5, 5.4, 0, 1, 1, 'peugeot_208.jpg', 'https://www.peugeot.es', 22000.00, 18900.00, 0),

('Ford', 'Focus', 'ST-Line EcoBoost', 'Compacto', 'Compacto dinamico con buen rendimiento', 2021, '2021-05-19', '2233 KTR', 'Estados Unidos', 'Rojo', 'Gasolina', 125, 999, 58000, 5, 5, 5.7, 0, 1, 1, 'focus.jpg', 'https://www.ford.es', 27000.00, 20500.00, 0),

('Dacia', 'Sandero', 'Stepway TCe', 'Utilitario', 'Coche economico con carroceria elevada', 2023, '2023-10-11', '3344 MDP', 'Rumania', 'Naranja', 'Gasolina', 90, 999, 14000, 5, 5, 5.6, 0, 1, 1, 'sandero.jpg', 'https://www.dacia.es', 19000.00, 15900.00, 0),

('Nissan', 'Qashqai', 'Mild Hybrid', 'SUV', 'SUV familiar con tecnologia de asistencia', 2024, '2024-03-21', '4455 NFK', 'Japon', 'Gris', 'Hibrido', 158, 1332, 10000, 5, 5, 6.2, 1, 1, 0, 'qashqai.jpg', 'https://www.nissan.es', 35000.00, 31900.00, 1),

('Volvo', 'XC40', 'B3 Core', 'SUV', 'SUV premium con sistemas de seguridad', 2022, '2022-12-02', '5566 LMP', 'Suecia', 'Blanco', 'Gasolina', 163, 1969, 29000, 5, 5, 6.5, 1, 1, 1, 'xc40.jpg', 'https://www.volvocars.com/es', 42000.00, 34900.00, 0),

('Tesla', 'Model 3', 'Long Range', 'Berlina', 'Vehiculo electrico con gran autonomia', 2024, '2024-04-08', '6677 MRS', 'Estados Unidos', 'Blanco', 'Electrico', 498, 0, 9000, 4, 5, 0, 1, 1, 0, 'model3.jpg', 'https://www.tesla.com/es_es', 48000.00, 43900.00, 1),

('Fiat', '500', 'Dolcevita', 'Utilitario', 'Pequeño coche urbano de estilo italiano', 2022, '2022-06-15', '7788 KVN', 'Italia', 'Verde', 'Gasolina', 70, 999, 35000, 3, 4, 5.1, 0, 1, 1, 'fiat500.jpg', 'https://www.fiat.es', 18000.00, 14500.00, 0),

('Mazda', 'CX-5', 'Skyactiv-G', 'SUV', 'SUV familiar con diseño elegante', 2023, '2023-02-27', '8899 LWT', 'Japon', 'Rojo', 'Gasolina', 165, 1998, 24000, 5, 5, 6.8, 0, 1, 1, 'cx5.jpg', 'https://www.mazda.es', 36000.00, 30900.00, 0),

('Honda', 'Civic', 'e:HEV Sport', 'Berlina', 'Berlina hibrida de gran eficiencia', 2024, '2024-07-10', '9900 MGH', 'Japon', 'Azul', 'Hibrido', 184, 1993, 5000, 5, 5, 4.7, 1, 1, 0, 'civic.jpg', 'https://www.honda.es', 39000.00, 36500.00, 1),

('Skoda', 'Octavia', '1.5 TSI', 'Berlina', 'Berlina espaciosa para uso familiar', 2022, '2022-09-17', '1023 KBC', 'Republica Checa', 'Gris', 'Gasolina', 150, 1498, 44000, 5, 5, 5.7, 1, 1, 1, 'octavia.jpg', 'https://www.skoda.es', 31000.00, 25900.00, 0),

('Citroen', 'C3', 'Feel Pack', 'Utilitario', 'Coche urbano compacto y confortable', 2021, '2021-04-23', '2134 LFD', 'Francia', 'Blanco', 'Gasolina', 83, 1199, 52000, 5, 5, 5.5, 0, 1, 1, 'citroen_c3.jpg', 'https://www.citroen.es', 17500.00, 12900.00, 0),

('Jeep', 'Renegade', 'Longitude', 'SUV', 'SUV compacto preparado para diferentes terrenos', 2022, '2022-05-30', '3245 MJK', 'Estados Unidos', 'Verde', 'Gasolina', 120, 1332, 39000, 5, 5, 6.7, 1, 1, 1, 'renegade.jpg', 'https://www.jeep.es', 29000.00, 23900.00, 0),

('Lexus', 'UX', '250h', 'SUV', 'SUV premium con motor hibrido', 2023, '2023-11-19', '4356 NPL', 'Japon', 'Negro', 'Hibrido', 184, 1987, 16000, 5, 5, 5.0, 1, 1, 0, 'lexus_ux.jpg', 'https://www.lexus.es', 43000.00, 38900.00, 1),

('Porsche', 'Macan', 'T', 'SUV', 'SUV deportivo de altas prestaciones', 2021, '2021-08-13', '5467 KRS', 'Alemania', 'Azul', 'Gasolina', 265, 1984, 47000, 5, 5, 8.5, 1, 1, 1, 'macan.jpg', 'https://www.porsche.com/spain', 72000.00, 58900.00, 0),

('Land Rover', 'Discovery Sport', 'D200', 'SUV', 'SUV todoterreno de siete plazas', 2022, '2022-10-06', '6578 LMT', 'Reino Unido', 'Gris', 'Diesel', 204, 1997, 43000, 5, 7, 6.9, 1, 1, 1, 'discovery.jpg', 'https://www.landrover.es', 59000.00, 48900.00, 0),

('Mini', 'Cooper', 'Classic', 'Utilitario', 'Vehiculo compacto de estilo deportivo', 2023, '2023-05-04', '7689 MBC', 'Reino Unido', 'Verde', 'Gasolina', 136, 1499, 21000, 3, 4, 5.8, 1, 1, 1, 'mini_cooper.jpg', 'https://www.mini.es', 30000.00, 25900.00, 0),

('Opel', 'Corsa', 'GS Line', 'Utilitario', 'Coche urbano practico y eficiente', 2022, '2022-02-25', '8790 KDP', 'Alemania', 'Amarillo', 'Gasolina', 100, 1199, 33000, 5, 5, 5.3, 0, 1, 1, 'corsa.jpg', 'https://www.opel.es', 21000.00, 16900.00, 0),

('Cupra', 'Formentor', 'VZ 2.0 TSI', 'SUV', 'SUV deportivo con motor de altas prestaciones', 2024, '2024-06-12', '9801 LRN', 'Espana', 'Gris', 'Gasolina', 310, 1984, 7000, 5, 5, 8.0, 1, 1, 0, 'formentor.jpg', 'https://www.cupraofficial.es', 52000.00, 47900.00, 1),

('Alfa Romeo', 'Giulia', 'Veloce', 'Berlina', 'Berlina italiana de caracter deportivo', 2021, '2021-03-18', '1098 MTS', 'Italia', 'Rojo', 'Gasolina', 280, 1995, 49000, 4, 5, 7.0, 1, 1, 1, 'giulia.jpg', 'https://www.alfaromeo.es', 49000.00, 35900.00, 0),

('Subaru', 'Forester', 'Sport', 'SUV', 'SUV con traccion integral y gran espacio', 2023, '2023-07-07', '2109 KLM', 'Japon', 'Verde', 'Gasolina', 150, 1995, 19000, 5, 5, 7.2, 1, 1, 0, 'forester.jpg', 'https://www.subaru.es', 39000.00, 34900.00, 1),

('Mitsubishi', 'ASX', 'Kaiteki', 'SUV', 'SUV compacto de diseño moderno', 2022, '2022-01-29', '3210 NBR', 'Japon', 'Blanco', 'Gasolina', 150, 1332, 36000, 5, 5, 6.0, 1, 1, 1, 'asx.jpg', 'https://www.mitsubishi-motors.es', 29000.00, 22900.00, 0),

('BYD', 'Atto 3', 'Comfort', 'SUV', 'SUV electrico con equipamiento tecnologico', 2024, '2024-08-16', '4321 MCV', 'China', 'Azul', 'Electrico', 204, 0, 3000, 5, 5, 0, 1, 1, 0, 'atto3.jpg', 'https://www.byd.com/es', 41000.00, 37900.00, 1),

('MG', 'ZS', 'Luxury', 'SUV', 'SUV familiar de precio competitivo', 2023, '2023-09-24', '5432 LPK', 'China', 'Rojo', 'Gasolina', 111, 1498, 17000, 5, 5, 6.6, 0, 1, 1, 'mg_zs.jpg', 'https://www.mgmotor.eu/es-ES', 24000.00, 19900.00, 0),

('Suzuki', 'Vitara', 'Mild Hybrid', 'SUV', 'SUV compacto con sistema de hibridacion ligera', 2022, '2022-04-11', '6543 KDF', 'Japon', 'Naranja', 'Hibrido', 129, 1373, 42000, 5, 5, 5.7, 1, 1, 1, 'vitara.jpg', 'https://auto.suzuki.es', 27000.00, 21900.00, 0),

('Dodge', 'Challenger', 'R/T', 'Deportivo', 'Coche deportivo americano de gran potencia', 2020, '2020-06-08', '7654 MGH', 'Estados Unidos', 'Negro', 'Gasolina', 375, 5700, 68000, 2, 5, 12.0, 1, 1, 1, 'challenger.jpg', 'https://www.dodge.com', 55000.00, 39900.00, 0),

('Chevrolet', 'Camaro', '2.0 Turbo', 'Deportivo', 'Deportivo americano de diseño agresivo', 2021, '2021-07-15', '8765 LTR', 'Estados Unidos', 'Amarillo', 'Gasolina', 275, 1998, 45000, 2, 4, 8.5, 1, 1, 1, 'camaro.jpg', 'https://www.chevrolet.com', 51000.00, 37900.00, 0),

('Jaguar', 'XE', 'R-Dynamic', 'Berlina', 'Berlina premium de diseño elegante', 2020, '2020-09-22', '9876 KBC', 'Reino Unido', 'Gris', 'Diesel', 180, 1999, 72000, 4, 5, 5.2, 1, 1, 1, 'jaguar_xe.jpg', 'https://www.jaguar.es', 46000.00, 29900.00, 0),

('Infiniti', 'Q50', 'Sport', 'Berlina', 'Berlina japonesa con motor potente', 2019, '2019-05-17', '1987 MNP', 'Japon', 'Blanco', 'Gasolina', 211, 1991, 85000, 4, 5, 7.4, 1, 1, 1, 'q50.jpg', 'https://www.infiniti.com', 42000.00, 23900.00, 0),

('DS Automobiles', 'DS 7', 'E-Tense', 'SUV', 'SUV premium con tecnologia hibrida enchufable', 2023, '2023-12-05', '2987 LFD', 'Francia', 'Negro', 'Hibrido', 225, 1598, 13000, 5, 5, 1.5, 1, 1, 0, 'ds7.jpg', 'https://www.dsautomobiles.es', 49000.00, 43900.00, 1),

('Polestar', '2', 'Long Range', 'Berlina', 'Vehiculo electrico de diseño minimalista', 2024, '2024-09-03', '3876 KTR', 'Suecia', 'Gris', 'Electrico', 299, 0, 4000, 5, 5, 0, 1, 1, 0, 'polestar2.jpg', 'https://www.polestar.com/es', 52000.00, 48900.00, 1),

('Smart', 'ForTwo', 'Passion', 'Utilitario', 'Pequeño vehiculo ideal para ciudad', 2020, '2020-02-14', '4765 MBC', 'Alemania', 'Blanco', 'Gasolina', 71, 999, 56000, 3, 2, 4.8, 0, 1, 1, 'smart.jpg', 'https://www.smart.com', 16000.00, 10900.00, 0),

('Toyota', 'Yaris', 'Cross Hybrid', 'SUV', 'SUV urbano con tecnologia hibrida', 2023, '2023-03-09', '5654 LPK', 'Japon', 'Gris', 'Hibrido', 116, 1490, 23000, 5, 5, 4.5, 1, 1, 1, 'yaris_cross.jpg', 'https://www.toyota.es', 30000.00, 25900.00, 1),

('Volkswagen', 'Tiguan', 'R-Line', 'SUV', 'SUV familiar con amplio espacio interior', 2024, '2024-10-02', '6543 NBT', 'Alemania', 'Azul', 'Diesel', 150, 1968, 6000, 5, 5, 5.5, 1, 1, 0, 'tiguan.jpg', 'https://www.volkswagen.es', 45000.00, 41900.00, 1),

('Ford', 'Mustang', 'GT', 'Deportivo', 'Deportivo americano con motor V8', 2021, '2021-11-12', '7432 KRS', 'Estados Unidos', 'Rojo', 'Gasolina', 450, 5038, 38000, 2, 4, 12.5, 1, 1, 1, 'mustang.jpg', 'https://www.ford.es', 65000.00, 52900.00, 0),

('Renault', 'Captur', 'E-Tech', 'SUV', 'SUV urbano con tecnologia hibrida', 2023, '2023-01-25', '8321 LMT', 'Francia', 'Naranja', 'Hibrido', 145, 1598, 20000, 5, 5, 4.8, 1, 1, 1, 'captur.jpg', 'https://www.renault.es', 31000.00, 26900.00, 1),

('Peugeot', '3008', 'Hybrid', 'SUV', 'SUV familiar con motorizacion hibrida', 2022, '2022-08-30', '9210 MJK', 'Francia', 'Blanco', 'Hibrido', 225, 1598, 34000, 5, 5, 1.6, 1, 1, 1, 'peugeot3008.jpg', 'https://www.peugeot.es', 39000.00, 31900.00, 0),

('Audi', 'Q5', '40 TDI', 'SUV', 'SUV premium con motor diesel', 2023, '2023-05-28', '1092 KDF', 'Alemania', 'Negro', 'Diesel', 204, 1968, 26000, 5, 5, 5.8, 1, 1, 1, 'audi_q5.jpg', 'https://www.audi.es', 55000.00, 46900.00, 1),

('BMW', 'X3', 'xDrive20d', 'SUV', 'SUV premium con traccion integral', 2022, '2022-07-19', '2183 MGH', 'Alemania', 'Azul', 'Diesel', 190, 1995, 39000, 5, 5, 5.6, 1, 1, 1, 'bmw_x3.jpg', 'https://www.bmw.es', 52000.00, 42900.00, 0),

('Mercedes-Benz', 'GLC', '220d', 'SUV', 'SUV premium con amplio equipamiento', 2024, '2024-11-08', '3274 LBC', 'Alemania', 'Blanco', 'Diesel', 197, 1993, 3000, 5, 5, 5.1, 1, 1, 0, 'mercedes_glc.jpg', 'https://www.mercedes-benz.es', 62000.00, 58900.00, 1),

('Kia', 'EV6', 'GT-Line', 'SUV', 'Vehiculo electrico de diseño futurista', 2023, '2023-04-06', '4365 KLP', 'Corea del Sur', 'Verde', 'Electrico', 229, 0, 15000, 5, 5, 0, 1, 1, 0, 'kia_ev6.jpg', 'https://www.kia.com/es', 49000.00, 43900.00, 1),

('Hyundai', 'Ioniq 5', 'Style', 'SUV', 'SUV electrico con tecnologia avanzada', 2024, '2024-05-23', '5456 MNP', 'Corea del Sur', 'Gris', 'Electrico', 229, 0, 8000, 5, 5, 0, 1, 1, 0, 'ioniq5.jpg', 'https://www.hyundai.com/es', 51000.00, 47500.00, 1),

('Fiat', 'Panda', 'City Life', 'Utilitario', 'Coche urbano pequeño y funcional', 2021, '2021-10-16', '6547 NRS', 'Italia', 'Rojo', 'Gasolina', 70, 999, 48000, 5, 5, 5.0, 0, 1, 1, 'panda.jpg', 'https://www.fiat.es', 15000.00, 11900.00, 0),

('Mazda', 'MX-5', 'Roadster', 'Deportivo', 'Deportivo descapotable de dos plazas', 2022, '2022-06-03', '7638 LDF', 'Japon', 'Rojo', 'Gasolina', 184, 1998, 27000, 2, 2, 6.9, 0, 1, 1, 'mx5.jpg', 'https://www.mazda.es', 36000.00, 29900.00, 0),

('Honda', 'HR-V', 'Advance', 'SUV', 'SUV compacto con tecnologia hibrida', 2023, '2023-09-14', '8729 MCV', 'Japon', 'Blanco', 'Hibrido', 131, 1498, 19000, 5, 5, 5.4, 1, 1, 1, 'honda_hrv.jpg', 'https://www.honda.es', 34000.00, 29900.00, 1),

('Skoda', 'Kodiaq', 'Sportline', 'SUV', 'SUV familiar de gran capacidad', 2022, '2022-12-21', '9810 KTR', 'Republica Checa', 'Negro', 'Diesel', 150, 1968, 46000, 5, 7, 5.9, 1, 1, 1, 'kodiaq.jpg', 'https://www.skoda.es', 42000.00, 34900.00, 0);
