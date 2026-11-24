INSERT INTO peliculas (
    titulo, titulo_original, director, genero, sinopsis,
    anio_estreno, fecha_estreno, duracion_minutos, pais,
    idioma_original, clasificacion_edades, presupuesto,
    recaudacion, valoracion_media, numero_valoraciones,
    numero_visualizaciones, disponible, vista, favorita,
    imagen_portada, url_trailer, precio_alquiler, precio_compra,
    formato, subtitulos_disponibles
)
VALUES
('Titanic', 'Titanic', 'James Cameron', 'Romance', 'Historia de amor a bordo del famoso transatlantico.', 1997, '1997-12-19', 195, 'Estados Unidos', 'Ingles', '12', 200000000, 2264000000, 7.9, 2500, 35000, 1, 1, 1, 'titanic.jpg', 'https://youtube.com', 3.99, 12.99, 'HD', 2),

('Avatar', 'Avatar', 'James Cameron', 'Ciencia ficcion', 'Un exmarine descubre el mundo de Pandora.', 2009, '2009-12-18', 162, 'Estados Unidos', 'Ingles', '12', 237000000, 2923000000, 7.9, 3000, 45000, 1, 0, 1, 'avatar.jpg', 'https://youtube.com', 4.99, 14.99, '4K', 3),

('Inception', 'Inception', 'Christopher Nolan', 'Ciencia ficcion', 'Un ladron especializado entra en los sueños de otras personas.', 2010, '2010-07-16', 148, 'Estados Unidos', 'Ingles', '12', 160000000, 839000000, 8.8, 4200, 28000, 1, 1, 1, 'inception.jpg', 'https://youtube.com', 3.99, 11.99, '4K', 2),

('The Dark Knight', 'The Dark Knight', 'Christopher Nolan', 'Accion', 'Batman lucha contra el Joker para salvar Gotham.', 2008, '2008-07-18', 152, 'Estados Unidos', 'Ingles', '12', 185000000, 1005000000, 9.0, 5000, 50000, 1, 1, 1, 'dark_knight.jpg', 'https://youtube.com', 3.99, 12.99, '4K', 3),

