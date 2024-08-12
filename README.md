# Fuga de Cerebros 🧠
## Hera Data
### Proyecto de Análisis de Datos y Experimentación A/B para ABC Corporation

## Descripción del Proyecto
Este proyecto tiene como objetivo principal reducir la rotación de empleados y mejorar la satisfacción en el trabajo dentro de ABC Corporation, una consultora tecnológica especializada en soluciones de inteligencia artificial y aprendizaje automático. A través del análisis de datos y experimentación A/B, se busca identificar los factores que influyen en la satisfacción laboral y en la retención de empleados.
Para el desarrollo de este proyecto hemos aplicado la metodologia Agile , dividiéndose en múltiples iteraciones cortas (sprints), cada una con una duración de 1-2 semanas Aproximadamente. Durante cada sprint, el equipo se centró en completar un conjunto de tareas priorizadas en el backlog del proyecto.
Planificación del Sprint:
Al inicio de cada sprint, se realizó una reunión de planificación donde el equipo y el Product Owner identificaron las tareas más importantes y las estimaron en términos de esfuerzo y tiempo. El equipo comprometió un conjunto de tareas que se completarían durante el sprint.
Desarrollo Iterativo:
El trabajo fue desarrollado de manera incremental, permitiendo al equipo ajustar el rumbo según los comentarios recibidos al final de cada sprint. Las tareas incluían descripción breve de las principales actividades, como análisis de datos, construcción de modelos, visualización de datos, etc.

Revisión y Retrospectiva:
Al final de cada sprint, se llevó a cabo una reunión de revisión para presentar los resultados del sprint a los interesados y recibir feedback. Esto garantizó que el trabajo cumpliera con los requisitos del negocio y permitió realizar ajustes antes de avanzar. Posteriormente, en la retrospectiva, el equipo discutió qué funcionó bien y qué áreas necesitaban mejoras, implementando estos aprendizajes en el siguiente sprint.

Entrega Continua:
Durante todo el proyecto, se priorizó la entrega continua de valor. Cada sprint resultó en una versión funcional del proyecto, que podía ser revisada y probada por los usuarios, asegurando que el producto final se alineara estrechamente con las necesidades del cliente.
Gracias a la flexibilidad de Agile, el equipo pudo adaptarse rápidamente a los cambios en los requisitos y las prioridades del proyecto. Esto resultó en la entrega de  un producto final de calidad , en el que destacan sus resultados.  

## 🚧 Estructura del proyecto

data
datos_empresa_final.csv
datos_empresa_nonulos.csv
datos_empresa_V.1.clean.csv
datos_empresa_V1.1.csv
datos_empresa_V1.csv
datos_empresa.csv
empleados.csv
satisfaccion.csv

img
abandonos_a_b.png
ABtesting.png
Años en la empresa por rotación.png
Edad por rotación.png
genero_civil.png
media_edad_renuncias.png
output.png
porcentaje_abandonos.png
rotacion_años_empresa.png
rotacion_departamento.png
rotacion_empleados.png
rotacion_rol_nivel.png
rotacion_vida_trabajo.png
satisfaccion_genero.png
satisfacción_laboral_años.png

src
Fase5_ETL_soporte_SQL.py
Fase5_ETL_soporte.py
main 
Fase_1.ipynb  
Fase1_EDA.ipnyb
Fase2_limpieza_funciones.ipynb  
Fase2_limpieza.ipynb
Fase2_visualizaciones.ipynb
Fase3_BBDD.ipynb  
Fase4_ABTesting.ipynb 
Documentacion.ipynb
Fase5_ETL.py

Readme.md


⚙ Requisitos

Python  
Jupyter Notebook  
Visual Studio Code  

Tecnologías Utilizadas
Python: Para análisis de datos y desarrollo de funciones ETL.
Pandas: Para manejo y manipulación de datos.
SQL: Para creación e interacción con la base de datos.
Matplotlib/Seaborn: Para visualización de datos.


🛠 Instalación

Instalar Python:

Descargar e instalar Python desde Python.org.  
Asegúrate de marcar la opción para agregar Python a tu PATH durante la instalación.

Instalar Jupyter Notebook:

Abre una terminal o símbolo del sistema y ejecuta el siguiente comando para instalar Jupyter Notebook:  
`pip install notebook`

Instalar Visual Studio Code:

Descargar e instalar Visual Studio Code desde Visual Studio Code.

Instalar Extensiones de Visual Studio Code:

