1.-Ya tenemos el simulacro de bases de datos
Al acabar el simulacro de bases de datos ya podemos empezar el de programación
porque el de programación depende de la base de datos

2.-Ahora lo que tenemos que hacer es:
a) Creamos un controlador Python
b) El controlador python importa el conector MySQL/SQLite/import json
c) Os aseguráis de que realmente se conecta a la base de datos antes de dar ningun paso mas
d) Añadis flask a la fiesta
e) Saquéis la información por pantalla html (información cruda y sucia) - si ya tenéis eso, ya tenéis el camino de vuelta. Recordad que esto se puede hacer de dos modos
	- El modo fácil, con Jinja y templates
  - El modo no tan fácil, que es crear 2 endpoints
  	- Uno sirve JSON
    - Y el otro consume JSON a través de Javascript fetch
    
f) En el camino de ida:
	- Creáis un formulario en un template HTML (crudo, sucio), y method POST y action
  - Creáis un segundo endpoint /insertar que recibe la información y la INSERT en la base de datos
  
g) El examen acaba cuando demostréis camino de ida (desde el formulario hasta la base de datos) y camino de vuelta (desde la base de datos hasta HTML (table/grid)

Reglas:
1.-Id incremental, id guardando archivos, en cada archivo id avanzando poco a poco
2.-Podéis usar vuestro apuntes, no podéis usar ni internet ni IA
3.-No podéis usar mis apuntes
4.-Una vez que hayáis acabado el ejercicio si queréis podéis usar IA para mejorarlo (mejorarlo, no corregirlo)
5.-Se admite IA en el caso de problemas con indentaciones en Python
6.-Para la realización del examen es imprescindible entrar en supervision.jocarsa.com (mismo enlace que os pasé ayer)






