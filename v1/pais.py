from flask import Blueprint, jsonify
from models import Pais

pais_v1_bp = Blueprint('pais_v1', __name__, url_prefix='/v1/pais')

@pais_v1_bp.route('/', methods=['GET'])
def obtener_paises():
    paises = Pais.query.all()
    resultado = [{
        'id_pais': pais.id_pais,
        'nombre': pais.nombre,
        'indicativo_telefonico': float(pais.indicativo_telefonico),
        'estado': int(pais.estado),
        'fecha_registro': pais.fecha_registro.isoformat() if pais.fecha_registro else None,
        'fecha_actualizacion': pais.fecha_actualizacion.isoformat() if pais.fecha_actualizacion else None,
        'usuario_id': pais.usuario_id,
        'id_address': pais.id_address  # Changed 'id_address' to 'ip_address'
    } for pais in paises]
    return jsonify(resultado)

@pais_v1_bp.route('/<int:id_pais>', methods=['GET'])  # Ensure id_pais is treated as an integer
def obtener_pais(id_pais):
    pais = Pais.query.get(id_pais)
    if not pais:
        return jsonify({'mensaje': 'Pais no encontrado'}), 404

    resultado = {
        'id_pais': pais.id_pais,
        'nombre': pais.nombre,
        'indicativo_telefonico': float(pais.indicativo_telefonico),
        'estado': int(pais.estado),
        'fecha_registro': pais.fecha_registro.isoformat() if pais.fecha_registro else None,
        'fecha_actualizacion': pais.fecha_actualizacion.isoformat() if pais.fecha_actualizacion else None,
        'usuario_id': pais.usuario_id,
        'id_address': pais.ip_address  # Changed 'id_address' to 'ip_address'
    }
    return jsonify(resultado)

# Add more routes for creating, updating, and deleting countries as needed.