('Forrest Gump', 'Forrest Gump', 'Robert Zemeckis', 'Drama', 'Un hombre extraordinario vive acontecimientos historicos.', 1994, '1994-07-06', 142, 'Estados Unidos', 'Ingles', '12', 55000000, 678000000, 8.8, 3500, 22000, 1, 1, 0, 'forrest_gump.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('The Matrix', 'The Matrix', 'Lana Wachowski', 'Ciencia ficcion', 'Un programador descubre que vive dentro de una simulacion.', 1999, '1999-03-31', 136, 'Estados Unidos', 'Ingles', '16', 63000000, 467000000, 8.7, 4000, 31000, 1, 0, 1, 'matrix.jpg', 'https://youtube.com', 3.49, 10.99, '4K', 2),

('Gladiator', 'Gladiator', 'Ridley Scott', 'Accion', 'Un general romano busca venganza tras una traicion.', 2000, '2000-05-05', 155, 'Estados Unidos', 'Ingles', '16', 103000000, 465000000, 8.5, 2800, 19000, 1, 1, 0, 'gladiator.jpg', 'https://youtube.com', 3.99, 11.99, 'HD', 2),

('Joker', 'Joker', 'Todd Phillips', 'Drama', 'La historia de un hombre que se transforma en el Joker.', 2019, '2019-10-04', 122, 'Estados Unidos', 'Ingles', '18', 55000000, 1074000000, 8.4, 3800, 27000, 1, 0, 1, 'joker.jpg', 'https://youtube.com', 4.99, 13.99, '4K', 3),

('Parasite', 'Gisaengchung', 'Bong Joon-ho', 'Suspense', 'Una familia pobre se introduce en la vida de una familia adinerada.', 2019, '2019-05-30', 132, 'Corea del Sur', 'Coreano', '16', 11400000, 263000000, 8.5, 2200, 15000, 1, 1, 1, 'parasite.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 4),

('Coco', 'Coco', 'Lee Unkrich', 'Animacion', 'Un niño descubre el mundo de los muertos a traves de la musica.', 2017, '2017-11-22', 105, 'Estados Unidos', 'Ingles', '7', 175000000, 814000000, 8.4, 2600, 40000, 1, 1, 1, 'coco.jpg', 'https://youtube.com', 2.99, 9.99, '4K', 3),

('The Lion King', 'The Lion King', 'Roger Allers', 'Animacion', 'Simba aprende a aceptar su destino como rey.', 1994, '1994-06-24', 88, 'Estados Unidos', 'Ingles', '7', 45000000, 968000000, 8.5, 3100, 37000, 1, 1, 1, 'lion_king.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('Toy Story', 'Toy Story', 'John Lasseter', 'Animacion', 'Los juguetes cobran vida cuando los humanos no estan.', 1995, '1995-11-22', 81, 'Estados Unidos', 'Ingles', '7', 30000000, 394000000, 8.3, 1800, 18000, 1, 1, 0, 'toy_story.jpg', 'https://youtube.com', 2.49, 8.99, 'HD', 2),

('Finding Nemo', 'Finding Nemo', 'Andrew Stanton', 'Animacion', 'Un pez busca desesperadamente a su hijo perdido.', 2003, '2003-05-30', 100, 'Estados Unidos', 'Ingles', '7', 94000000, 941000000, 8.2, 1700, 26000, 1, 0, 0, 'nemo.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('Up', 'Up', 'Pete Docter', 'Animacion', 'Un anciano viaja a Sudamerica en una casa con globos.', 2009, '2009-05-29', 96, 'Estados Unidos', 'Ingles', '7', 175000000, 735000000, 8.3, 2000, 21000, 1, 1, 1, 'up.jpg', 'https://youtube.com', 2.99, 9.99, '4K', 2),

('Frozen', 'Frozen', 'Chris Buck', 'Animacion', 'Dos hermanas enfrentan los poderes del hielo.', 2013, '2013-11-27', 102, 'Estados Unidos', 'Ingles', '7', 150000000, 1290000000, 7.4, 2400, 33000, 1, 0, 1, 'frozen.jpg', 'https://youtube.com', 3.49, 10.99, '4K', 3),

('Interstellar', 'Interstellar', 'Christopher Nolan', 'Ciencia ficcion', 'Un grupo de exploradores viaja por el espacio buscando un nuevo hogar para la humanidad.', 2014, '2014-11-07', 169, 'Estados Unidos', 'Ingles', '12', 165000000, 700000000, 8.7, 1500, 25000, 1, 0, 1, 'interstellar.jpg', 'https://youtube.com', 3.99, 12.99, '4K', 2),

('Dune', 'Dune', 'Denis Villeneuve', 'Ciencia ficcion', 'Un joven heredero viaja a un planeta desertico lleno de peligros.', 2021, '2021-10-22', 155, 'Estados Unidos', 'Ingles', '12', 165000000, 402000000, 8.0, 2100, 19000, 1, 0, 1, 'dune.jpg', 'https://youtube.com', 4.99, 14.99, '4K', 3),

('Oppenheimer', 'Oppenheimer', 'Christopher Nolan', 'Drama', 'La vida del cientifico que desarrollo la bomba atomica.', 2023, '2023-07-21', 180, 'Estados Unidos', 'Ingles', '16', 100000000, 975000000, 8.3, 3200, 29000, 1, 1, 1, 'oppenheimer.jpg', 'https://youtube.com', 5.99, 16.99, '4K', 3),

('Barbie', 'Barbie', 'Greta Gerwig', 'Comedia', 'Barbie descubre el mundo real y comienza a cuestionar su existencia.', 2023, '2023-07-21', 114, 'Estados Unidos', 'Ingles', '7', 145000000, 1446000000, 7.0, 2700, 38000, 1, 0, 1, 'barbie.jpg', 'https://youtube.com', 4.99, 13.99, '4K', 4),

('The Avengers', 'The Avengers', 'Joss Whedon', 'Accion', 'Un equipo de superheroes se une para salvar el planeta.', 2012, '2012-05-04', 143, 'Estados Unidos', 'Ingles', '12', 220000000, 1518000000, 8.0, 3000, 42000, 1, 1, 1, 'avengers.jpg', 'https://youtube.com', 3.99, 12.99, '4K', 3),

('Iron Man', 'Iron Man', 'Jon Favreau', 'Accion', 'Un inventor construye una armadura tecnologica para combatir el mal.', 2008, '2008-05-02', 126, 'Estados Unidos', 'Ingles', '12', 140000000, 585000000, 7.9, 1900, 17000, 1, 1, 0, 'iron_man.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 2),

('Doctor Strange', 'Doctor Strange', 'Scott Derrickson', 'Fantasia', 'Un cirujano descubre las artes misticas.', 2016, '2016-11-04', 115, 'Estados Unidos', 'Ingles', '12', 165000000, 677000000, 7.5, 1600, 22000, 1, 0, 0, 'doctor_strange.jpg', 'https://youtube.com', 3.99, 11.99, '4K', 3),

('Black Panther', 'Black Panther', 'Ryan Coogler', 'Accion', 'Un rey protege su pais y su tecnologia.', 2018, '2018-02-16', 134, 'Estados Unidos', 'Ingles', '12', 200000000, 1350000000, 7.3, 2100, 24000, 1, 1, 1, 'black_panther.jpg', 'https://youtube.com', 3.99, 12.99, '4K', 3),

('Jurassic Park', 'Jurassic Park', 'Steven Spielberg', 'Aventura', 'Un parque tematico con dinosaurios vivos se convierte en un desastre.', 1993, '1993-06-11', 127, 'Estados Unidos', 'Ingles', '12', 63000000, 1046000000, 8.2, 2500, 30000, 1, 1, 0, 'jurassic_park.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('Jaws', 'Jaws', 'Steven Spielberg', 'Suspense', 'Un tiburon aterroriza a los habitantes de una localidad costera.', 1975, '1975-06-20', 124, 'Estados Unidos', 'Ingles', '16', 9000000, 476000000, 8.1, 1700, 12000, 1, 0, 0, 'jaws.jpg', 'https://youtube.com', 2.49, 8.99, 'HD', 2),

('The Godfather', 'The Godfather', 'Francis Ford Coppola', 'Drama', 'Una familia mafiosa lucha por mantener su poder.', 1972, '1972-03-24', 175, 'Estados Unidos', 'Ingles', '18', 6000000, 250000000, 9.2, 4500, 20000, 1, 1, 1, 'godfather.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3),

('Pulp Fiction', 'Pulp Fiction', 'Quentin Tarantino', 'Crimen', 'Varias historias criminales se entrelazan en Los Angeles.', 1994, '1994-10-14', 154, 'Estados Unidos', 'Ingles', '18', 8000000, 213000000, 8.9, 3900, 18000, 1, 0, 1, 'pulp_fiction.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 2),

('Fight Club', 'Fight Club', 'David Fincher', 'Drama', 'Un hombre crea un club clandestino de lucha.', 1999, '1999-10-15', 139, 'Estados Unidos', 'Ingles', '18', 63000000, 101000000, 8.8, 3600, 16000, 1, 1, 0, 'fight_club.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 2),

('Se7en', 'Seven', 'David Fincher', 'Suspense', 'Dos detectives investigan una serie de asesinatos.', 1995, '1995-09-22', 127, 'Estados Unidos', 'Ingles', '18', 33000000, 327000000, 8.6, 2400, 14000, 1, 0, 0, 'seven.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('The Shawshank Redemption', 'The Shawshank Redemption', 'Frank Darabont', 'Drama', 'Un banquero condenado injustamente busca recuperar su libertad.', 1994, '1994-09-23', 142, 'Estados Unidos', 'Ingles', '16', 25000000, 73000000, 9.3, 5000, 26000, 1, 1, 1, 'shawshank.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('Whiplash', 'Whiplash', 'Damien Chazelle', 'Drama', 'Un joven baterista busca alcanzar la perfeccion musical.', 2014, '2014-10-10', 107, 'Estados Unidos', 'Ingles', '16', 3300000, 49000000, 8.5, 1900, 11000, 1, 0, 1, 'whiplash.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('La La Land', 'La La Land', 'Damien Chazelle', 'Musical', 'Dos artistas persiguen sus sueños en Los Angeles.', 2016, '2016-12-09', 128, 'Estados Unidos', 'Ingles', '7', 30000000, 472000000, 8.0, 2300, 21000, 1, 1, 1, 'la_la_land.jpg', 'https://youtube.com', 3.49, 10.99, '4K', 3),

('The Grand Budapest Hotel', 'The Grand Budapest Hotel', 'Wes Anderson', 'Comedia', 'Un conserje y su aprendiz viven una aventura en un hotel europeo.', 2014, '2014-03-28', 99, 'Estados Unidos', 'Ingles', '12', 25000000, 174000000, 8.1, 1500, 9000, 1, 0, 0, 'grand_budapest.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('Amelie', 'Le Fabuleux Destin d Amelie Poulain', 'Jean-Pierre Jeunet', 'Romance', 'Una joven decide mejorar la vida de las personas que la rodean.', 2001, '2001-04-25', 122, 'Francia', 'Frances', '12', 10000000, 174000000, 8.3, 1700, 10000, 1, 1, 1, 'amelie.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 4),

('Life Is Beautiful', 'La vita e bella', 'Roberto Benigni', 'Drama', 'Un padre utiliza su imaginacion para proteger a su hijo durante la guerra.', 1997, '1997-12-20', 116, 'Italia', 'Italiano', '12', 20000000, 230000000, 8.6, 2200, 13000, 1, 1, 1, 'life_is_beautiful.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('Spirited Away', 'Sen to Chihiro no Kamikakushi', 'Hayao Miyazaki', 'Animacion', 'Una niña entra en un mundo magico de espiritus.', 2001, '2001-07-20', 125, 'Japon', 'Japones', '7', 19000000, 395000000, 8.6, 2400, 16000, 1, 0, 1, 'spirited_away.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 4),

('Your Name', 'Kimi no Na wa', 'Makoto Shinkai', 'Romance', 'Dos jovenes intercambian sus cuerpos misteriosamente.', 2016, '2016-08-26', 106, 'Japon', 'Japones', '7', 7500000, 382000000, 8.4, 2000, 17000, 1, 1, 1, 'your_name.jpg', 'https://youtube.com', 2.99, 9.99, '4K', 4),

('Train to Busan', 'Busanhaeng', 'Yeon Sang-ho', 'Terror', 'Un grupo de pasajeros intenta sobrevivir a una epidemia zombie.', 2016, '2016-07-20', 118, 'Corea del Sur', 'Coreano', '16', 8500000, 98000000, 7.6, 1300, 12000, 1, 0, 0, 'train_to_busan.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3),

('The Conjuring', 'The Conjuring', 'James Wan', 'Terror', 'Una familia experimenta sucesos paranormales en su casa.', 2013, '2013-07-19', 112, 'Estados Unidos', 'Ingles', '16', 20000000, 319000000, 7.5, 1400, 15000, 1, 1, 0, 'conjuring.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3),

('Get Out', 'Get Out', 'Jordan Peele', 'Terror', 'Un joven descubre secretos inquietantes durante una visita familiar.', 2017, '2017-02-24', 104, 'Estados Unidos', 'Ingles', '16', 4500000, 255000000, 7.8, 1800, 14000, 1, 0, 1, 'get_out.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3),

('A Quiet Place', 'A Quiet Place', 'John Krasinski', 'Terror', 'Una familia debe vivir en silencio para sobrevivir.', 2018, '2018-04-06', 90, 'Estados Unidos', 'Ingles', '16', 17000000, 341000000, 7.5, 1200, 13000, 1, 1, 0, 'quiet_place.jpg', 'https://youtube.com', 3.49, 10.99, '4K', 2),

('Deadpool', 'Deadpool', 'Tim Miller', 'Comedia', 'Un mercenario adquiere poderes de regeneracion y busca venganza.', 2016, '2016-02-12', 108, 'Estados Unidos', 'Ingles', '18', 58000000, 783000000, 8.0, 2300, 25000, 1, 0, 1, 'deadpool.jpg', 'https://youtube.com', 3.99, 11.99, '4K', 3),

('Mad Max Fury Road', 'Mad Max Fury Road', 'George Miller', 'Accion', 'Un grupo de supervivientes atraviesa un desierto postapocaliptico.', 2015, '2015-05-15', 120, 'Australia', 'Ingles', '16', 150000000, 380000000, 8.1, 1900, 17000, 1, 1, 1, 'mad_max.jpg', 'https://youtube.com', 3.99, 11.99, '4K', 3),

('The Wolf of Wall Street', 'The Wolf of Wall Street', 'Martin Scorsese', 'Comedia', 'Un corredor de bolsa alcanza el exito mediante practicas fraudulentas.', 2013, '2013-12-25', 180, 'Estados Unidos', 'Ingles', '18', 100000000, 392000000, 8.2, 2500, 21000, 1, 0, 0, 'wolf_wall_street.jpg', 'https://youtube.com', 3.99, 11.99, 'HD', 3),

('Shrek', 'Shrek', 'Andrew Adamson', 'Animacion', 'Un ogro emprende una aventura para recuperar su pantano.', 2001, '2001-05-18', 90, 'Estados Unidos', 'Ingles', '7', 60000000, 488000000, 7.9, 1900, 35000, 1, 1, 1, 'shrek.jpg', 'https://youtube.com', 2.49, 8.99, 'HD', 2),

('Inside Out', 'Inside Out', 'Pete Docter', 'Animacion', 'Las emociones de una niña intentan adaptarse a una nueva ciudad.', 2015, '2015-06-19', 95, 'Estados Unidos', 'Ingles', '7', 175000000, 858000000, 8.1, 2000, 27000, 1, 1, 1, 'inside_out.jpg', 'https://youtube.com', 2.99, 9.99, '4K', 3),

('The Incredibles', 'The Incredibles', 'Brad Bird', 'Animacion', 'Una familia de superheroes intenta llevar una vida normal.', 2004, '2004-11-05', 115, 'Estados Unidos', 'Ingles', '7', 92000000, 631000000, 8.0, 1700, 20000, 1, 0, 0, 'incredibles.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('The Truman Show', 'The Truman Show', 'Peter Weir', 'Drama', 'Un hombre descubre que toda su vida podria ser un programa de television.', 1998, '1998-06-05', 103, 'Estados Unidos', 'Ingles', '7', 60000000, 264000000, 8.2, 2100, 16000, 1, 1, 1, 'truman_show.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('Cast Away', 'Cast Away', 'Robert Zemeckis', 'Aventura', 'Un hombre lucha por sobrevivir solo en una isla desierta.', 2000, '2000-12-22', 143, 'Estados Unidos', 'Ingles', '12', 90000000, 429000000, 7.8, 1500, 13000, 1, 0, 0, 'cast_away.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 2),

('The Notebook', 'The Notebook', 'Nick Cassavetes', 'Romance', 'Dos jovenes enamorados luchan por permanecer juntos.', 2004, '2004-06-25', 123, 'Estados Unidos', 'Ingles', '12', 29000000, 118000000, 7.8, 1800, 22000, 1, 1, 1, 'notebook.jpg', 'https://youtube.com', 2.99, 9.99, 'HD', 3),

('The Social Network', 'The Social Network', 'David Fincher', 'Drama', 'La creacion de una de las redes sociales mas conocidas del mundo.', 2010, '2010-10-01', 120, 'Estados Unidos', 'Ingles', '12', 40000000, 224000000, 7.8, 1600, 10000, 1, 0, 0, 'social_network.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3),

('Cinderella', 'Cinderella', 'Clyde Geronimi', 'Fantasia', 'Una joven encuentra una oportunidad para cambiar su destino.', 1950, '1950-02-15', 74, 'Estados Unidos', 'Ingles', '7', 2900000, 263000000, 7.3, 1200, 14000, 1, 1, 0, 'cinderella.jpg', 'https://youtube.com', 2.49, 8.99, 'HD', 2),

('The Hunger Games', 'The Hunger Games', 'Gary Ross', 'Ciencia ficcion', 'Una joven participa en una competencia mortal televisada.', 2012, '2012-03-23', 142, 'Estados Unidos', 'Ingles', '12', 78000000, 695000000, 7.2, 1900, 23000, 1, 0, 1, 'hunger_games.jpg', 'https://youtube.com', 3.49, 10.99, 'HD', 3);
