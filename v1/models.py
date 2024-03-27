
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
    id_address = db.Column(db.String(15), nullable=True)  # Cambiado a minúsculas

    def __repr__(self):
        return f"<Pais(id_pais='{self.id}', nombre='{self.nombre}', indicativo_telefonico={self.indicativo_telefonico}, estado={self.estado}, fecha_resgistro='{self.fecha_resgistro}', fecha_actualizacion='{self.fecha_actualizacion}', id_usuario='{self.id_usuario}', id_address='{self.id_address}')>"

class Ciudad(db.Model):
    __tablename__ = 'ciudad'
    __table_args__ = {'schema': 'public'}

    id_ciudad = db.Column(db.String(3), primary_key=True)  # Cambiado a minúsculas
    id_departamento = db.Column(db.String(3), nullable=True) 
    nombre = db.Column(db.String(40), nullable=False)  # Cambiado a minúsculas
    indicativo = db.Column(db.Numeric(4), nullable=False)  # Cambiado a minúsculas
    estado = db.Column(db.Numeric(1), nullable=False)  # Cambiado a minúsculas
    fecha_registro = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow)  # Cambiado a minúsculas
    fecha_actulizacion = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)  # Cambiado a minúsculas
    
    def __repr__(self):
        return f"<Ciudad(id_ciudad='{self.id}', id_departamento='{self.id_departamento}',nombre='{self.nombre}', indicativo={self.indicativo}, estado={self.estado}, fecha_registro='{self.fecha_registro}', fecha_actulizacion='{self.fecha_actulizacion}')>"
