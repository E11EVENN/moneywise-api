from flask import Blueprint, jsonify
from models import TipoDireccion

tipo_direccion_v1_bp = Blueprint('tipo_direccion_v1', __name__, url_prefix='/v1/tipo_direccion')

@tipo_direccion_v1_bp.route('/', methods=['GET'])
def obtener_tipos_direccion():
    tipos_direccion = TipoDireccion.query.all()
    resultado = [{
        'id_direccion': tipo_dir.id_direccion,
        'pueblo_o_ciudad': tipo_dir.pueblo_o_ciudad
    } for tipo_dir in tipos_direccion]
    return jsonify(resultado)

@tipo_direccion_v1_bp.route('/<string:id_direccion>', methods=['GET'])
def obtener_tipo_direccion(id_direccion):
    tipo_direccion = TipoDireccion.query.get(id_direccion)
    if not tipo_direccion:
        return jsonify({'mensaje': 'Tipo de Dirección no encontrado'}), 404

    resultado = {
        'id_direccion': tipo_direccion.id_direccion,
        'pueblo_o_ciudad': tipo_direccion.pueblo_o_ciudad
    }
    return jsonify(resultado)
