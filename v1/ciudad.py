from flask import Blueprint, jsonify
from models import Ciudad

ciudad_v1_bp = Blueprint('ciudad_v1', __name__, url_prefix='/v1/ciudad')

@ciudad_v1_bp.route('/', methods=['GET'])
def obtener_ciudades():
    ciudades = Ciudad.query.all()
    resultado = [
        {
            'id_ciudad': ciudad.id_ciudad,
            'id_departamento': ciudad.id_departamento,  # Asegúrate de que esto coincide con tu modelo
            'nombre': ciudad.nombre,
            'indicativo': ciudad.indicativo,
            'estado': ciudad.estado,  # Asegurándose de que esto coincida con el tipo de columna correcto
            'fecha_registro': ciudad.fecha_registro.isoformat() if ciudad.fecha_registro else None,
            'fecha_actualizacion': ciudad.fecha_actualizacion.isoformat() if ciudad.fecha_actualizacion else None,
        } for ciudad in ciudades
    ]
    return jsonify(resultado)

@ciudad_v1_bp.route('/<int:id_ciudad>', methods=['GET'])  # Asumiendo que id_ciudad es un entero
def obtener_ciudad(id_ciudad):
    ciudad = Ciudad.query.get(id_ciudad)
    if not ciudad:
        return jsonify({'mensaje': 'Ciudad no encontrada'}), 404

    resultado = {
        'id_ciudad': ciudad.id_ciudad,
        'id_departamento': ciudad.id_departamento,  # Asegúrate de que esto coincide con tu modelo
        'nombre': ciudad.nombre,
        'indicativo': ciudad.indicativo,
        'estado': ciudad.estado,  # Asegurándose de que esto coincida con el tipo de columna correcto
        'fecha_registro': ciudad.fecha_registro.isoformat() if ciudad.fecha_registro else None,
        'fecha_actualizacion': ciudad.fecha_actualizacion.isoformat() if ciudad.fecha_actualizacion else None,
    }
    return jsonify(resultado)

