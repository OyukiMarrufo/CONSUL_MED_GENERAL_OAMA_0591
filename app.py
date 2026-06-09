#Aquí vamos a importar Flask, igual se instala desde pip y la terminal. 
from flask import Flask
#Desde nuestro otro archivo, Database, vamos a importar el nombre de nuestra base de datos. 
from database import db

app = Flask(__name__)

#Vamos a crear una carpeta llamada "routes" donde vamos a almacenar los documentos.py de cada una de nuestras colecciones.
from routes.index import index_bp
from routes.pacientes import pacientes_bp
from routes.medicos import medicos_bp
from routes.expediente import expediente_bp

#Y vamos a registrarlas dentro del app que nos crea Flask. 
app.register_blueprint(index_bp)
app.register_blueprint(pacientes_bp, url_prefix='/pacientes')
app.register_blueprint(medicos_bp, url_prefix='/medicos')
app.register_blueprint(expediente_bp, url_prefix='/expediente')

if __name__ == "__main__":
    app.run(debug=True)