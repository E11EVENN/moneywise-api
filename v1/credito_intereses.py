from flask import Blueprint, jsonify
from models import CreditoIntereses

credito_intereses_v1_bp = Blueprint('credito_intereses_v1', __name__, url_prefix='/v1/credito-intereses')

@credito_intereses_v1_bp.route('/', methods=['GET'])
def obtener_creditos_intereses():
    creditos_intereses = CreditoIntereses.query.all()
    resultado = [{
        'id_credito_intereses': ci.id_credito_intereses,
        'interes': float(ci.interes),
        'id_credito': ci.id_credito,
        'id_tipo_interes': ci.id_tipo_interes
    } for ci in creditos_intereses]
    return jsonify(resultado)

@credito_intereses_v1_bp.route('/<int:id_credito_intereses>', methods=['GET'])
def obtener_credito_interes(id_credito_intereses):
    credito_interes = CreditoIntereses.query.get(id_credito_intereses)
    if not credito_interes:
        return jsonify({'mensaje': 'Crédito interés no encontrado'}), 404

    resultado = {
        'id_credito_intereses': credito_interes.id_credito_intereses,
        'interes': float(credito_interes.interes),
        'id_credito': credito_interes.id_credito,
        'id_tipo_interes': credito_interes.id_tipo_interes
    }
    return jsonify(resultado)
