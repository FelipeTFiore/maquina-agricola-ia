Sistema de irrigação automatizado com sensores simulados e banco de dados SQLite

📌 Visão Geral
Projeto desenvolvido para a disciplina de [Tarefa Cap 1: Construindo uma Maquina agricola] que simula um sistema de irrigação inteligente com:

Hardware: ESP32, sensores de umidade, pH, fósforo e potássio (simulados no Wokwi).

Software: Lógica de controle em C++ e armazenamento em banco de dados SQLite via Python.

Vídeo Demonstrativo (https://www.youtube.com/watch?v=yV4pkV2_Nac)

🛠 Estrutura do Projeto
maquina-agricola-ia/  
├── ESP32/  
│   ├── main.cpp          # Código do microcontrolador  
│   ├── circuito.png      # Esquema do circuito  
│   └── README.md         # Detalhes do hardware  
├── Python/  
│   ├── database.py       # Script CRUD em Python  
│   └── README.md         # Documentação do banco de dados  
└── README.md             # Este arquivo  
🔌 Hardware (ESP32 no Wokwi)
Circuito
Circuito no Wokwi(https://wokwi.com/projects/431417188916801537)

Componentes
Sensor	Pino ESP32	Simulação no Wokwi
Umidade (DHT22)	GPIO13	DHT22
pH (LDR)	GPIO34	LDR + resistor 10kΩ
Fósforo	GPIO4	Botão digital
Potássio	GPIO5	Botão digital
Bomba (Relé)	GPIO12	Módulo Relé
 Código Comentado
 ESP32/main.cpp
cpp
#include <DHT.h>  
#define DHTPIN 13          // Pino do DHT22  
#define DHTTYPE DHT22      // Modelo do sensor  

DHT dht(DHTPIN, DHTTYPE);  

// Pinos dos sensores  
const int botaoFosforo = 4;   // Botão Fósforo (GPIO4)  
const int botaoPotassio = 5;  // Botão Potássio (GPIO5)  

void setup() {  
  pinMode(botaoFosforo, INPUT_PULLUP); // Configura botão com resistor pull-up interno  
  Serial.begin(9600); // Inicia comunicação serial  
}  

void loop() {  
  float umidade = dht.readHumidity(); // Lê umidade do DHT22  
  int fosforo = digitalRead(botaoFosforo); // 0 = pressionado (presente)  

  // Lógica de irrigação  
  if (umidade < 30) {  
    digitalWrite(12, HIGH); // Liga a bomba no GPIO12  
  }  
  delay(2000);  
}  
 Python/database.py
python
import sqlite3  
from datetime import datetime  

# Cria/conecta ao banco de dados  
conn = sqlite3.connect('dados_agricolas.db')  
cursor = conn.cursor()  

# Cria tabela (se não existir)  
cursor.execute('''  
CREATE TABLE IF NOT EXISTS leituras (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    data TIMESTAMP,  
    umidade REAL,  
    ph REAL  
)''')  

# Insere dados simulados  
cursor.execute('''  
INSERT INTO leituras (data, umidade, ph)  
VALUES (?, ?, ?)''', (datetime.now(), 45.0, 6.8))  

conn.commit()  
print("Dados salvos!")  
 Banco de Dados
Estrutura da Tabela
Coluna	Tipo	Descrição
id	INTEGER	Chave primária
data	TIMESTAMP	Data/hora da leitura
umidade	REAL	Valor de umidade (%)
ph	REAL	Nível de pH do solo
Operações CRUD
Create: INSERT INTO leituras (data, umidade) VALUES (...)

Read: SELECT * FROM leituras WHERE umidade < 30

 Como Executar
Simule o hardware:

Acesse o projeto no Wokwi e clique em "Play".

Execute o banco de dados:

bash
cd Python  
python3 database.py  
