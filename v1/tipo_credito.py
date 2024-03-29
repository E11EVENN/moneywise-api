from flask import Blueprint, jsonify
from models import TipoCredito

tipo_credito_v1_bp = Blueprint('tipo_credito_v1', __name__, url_prefix='/v1/tipo_credito')

@tipo_credito_v1_bp.route('/', methods=['GET'])
def obtener_tipos_credito():
    tipos_credito = TipoCredito.query.all()
    resultado = [
        {
            'id_tipo_credito': tipo_credito.id_tipo_credito,
            'descripcion': tipo_credito.descripcion
        } for tipo_credito in tipos_credito
    ]
    return jsonify(resultado)

@tipo_credito_v1_bp.route('/<string:id_tipo_credito>', methods=['GET'])
def obtener_tipo_credito(id_tipo_credito):
    tipo_credito = TipoCredito.query.get(id_tipo_credito)
    if not tipo_credito:
        return jsonify({'mensaje': 'Tipo de crédito no encontrado'}), 404

    resultado = {
        'id_tipo_credito': tipo_credito.id_tipo_credito,
        'descripcion': tipo_credito.descripcion
    }
    return jsonify(resultado)
