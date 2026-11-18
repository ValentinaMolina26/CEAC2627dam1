sudo mysql -u root -p

CREATE DATABASE blogceacdam2627;

USE blogceacdam2627;

CREATE TABLE articulos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	titulo VARCHAR(255),
	fecha DATE,
	contenido TEXT
);

INSERT INTO articulos (titulo, fecha, contenido) VALUES

(
    'Mi camino en el mundo de la programación',
    '2026-10-26',
    'Actualmente estoy estudiando Desarrollo de Aplicaciones Multiplataforma (DAM), una formación que me permite aprender a crear aplicaciones, trabajar con bases de datos y descubrir nuevas tecnologías.'
),

(
    'Mi proyecto personal: Social Planner',
    '2026-10-25',
    'Social Planner es mi proyecto intermodular, una aplicación pensada para organizar tareas, publicaciones y fechas importantes. Mi objetivo es crear una herramienta práctica que ayude a las personas a gestionar mejor sus actividades.'
),

(
    'La importancia de las redes sociales',
    '2026-10-24',
    'Las redes sociales se han convertido en una parte importante de la comunicación actual. Me interesa aprender cómo utilizarlas para compartir contenido, conectar con otras personas y ayudar a las marcas a llegar a su público.'
),

(
    'Diseño gráfico y creatividad digital',
    '2026-10-23',
    'El diseño gráfico es una de las áreas que más me llaman la atención. Me gusta la posibilidad de combinar colores, imágenes, tipografías y diferentes elementos para crear diseños visualmente atractivos.'
),

(
    'Mi interés por la inteligencia artificial',
    '2026-10-22',
    'La inteligencia artificial está transformando la forma de trabajar y desarrollar nuevas ideas. Quiero aprender a utilizar estas herramientas para mejorar mis habilidades, automatizar tareas y crear proyectos digitales.'
),

(
    'Aprendiendo a programar con Python',
    '2026-10-21',
    'Python es uno de los lenguajes que estoy aprendiendo durante mis estudios. A través de ejercicios y pequeños proyectos, estoy descubriendo cómo funcionan las variables, las condiciones, los bucles y las funciones.'
),

(
    'Mi experiencia aprendiendo HTML y CSS',
    '2026-10-20',
    'HTML y CSS me permiten comenzar a construir páginas web y personalizar su apariencia. Estoy aprendiendo a organizar el contenido, utilizar diferentes estilos y crear diseños que sean claros y agradables para los usuarios.'
),

(
    'La conexión entre programación y marketing',
    '2026-10-19',
    'La programación y el marketing digital pueden complementarse de muchas maneras. Me interesa descubrir cómo desarrollar herramientas que ayuden a las empresas a gestionar sus redes sociales, organizar campañas y mejorar su presencia en Internet.'
),

(
    'Creando contenido con Canva y CapCut',
    '2026-10-18',
    'Herramientas como Canva y CapCut facilitan la creación de diseños, vídeos y publicaciones para redes sociales. Me interesa aprender a utilizarlas mejor para desarrollar contenido creativo y comunicar ideas de forma visual.'
),

(
    'Mis primeros pasos con las bases de datos',
    '2026-10-17',
    'Durante mis estudios estoy aprendiendo a crear y gestionar bases de datos. Comprender cómo almacenar, organizar, consultar y modificar información es fundamental para desarrollar aplicaciones útiles y funcionales.'
),

(
    'Cómo organizo mis ideas para nuevos proyectos',
    '2026-10-16',
    'Antes de comenzar un proyecto, es importante tener claras las ideas y definir qué se quiere conseguir. Organizar las tareas, establecer prioridades y dividir el trabajo en pequeños pasos me ayuda a avanzar de forma más ordenada.'
),

(
    'El diseño de aplicaciones centrado en el usuario',
    '2026-10-15',
    'Una aplicación no solo debe funcionar correctamente, también debe ser fácil de utilizar. Por eso me interesa aprender a diseñar interfaces intuitivas, con una buena organización visual y opciones que permitan a cada usuario encontrar lo que necesita.'
),

(
    'La importancia de aprender inglés en tecnología',
    '2026-10-14',
    'El inglés es una herramienta importante en el mundo de la programación, ya que gran parte de la documentación y los recursos tecnológicos están en este idioma. Mejorar mi nivel me ayudará a comprender mejor los contenidos técnicos y ampliar mis oportunidades profesionales.'
),

(
    'Mi interés por el mundo de la publicidad digital',
    '2026-10-13',
    'La publicidad digital permite a las marcas promocionar sus productos y servicios a través de diferentes plataformas. Me interesa conocer cómo se crean campañas, se identifican públicos y se diseñan contenidos capaces de captar la atención.'
),

(
    'Aprendiendo a trabajar con bases de datos SQL',
    '2026-10-12',
    'SQL permite consultar y gestionar información almacenada en bases de datos. Estoy aprendiendo a utilizar instrucciones para insertar registros, buscar información, actualizar datos y relacionar tablas dentro de una aplicación.'
),

(
    'La creatividad como parte del desarrollo de software',
    '2026-10-11',
    'Programar también requiere creatividad, porque desarrollar una aplicación implica buscar soluciones y transformar ideas en herramientas reales. Me gusta la posibilidad de combinar el pensamiento lógico con el diseño para crear proyectos propios.'
),

(
    'Cómo imagino el futuro de Social Planner',
    '2026-10-10',
    'Me gustaría que Social Planner evolucionara hasta convertirse en una aplicación flexible y fácil de utilizar. En el futuro podría incluir tableros personalizables, calendarios, gestión de publicaciones y organización de tareas para diferentes tipos de usuarios.'
),

(
    'La importancia de la organización en los estudios',
    '2026-10-09',
    'Estudiar programación requiere práctica, constancia y una buena organización del tiempo. Dividir las actividades, repasar los conceptos y practicar con ejemplos me ayuda a comprender mejor los temas y avanzar en mi formación.'
),

(
    'La tecnología como herramienta para emprender',
    '2026-10-08',
    'Las herramientas digitales ofrecen muchas oportunidades para desarrollar ideas y crear nuevos proyectos. Me interesa aprender a combinar programación, diseño y marketing para construir soluciones que puedan ser útiles para personas y empresas.'
),

(
    'Mis objetivos profesionales en el mundo digital',
    '2026-10-07',
    'Mi objetivo es seguir aprendiendo sobre programación, diseño, inteligencia artificial y marketing digital. Quiero desarrollar mis habilidades, crear proyectos propios y descubrir oportunidades profesionales en empresas tecnológicas y del entorno digital.'
);

-- ahora el usuario

CREATE USER 'blogceacdam2627'@'localhost' IDENTIFIED BY 'Blogceac123$';

GRANT USAGE ON *.* TO 'blogceacdam2627'@'localhost';

ALTER USER 'blogceacdam2627'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

GRANT ALL PRIVILEGES ON blogceacdam2627.* 
TO 'blogceacdam2627'@'localhost';

FLUSH PRIVILEGES;