Abre Visual Studio Code.  
Ve a la vista de Extensiones haciendo clic en el ícono cuadrado en la barra lateral o presionando Ctrl+Shift+X.  
Busca e instala las siguientes extensiones:  
- Python (de Microsoft)  
- Jupyter (de Microsoft)  

# Fases en las que se desarrolló el proyecto :

1.Análisis Exploratorio de Datos (EDA): Exploración del conjunto de datos para familiarizarse con ellos y entender su estructura.

Por favor, ejecuta el archivo 1_initial_exploration.ipynb para ver los resultados del análisis. Estos fueron los pasos a seguir:

Identificación de problemas tales como valores nulos, valores atípicos y datos faltantes.
Uso de Pandas para obtener información sobre la estructura de los datos y estadísticas básicas.
Unión de conjuntos de datos.


2.Transformación de Datos: Limpieza y transformación del conjunto de datos.
Por favor, ejecuta el archivo Fase2_limpieza.ipynb y Fase2_visualizacion.ipynb para ver los resultados.
Estos fueron los pasos a seguir:
Limpieza de datos
Normalización y conversión de tipos de datos y la aplicación de reglas empresariales específicas. 
Uso de funciones de Python que se aplicarán a los datos extraídos.




3.Diseño de Base de Datos e Inserción de Datos: Creación de la estructura de la base de datos y carga de los datos iniciales.
Por favor ejecuta el archivo  Fase_3BBDD.ipynb para ver los resultados obtenidos.
Estos fueron los pasos a seguir:
Diseño de la Estructura de la Base de Datos
Creación de la Base de Datos
Inserción de Datos Iniciales
   

![Base de datos ](img/BBDD.png)


4.Experimentación A/B:Prueba de hipótesis relacionada con la satisfacción laboral y la rotación de empleados, analizando los resultados.
Por favor, ejecute el archivo Fase4_ABTesting.ipynb para ver los  resultados. 

   
   ![A/B testing](img/ABtesting.png)




5.Creación de una ETL: Automatización del proceso de extracción, transformación y carga de datos en la base de datos.
Por favor abrir el archivo Fase5_ETL.py para ver los resultados'
Pasos a seguir:
Extracción de Datos
Transformación de Datos
Creación de la Base de Datos
Carga de Datos
 
Conclusiones:📑

ABC Corporation presenta una tasa de rotación del 16%, significativamente inferior al 27% observado en otras empresas del sector. Para entender mejor esta diferencia, segmentamos a los empleados en dos grupos basados en su nivel de satisfacción.
Observamos que roles como "Representantes de ventas" y "Técnico de laboratorio" tienen una rotación significativamente mayor, posiblemente debido a la naturaleza competitiva de estos puestos o las condiciones del mercado laboral. Además, la rotación es más alta en los niveles jerárquicos más bajos, lo que podría reflejar menor satisfacción o limitadas oportunidades de crecimiento en estos niveles. Estos hallazgos subrayan la necesidad de implementar estrategias diferenciadas por rol y nivel jerárquico, para retener talento crítico y reducir la rotación en áreas clave.
Examinamos la tendencia de rotación en función de los años de antigüedad en la empresa. Dos patrones importantes emergen: en primer lugar, existe una alta rotación durante los primeros 0-5 años de empleo, lo que sugiere desafíos en la integración y en la gestión de expectativas iniciales. En segundo lugar, se observan picos significativos en la rotación en torno a los 20 y 40 años de antigüedad, lo que podría estar relacionado con la jubilación anticipada o con una percepción de estancamiento profesional. Estos resultados destacan la importancia de optimizar el proceso de onboarding y de fomentar el desarrollo profesional continuo a lo largo de toda la carrera del empleado en la empresa.

Tecnologías Utilizadas

Python: Para análisis de datos y desarrollo de funciones ETL.

Pandas: Para manejo y manipulación de datos.

SQL: Para creación e interacción con la base de datos.

Matplotlib/Seaborn: Para visualización de datos.

Contacto
Para más información o preguntas sobre el proyecto, contacta al equipo  a traves del repositorio de GitHub.
 GitHub: [laural87](https://github.com/laural87)
 GitHub: [Bea]( https://github.com/BeaDataArtist)
 GitHub :[Bertha_Karolina](https://github.com/910129023)

 Licencia
Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

---

Agradecimientos
Agradecemos a ABC Corporation por confiar en nuestro equipo y brindarnos la oportunidad de contribuir a la mejora de la satisfacción y retención de empleados.

¡Esperamos que este informe sea útil y conduzca a decisiones estratégicas que impulsen el éxito a largo plazo de ABC Corporation!
