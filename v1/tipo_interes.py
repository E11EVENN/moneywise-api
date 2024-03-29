from flask import Blueprint, jsonify
from models import TipoInteres

tipo_interes_v1_bp = Blueprint('tipo_interes_v1', __name__, url_prefix='/v1/tipo_interes')

@tipo_interes_v1_bp.route('/', methods=['GET'])
def obtener_tipos_interes():
    tipos_interes = TipoInteres.query.all()
    resultado = [{
        'id_tipo_interes': tipo_interes.id_tipo_interes,
        'descripcion': tipo_interes.descripcion
    } for tipo_interes in tipos_interes]
    return jsonify(resultado)

@tipo_interes_v1_bp.route('/<int:id_tipo_interes>', methods=['GET'])
def obtener_tipo_interes(id_tipo_interes):
    tipo_interes = TipoInteres.query.get(id_tipo_interes)
    if not tipo_interes:
        return jsonify({'mensaje': 'Tipo de Interés no encontrado'}), 404

    resultado = {
        'id_tipo_interes': tipo_interes.id_tipo_interes,
        'descripcion': tipo_interes.descripcion
    }
    return jsonify(resultado)
