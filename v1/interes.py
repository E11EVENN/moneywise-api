from flask import Blueprint, jsonify
from models import Interes

interes_v1_bp = Blueprint('interes_v1', __name__, url_prefix='/v1/interes')

@interes_v1_bp.route('/', methods=['GET'])
def obtener_intereses():
    intereses = Interes.query.all()
    resultado = [{
        'id_interes': interes.id_interes,
        'id_tipo_interes': interes.id_tipo_interes,
        'tasa': float(interes.tasa),
        'descripcion': interes.descripcion
    } for interes in intereses]
    return jsonify(resultado)

@interes_v1_bp.route('/<int:id_interes>', methods=['GET'])
def obtener_interes(id_interes):
    interes = Interes.query.get(id_interes)
    if not interes:
        return jsonify({'mensaje': 'Interés no encontrado'}), 404

    resultado = {
        'id_interes': interes.id_interes,
        'id_tipo_interes': interes.id_tipo_interes,
        'tasa': float(interes.tasa),
        'descripcion': interes.descripcion
    }
    return jsonify(resultado)
