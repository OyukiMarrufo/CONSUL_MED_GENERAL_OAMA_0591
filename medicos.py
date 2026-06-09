from flask import Blueprint, request, render_template, redirect, url_for
from database import db

medicos_bp = Blueprint('medicos', __name__)

# RUTA GET: Para mostrar el formulario visual (medicos.html)
@medicos_bp.route('/', methods=['GET'])
def vista_medicos():
    return render_template('medicos.html')

# RUTA POST: Para recibir los datos del formulario e insertarlos en MongoDB
@medicos_bp.route('/registrar', methods=['POST'])
def registrar_medico():
    coleccion = db['medicos']
    
    datos = {
        "nombre_medico": request.form.get('nombre_medico'),
        "cedula_profesional": request.form.get('cedula_profesional'),
        "especialidad": request.form.get('especialidad'),
        "turno": request.form.get('turno'),
        "dias_trabajo": request.form.get('dias_trabajo'),
        "correo_electronico": request.form.get('correo_electronico'),
        "telefono": request.form.get('telefono')
    }
    
    # Insertar en MongoDB
    coleccion.insert_one(datos)
    
    # Redirigir al index para ver los cambios
    return redirect(url_for('index.index'))