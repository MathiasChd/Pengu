from pickle import PUT
from unicodedata import name
from webbrowser import get
from flask import Flask, escape, request, render_template, url_for 



app = Flask(__name__)

@app.route('/')
def home():
   return '¡Hola Mundo!'

@app.route('/procesar',methods = ['PUT'])
def procesar_datos():
    request_data = request.get_json()
    validacion = request_data['validacion']
    #Funcion para obtener el equivalente del error
    if validacion == 'can only concatenate str (not "int") to str':
        return 'Intente concatenar (unir) un valor que no sea un str con un int. Str: string cadenas de texto que van entre comillas. Int: numeros enteros'
    elif validacion == 'invalid syntax':
        return 'Intente no utilizar palabras clave de Python como nombres de variables. Las palabras claves son las palabras predefinidas que no pueden ser utilizadas para nombrar cualquier variable, función, clase, etc.'
    elif validacion == 'unexpected EOF while parsing':
        return 'Hay un error en la estructura o sintaxis de su código.'
    elif validacion == "SyntaxError: unmatched ')'":
        return 'Este error es porque su codigo cuenta con un parentesis faltante de cierre.'
    elif validacion == 'NameError: name "xxxx" is not defined':
        return 'Este error es porque se intenta imprimir una variable que no esta definida. '
    elif validacion == "SyntaxError: can't assign to function call":
        return 'Asegúrese de utilizar la sintaxis correcta para declarar una variable. El nombre de la variable viene primero, seguido de un signo igual, seguido del valor que desea asignar a la variable.'
    elif validacion == "SyntaxError: can't assign to literal":
        return 'Asegúrese de que los nombres de sus variables sean nombres en lugar de valores.'
    elif validacion == 'IndentationError: unexpected indent':
        return 'Uso incorrecto de la sangría. Recuerde que el aumento en la sangría solo se usa después de que la declaración termina con:, y luego debe volver al formato de sangría anterior.'
    elif validacion == 'SyntaxError: EOL while scanning string literal':
        return 'Olvidar agregar comillas al principio y al final de la cadena.'
    elif validacion == "AttributeError: 'str' object has no attribute 'lowerr":
        return 'El nombre del método está mal escrito.'
    elif validacion == 'IndexError: list index out of range':
        return 'La referencia excede el índice máximo de la lista.'
    else:
        return 'Error no encontrado'


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True)
