from flask import Blueprint, request, render_template, redirect, url_for
from database import db

pacientes_bp = Blueprint('pacientes', __name__)

# RUTA GET: Para mostrar el formulario visual (pacientes.html)
@pacientes_bp.route('/', methods=['GET'])
def vista_pacientes():
    return render_template('pacientes.html')

# RUTA POST: Para recibir los datos del formulario e insertarlos en MongoDB
@pacientes_bp.route('/registrar', methods=['POST'])
def registrar_paciente():
    coleccion = db['pacientes']
    
    datos = {
        "nombre": request.form.get('nombre'),
        "nacimiento": request.form.get('nacimiento'),
        "genero": request.form.get('genero'),
        "telefono": request.form.get('telefono'),
        "tipo_sangre": request.form.get('tipo_sangre'),
        "curp": request.form.get('curp'),
        "domicilio": request.form.get('domicilio'),
        "correo": request.form.get('correo'),
        "contacto_emergencia": request.form.get('contacto_emergencia')
    }
    
    # Insertar en MongoDB
    coleccion.insert_one(datos)
    
    # Redirigir automáticamente al index para ver la tabla actualizada
    return redirect(url_for('index.index'))