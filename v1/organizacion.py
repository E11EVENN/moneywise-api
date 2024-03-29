from flask import Blueprint, jsonify
from models import Organizacion

organizacion_v1_bp = Blueprint('organizacion_v1', __name__, url_prefix='/v1/organizacion')

@organizacion_v1_bp.route('/', methods=['GET'])
def obtener_organizaciones():
    organizaciones = Organizacion.query.all()
    resultado = [{
        'id_organizacion': organizacion.id_organizacion,
        'nombre': organizacion.nombre
    } for organizacion in organizaciones]
    return jsonify(resultado)

@organizacion_v1_bp.route('/<int:id_organizacion>', methods=['GET'])
def obtener_organizacion(id_organizacion):
    organizacion = Organizacion.query.get(id_organizacion)
    if not organizacion:
        return jsonify({'mensaje': 'Organización no encontrada'}), 404

    resultado = {
        'id_organizacion': organizacion.id_organizacion,
        'nombre': organizacion.nombre
    }
    return jsonify(resultado)
