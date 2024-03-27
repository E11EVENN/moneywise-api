from flask import Blueprint, jsonify
from models import Ciudad

ciudad_v1_bp = Blueprint('ciudad_v1', __name__, url_prefix='/v1/ciudad')

@ciudad_v1_bp.route('/', methods=['GET'])
def obtener_ciudades():
    ciudades = Ciudad.query.all()
    resultado = [{
        'id_ciudad': ciudad.id_ciudad,
        'id_departamento': ciudad.id_ciudad,
        'nombre': ciudad.nombre,
        'indicativo': ciudad.indicativo,
        'estado': int(ciudad.estado),
        'fecha_registro': ciudad.fecha_registro.isoformat(),
        'fecha_actulizacion': ciudad.fecha_actulizacion.isoformat(),
        
    } for ciudad in ciudades]
    return jsonify(resultado)

@ciudad_v1_bp.route('/<id_ciudad>', methods=['GET'])
def obtener_ciudad(id_ciudad):
    ciudad = ciudad.query.get(id_ciudad)
    if not ciudad:
        return jsonify({'mensaje': 'Ciudad no encontrado'}), 404

    resultado = {
        'id_ciudad': ciudad.id_ciudad,
        'id_departamento': ciudad.id_ciudad,
        'nombre': ciudad.nombre,
        'indicativo': ciudad.indicativo,
        'estado': int(ciudad.estado),
        'fecha_registro': ciudad.fecha_registro.isoformat(),
        'fecha_actulizacion': ciudad.fecha_actulizacion.isoformat(),
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
