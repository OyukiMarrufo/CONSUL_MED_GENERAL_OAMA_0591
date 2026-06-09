# Importamos Blueprint para crear este módulo y render_template para poder dibujar el HTML en pantalla
from flask import Blueprint, render_template
# Importamos la conexión a tu base de datos desde el archivo database.py
from database import db

# Creamos el Blueprint llamado 'index'. Sirve para agrupar las rutas principales de la aplicación.
index_bp = Blueprint('index', __name__)

# =========================================================================
# RUTA PRINCIPAL (RAÍZ): Muestra la pantalla de inicio
# Se activa cuando entras en el navegador a: http://127.0.0.1:5000/
# =========================================================================
@index_bp.route('/')
def index():
    
    # 1. Trae todos los pacientes registrados de la colección 'pacientes'
    lista_pacientes = list(db['pacientes'].find())
    
    # 2. Trae todo el personal médico de la colección 'medicos'
    lista_medicos = list(db['medicos'].find())
    
    # 3. Trae todo el historial de consultas de la colección 'expedientes'
    lista_expedientes = list(db['expedientes'].find())
    
    return render_template(
    'index.html', 
    pacientes=lista_pacientes, 
    medicos=lista_medicos, 
    expedientes=lista_expedientes
    )