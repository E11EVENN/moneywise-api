from flask import Blueprint, jsonify
from models import Credito

credito_v1_bp = Blueprint('credito_v1', __name__, url_prefix='/v1/credito')

@credito_v1_bp.route('/', methods=['GET'])
def obtener_creditos():
    creditos = Credito.query.all()
    resultado = [{
        'id_credito': credito.id_credito,
        'id_cliente': credito.id_cliente,
        'id_tipo_credito': credito.id_tipo_credito,
        'monto': float(credito.monto),
        'fecha_inicio': credito.fecha_inicio.isoformat() if credito.fecha_inicio else None,
        'estado': credito.estado
    } for credito in creditos]
    return jsonify(resultado)

@credito_v1_bp.route('/<int:id_credito>', methods=['GET'])
def obtener_credito(id_credito):
    credito = Credito.query.get(id_credito)
    if not credito:
        return jsonify({'mensaje': 'Crédito no encontrado'}), 404

    resultado = {
        'id_credito': credito.id_credito,
        'id_cliente': credito.id_cliente,
        'id_tipo_credito': credito.id_tipo_credito,
        'monto': float(credito.monto),
        'fecha_inicio': credito.fecha_inicio.isoformat() if credito.fecha_inicio else None,
        'estado': credito.estado
    }
    return jsonify(resultado)

# Agrega más rutas según sea necesario para crear, actualizar y eliminar créditos.
