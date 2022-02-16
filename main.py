# Importamos las librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from flask import Flask, request
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import RandomOverSampler

#funcion para balancear los datos
def balancear_data(data):
    random_data_generator = RandomOverSampler()
    data_balanceada, data_balanceada['definicion_amigable'] = random_data_generator.fit_resample(data[['definicion_error']],data['definicion_amigable'])
    return data_balanceada

#definir la locacion del dataset
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT-Sp5FOBNtydEtxQqSf-GDGD8skbrocUOXgO-mU-P0yI4hRj4TcVFKzjyNGLskWS9Snfe1i_6bdj8Q/pub?gid=0&single=true&output=csv"

#cargar el dataset 
dataset = pd.read_csv(url)

#balancear los datos
balanced_data = balancear_data(dataset)

#Separamos el dataset en train y test
data_train, data_test, = train_test_split(balanced_data, test_size=0.3, random_state=7)
data_train_x, data_train_y = data_train['definicion_error'], data_train['definicion_amigable']
data_test_x, data_test_y = data_test['definicion_error'], data_test['definicion_amigable']

#vectorizacion de datos
tfidf = TfidfVectorizer(stop_words='english')
vector_train_x = tfidf.fit_transform(data_train_x)
vector_test_x = tfidf.transform(data_test_x)

#generacion de modelo SVM
svc = SVC()
svc.fit(vector_train_x, data_train_y)

def transform_error(validacion):
    resultado  = svc.predict(tfidf.transform([validacion]))
    return resultado

app = Flask(__name__)
@app.route('/procesar',methods = ['PUT'])
def procesar_datos():
    request_data = request.get_json()
    validacion = request_data['validacion']
    resultado_machine_learning = transform_error(validacion)
    return resultado_machine_learning[0]
    
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)