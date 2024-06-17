# TFM: Aplicación web interactiva
Aplicación web interactiva para el proyecto de final de máster: "Aplicación de técnicas de Clustering para la segmentación de masas mamográficas”. El código y la memoria del proyecte pede encontrarse en el repositorio: https://github.com/DemetrioMunoz/GitR
## Descripción
'app.py' es un script de aplicación web Flask que utiliza modelos de aprendizaje automático (KMeans y UMAP) para realizar predicciones en base a datos ingresados por el usuario, codificando variables categóricas y aplicando transformaciones antes de la predicción.
## Funcionamiento
La aplicación permite a los usuarios introducir características tumorales mediante un formulario web. Estas características se utilizan como entrada para los modelos de agrupamiento previamente entrenados. Como resultado, las observaciones se agrupan en el grupo correspondiente, determinando su riesgo de malignidad.
## Prepocesamiento y modelos 
La aplicación no vuelve a entrenar los modelos con los nuevos datos. En su lugar, utiliza los modelos ya entrenados y guardados en archivos pickle (kmeans_model.pkl, umap_model.pkl, ohe.pkl). 
Los archivos pickle se han obteniado de código "web_test" donde se a implementado el modelo y los correspondientes preprocesamientos.
## Esctructura 
-  'app.py': Script principal que define la aplicación Flask, las rutas y la lógica para procesar las solicitudes de los usuarios.
