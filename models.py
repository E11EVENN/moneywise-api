from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Pais(db.Model):
    __tablename__ = 'pais'
    __table_args__ = {'schema': 'public'}

    id_pais = db.Column(db.Numeric(10), primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    codigo = db.Column(db.String(3), nullable=False)
    capital = db.Column(db.String(255), nullable=False)
    region = db.Column(db.String(255), nullable=False)  # Agregado según la estructura de la tabla
    fecha_registro = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    usuario_id = db.Column(db.String(10), nullable=True)
    ip_address = db.Column(db.String(50), nullable=True)  # Longitud actualizada a 50

    def __repr__(self):
        return f"<Pais(id_pais='{self.id_pais}', nombre='{self.nombre}', codigo='{self.codigo}', capital='{self.capital}', region='{self.region}', fecha_registro='{self.fecha_registro}',  usuario_id='{self.usuario_id}', ip_address='{self.ip_address}')>"
