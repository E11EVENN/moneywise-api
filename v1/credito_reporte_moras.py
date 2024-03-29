from flask import Blueprint, jsonify
from models import CreditoReporteMora

credito_reporte_mora_v1_bp = Blueprint('credito_reporte_mora_v1', __name__, url_prefix='/v1/credito_reporte_moras')

@credito_reporte_mora_v1_bp.route('/', methods=['GET'])
def obtener_creditos_reporte_moras():
    reportes_moras = CreditoReporteMora.query.all()
    resultado = [{
        'id_credito_reporte_moras': reporte_mora.id_credito_reporte_moras,
        'id_credito': reporte_mora.id_credito,
        'monto': reporte_mora.monto
    } for reporte_mora in reportes_moras]
    return jsonify(resultado)

@credito_reporte_mora_v1_bp.route('/<int:id_credito_reporte_moras>', methods=['GET'])
def obtener_credito_reporte_mora(id_credito_reporte_moras):
    reporte_mora = CreditoReporteMora.query.get(id_credito_reporte_moras)
    if not reporte_mora:
        return jsonify({'mensaje': 'Reporte de Mora no encontrado'}), 404

    resultado = {
        'id_credito_reporte_moras': reporte_mora.id_credito_reporte_moras,
        'id_credito': reporte_mora.id_credito,
        'monto': reporte_mora.monto
    }
    return jsonify(resultado)
