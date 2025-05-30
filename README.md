# Practica Final Gestión de Sistemas Distribuidos
##  Procesamiento de datos con pyspark 
#### Desarollado por Izzy D., Elizabeth Johana y David Martinez

---

Este proyecto utliza spark para la carga, análisis y utilización de datos de consumo de energía. Los datos provienen de [Junil Patel en Kaggle](https://www.kaggle.com/datasets/ajinilpatel/energy-consumption-prediction/data). El proyecto esta dividido en tres partes:

1. Análisis exploratorio de los datos.
2. Entrenamiento de dos modelos predictivos con los datos.
3. Simulación de lectura de datos en streaming con pyspark y kafka.

---

# Ejecutando el proyecto
Este proyecto utiliza python 3.10.16 y las versiones de las dependencias compatibles con esta versión. Las dependencias se pueden instalar creando un entorno conda usando el archivo `environment.yml`.

## Dependencias

* kafka-python 2.2.10
* matplotlib 3.10.0
* numpy 1.26.4
* pandas 2.2.3
* pyspark 3.5.4
* seaborn 0.13.2

El notebook `parte1_exploracion.ipynb` contiene la primera parte de el proyecto, en la cual realizamos un análisis exploratorio de los datos. Este incluye una mirada a la distribucón de las variables numericas, la frequencía de las variables categoricas y la correlación entre las variables. 

El notebook `parte2_modelado.ipynb` contiene la segunda parte. En esta entrenamos dos modelos, uno de regresión lineal y otro de random forest regression. Usamos los datos explorados en la parte 1 para predecír el consumo de energía por hogar.

El directorio /parte3_streaming/ contiene la tercera y ultima parte. Esta esta formada por tres archivos. El script `productor_kafka.py` genera un productor de kafka que lee los datos contenidos dentro del fichero `streaming_sample.json` y los transmite en un topic en el puerto 9092. El notebook `consumidor.ipynb` usa el modulo `readStream` para igualmente leer los datos del fichero `streaming_sample.json` y así simular la lectura de datos en tiempo real. En este notebook realizamos transformaciones y agregaciones de los datos en streaming con pyspark.