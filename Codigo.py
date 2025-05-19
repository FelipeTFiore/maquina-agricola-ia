import sqlite3
from datetime import datetime


conn = sqlite3.connect('dados_agricolas.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TIMESTAMP,
    umidade REAL,
    fosforo TEXT,
    potassio TEXT,
    ph REAL,
    irrigacao TEXT
)
''')


dados = {
    'data': datetime.now(),
    'umidade': 45.0,
    'fosforo': 'Presente',
    'potassio': 'Ausente',
    'ph': 6.8,
    'irrigacao': 'Desligada'
}


cursor.execute('''
INSERT INTO leituras (data, umidade, fosforo, potassio, ph, irrigacao)
VALUES (?, ?, ?, ?, ?, ?)
''', (dados['data'], dados['umidade'], dados['fosforo'], dados['potassio'], dados['ph'], dados['irrigacao']))

conn.commit()
print("Dados salvos com sucesso!")
conn.close()
