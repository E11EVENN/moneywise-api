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
        'fecha_resgistro': pais.fecha_resgistro.isoformat(),
        'fecha_actualizacion': pais.fecha_actualizacion.isoformat(),
        'id_usuario': pais.id_usuario,
        'ip_address': pais.ip_address
    } for pais in paises]
    return jsonify(resultado)

@pais_v1_bp.route('/<id_pais>', methods=['GET'])
def obtener_pais(id_pais):
    pais = Pais.query.get(id_pais)
    if not pais:
        return jsonify({'mensaje': 'Pais no encontrado'}), 404

    resultado = {
        'id_pais': pais.id_pais,
        'nombre': pais.nombre,
        'indicativo_telefonico': float(pais.indicativo_telefonico),
        'estado': int(pais.estado),
        'fecha_resgistro': pais.fecha_resgistro.isoformat(),
        'fecha_actualizacion': pais.fecha_actualizacion.isoformat(),
        'id_usuario': pais.id_usuario,
        'ip_address': pais.ip_address
    }
    return jsonify(resultado)

# Aquí podrías definir más rutas para crear, actualizar y eliminar países si es necesario.
