# TFM: Aplicación web interactiva
Aplicación web interactiva para el proyecto de final de máster: "Aplicación de técnicas de Clustering para la segmentación de masas mamográficas”. El código y la memoria del proyecte pede encontrarse en el repositorio: https://github.com/DemetrioMunoz/GitR
## Descripción
'app.py' es un script de aplicación web Flask que utiliza modelos de aprendizaje automático (KMeans y UMAP) para realizar predicciones en base a datos ingresados por el usuario, codificando variables categóricas y aplicando transformaciones antes de la predicción.
## Funcionamiento
La aplicación permite a los usuarios introducir características tumorales mediante un formulario web. Estas características se utilizan como entrada para los modelos de agrupamiento previamente entrenados. Como resultado, las observaciones se agrupan en el grupo correspondiente, determinando su riesgo de malignidad.

Debido a las limitaciones de los recursos de los servicios de alojamiento web gratuitos, el tiempo de procesamiento de la aplicación web está restringido.
## Prepocesamiento y modelos 
La aplicación no reentrena los modelos con los nuevos datos. En su lugar, utiliza modelos previamente entrenados y guardados en archivos pickle ('kmeans_model.pkl', 'umap_model.pkl', 'ohe.pkl').

Los archivos pickle fueron obtenidos del código en "web_test.ipynb", donde se implementó el modelo y los respectivos preprocesamientos.
## Esctructura 
- 'app.py': Script principal que define la aplicación Flask, las rutas y la lógica para procesar las solicitudes de los usuarios.
- 'kmeans_model.pkl': Modelo K-means. 
- 'umap_model.pkl': Modelo de reduccion de dimensiones UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction)
- 'ohe.pkl': Codificador One-Hot Encoder para las variables categoricas. 
- 'templates/': Carpeta que contiene los archivos HTML utilizados para renderizar las diferentes vistas de la aplicación (index.html, result.html, model_result.html).
- 'static/images: Carpeta que contiene los archivos PNG de los resultados del modelo K-means.
- 'web_tes': Archivo Jupyter Notebook que contiene la implementacion del modelo K-means y las diferentes técnicas de preprocesamiento. Además de obtener guardar los modelo en los archivos pickle.
- 'requeriments.txt': Archivo que contiene todas las versiones de los modulos de python utilizados.
- 'README': Guía detallada sobre la estructura, el propósito y el funcionamiento del proyecto. 
## Despliege
La aplicación web interactiva ha sido desplegada utilizando el servicio de alojamiento 'render': https://render.com/.
## Autor
Nombre: Demtrio Muñoz Álvarez
GitHub: https://github.com/DemetrioMunoz
