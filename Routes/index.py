from flask import Flask, request, jsonify, redirect, flash


# Importar la librería de la libreria flask_mysqldb el modulo MySQL 
# para permitir la conexión de una aplicación Flask a una base de datos MySQL.
from flask_mysqldb import MySQL


# Importamos las funciones de tiempo
import time as tm




# Instanciamos Flask
app = Flask(__name__)

@app.route("/")
def index():
    # flash('¡Redireccionando...!',"message")
    # tm.sleep(20)

    # Con redirect podemos redireccionar la petición HTTP a una ruta definida.
    return redirect("http://127.0.0.1:5501/Flask/Views/index.html")

# Levantamos y escuchamos el servidor en modo de depuracion, en el puerto 8080.
if __name__ == '__main__':
    app.run(debug=True, port=8080)