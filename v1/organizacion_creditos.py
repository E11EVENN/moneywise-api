from flask import Blueprint, jsonify
from models import OrganizacionCredito

organizacion_credito_v1_bp = Blueprint('organizacion_credito_v1', __name__, url_prefix='/v1/organizacion_creditos')

@organizacion_credito_v1_bp.route('/', methods=['GET'])
def obtener_organizacion_creditos():
    organizacion_creditos = OrganizacionCredito.query.all()
    resultado = [{
        'id_organizacion_credito': org_credito.id_organizacion_credito,
        'id_organizacion': org_credito.id_organizacion,
        'id_credito': org_credito.id_credito
    } for org_credito in organizacion_creditos]
    return jsonify(resultado)

@organizacion_credito_v1_bp.route('/<string:id_organizacion_credito>', methods=['GET'])
def obtener_organizacion_credito(id_organizacion_credito):
    org_credito = OrganizacionCredito.query.get(id_organizacion_credito)
    if not org_credito:
        return jsonify({'mensaje': 'Organización Crédito no encontrado'}), 404

    resultado = {
        'id_organizacion_credito': org_credito.id_organizacion_credito,
        'id_organizacion': org_credito.id_organizacion,
        'id_credito': org_credito.id_credito
    }
    return jsonify(resultado)
