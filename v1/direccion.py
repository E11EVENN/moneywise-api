from flask import Blueprint, jsonify
from models import Direccion

direccion_v1_bp = Blueprint('direccion_v1', __name__, url_prefix='/v1/direccion')

@direccion_v1_bp.route('/', methods=['GET'])
def obtener_direcciones():
    direcciones = Direccion.query.all()
    resultado = [{
        'barrio': direccion.barrio,
        'ciudad': direccion.ciudad,
        'direccion': direccion.direccion
    } for direccion in direcciones]
    return jsonify(resultado)

@direccion_v1_bp.route('/<string:barrio>', methods=['GET'])
def obtener_direccion(barrio):
    direccion = Direccion.query.get(barrio)
    if not direccion:
        return jsonify({'mensaje': 'Dirección no encontrada'}), 404

    resultado = {
        'barrio': direccion.barrio,
        'ciudad': direccion.ciudad,
        'direccion': direccion.direccion
    }
    return jsonify(resultado)
