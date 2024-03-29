from flask import Blueprint, jsonify
from models import CreditoPazSalvo

credito_paz_salvo_v1_bp = Blueprint('credito_paz_salvo_v1', __name__, url_prefix='/v1/credito_paz_salvo')

@credito_paz_salvo_v1_bp.route('/', methods=['GET'])
def obtener_creditos_paz_salvo():
    paz_salvos = CreditoPazSalvo.query.all()
    resultado = [{
        'id_credito_paz_salvo': paz_salvo.id_credito_paz_salvo,
        'id_credito': paz_salvo.id_credito,
        'fecha_paz_salvo': paz_salvo.fecha_paz_salvo.isoformat() if paz_salvo.fecha_paz_salvo else None
    } for paz_salvo in paz_salvos]
    return jsonify(resultado)

@credito_paz_salvo_v1_bp.route('/<int:id_credito_paz_salvo>', methods=['GET'])
def obtener_credito_paz_salvo(id_credito_paz_salvo):
    paz_salvo = CreditoPazSalvo.query.get(id_credito_paz_salvo)
    if not paz_salvo:
        return jsonify({'mensaje': 'Paz Salvo no encontrado'}), 404

    resultado = {
        'id_credito_paz_salvo': paz_salvo.id_credito_paz_salvo,
        'id_credito': paz_salvo.id_credito,
        'fecha_paz_salvo': paz_salvo.fecha_paz_salvo.isoformat() if paz_salvo.fecha_paz_salvo else None
    }
    return jsonify(resultado)
