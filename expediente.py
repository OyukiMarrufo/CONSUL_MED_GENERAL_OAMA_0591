# Importamos las herramientas necesarias de Flask para manejar rutas, capturar formularios y redireccionar
from flask import Blueprint, request, render_template, redirect, url_for
# Importamos la conexión centralizada a nuestra base de datos en MongoDB Atlas
from database import db

# Creamos el Blueprint para organizar las rutas de este módulo de forma independiente
expediente_bp = Blueprint('expediente', __name__)

# =========================================================================
# RUTA 1: MOSTRAR EL FORMULARIO (MÉTODO GET)
# Se activa cuando entramos en el navegador a: http://127.0.0.1:5000/expediente/
# =========================================================================
@expediente_bp.route('/', methods=['GET'])
def vista_expediente():
    return render_template('expediente.html')


# =========================================================================
# RUTA 2: GUARDAR LOS DATOS EN LA BASE DE DATOS (MÉTODO POST)
# Se activa cuando el usuario da clic en el botón "Guardar en Expediente"
# =========================================================================
@expediente_bp.route('/registrar', methods=['POST'])
def registrar_expediente():
    coleccion = db['expedientes']
    
    datos = {
        "id_paciente": request.form.get('id_paciente'), # El ID o nombre del paciente
        "signos_vitales": request.form.get('signos_vitales'), # Presión, temperatura, etc.
        "diagnostico": request.form.get('diagnostico'), # El diagnóstico del médico
        "treatment_sugerido": request.form.get('tratamiento_sugerido'), # La receta o tratamiento
        "observaciones_adicionales": request.form.get('observaciones_adicionales') # Notas extra
    }
    
    # insert_one toma el diccionario "datos" y lo guarda como un nuevo documento en MongoDB Atlas
    coleccion.insert_one(datos)
    
    return redirect(url_for('index.index'))