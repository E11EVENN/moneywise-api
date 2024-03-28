from flask import Blueprint, jsonify
from models import Depto



depto_v1_bp = Blueprint('depto_v1', __name__, url_prefix='/v1/depto')

@depto_v1_bp.route('/', methods=['GET'])
def obtener_deptos():
    deptos = Depto.query.all()
    resultado = [{
        'id_departamento': depto.id_departamento,
        'id_pais': depto.id_pais,
        'nombre': depto.nombre,
        'indicativo': depto.indicativo,
        'estado': depto.estado,
        'fecha_registro': depto.fecha_registro.isoformat() if depto.fecha_registro else None,
        'fecha_actualizacion': depto.fecha_actualizacion.isoformat() if depto.fecha_actualizacion else None,
        'id_usuario': depto.id_usuario,
        'ip_address': depto.ip_address
    } for depto in deptos]
    return jsonify(resultado)

@depto_v1_bp.route('/<string:id_departamento>', methods=['GET'])
def obtener_depto(id_departamento):
    depto = Depto.query.get(id_departamento)
    if not depto:
        return jsonify({'mensaje': 'Departamento no encontrado'}), 404

    resultado = {
        'id_departamento': depto.id_departamento,
        'id_pais': depto.id_pais,
        'nombre': depto.nombre,
        'indicativo': depto.indicativo,
        'estado': depto.estado,
        'fecha_registro': depto.fecha_registro.isoformat() if depto.fecha_registro else None,
        'fecha_actualizacion': depto.fecha_actualizacion.isoformat() if depto.fecha_actualizacion else None,
        'id_usuario': depto.id_usuario,
        'ip_address': depto.ip_address
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para operaciones CRUD en departamentos
