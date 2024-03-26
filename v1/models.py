
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id_pais = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    nombre = db.Column(db.String(40), nullable=False)  # Cambiado a minúsculas
    indicativo_telefonico = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Numeric(1), nullable=False)  # Cambiado a minúsculas
    fecha_resgistro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actualizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    id_usuario = db.Column(db.String(10), nullable=True)  # Cambiado a minúsculas
    ip_address = db.Column(db.String(15), nullable=True)  # Cambiado a minúsculas

    def __repr__(self):
        return f"<Pais(id_pais='{self.id}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_resgistro='{self.fecha_resgistro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', ip_address='{self.ip_address}')>"
