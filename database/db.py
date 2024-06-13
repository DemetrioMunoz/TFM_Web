from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mammographic_masses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir el modelo de datos
class Observation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Float, nullable=False)
    shape = db.Column(db.Integer, nullable=False)
    margin = db.Column(db.Integer, nullable=False)
    density = db.Column(db.Integer, nullable=False)
    malignant = db.Column(db.Integer, nullable=False)  # Asumiendo que 'malignant' es una columna

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Cargar datos del archivo CSV
data_file_path = "mammographic_masses_data.csv"
df = pd.read_csv(data_file_path)
df = df.dropna()

# Insertar datos en la base de datos
with app.app_context():
    for _, row in df.iterrows():
        observation = Observation(
            age=row['age'],
            shape=row['shape'],
            margin=row['margin'],
            density=row['density'],
            malignant=row['malignant']  # Asumiendo que 'malignant' es una columna
        )
        db.session.add(observation)
    db.session.commit()
