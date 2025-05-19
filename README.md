# 🌾 Sistema de Irrigação Automatizado com ESP32

> Projeto desenvolvido para a disciplina **Tarefa Cap 1: Construindo uma Máquina Agrícola**  
> Simulação de um sistema inteligente com sensores e banco de dados SQLite

[![Vídeo Demonstrativo](](https://www.youtube.com/watch?v=yV4pkV2_Nac)

## 🧰 Componentes do Sistema

### Hardware (Simulado no Wokwi)
| Componente       | Pino ESP32 | Simulação          |
|------------------|------------|--------------------|
| DHT22 (Umidade)  | GPIO13     | Sensor de umidade  |
| LDR (pH)         | GPIO34     | + Resistor 10kΩ    |
| Botão (Fósforo)  | GPIO4      | Entrada digital    |
| Botão (Potássio) | GPIO5      | Entrada digital    |
| Relé (Bomba)     | GPIO12     | Atuador de irrigação |

🔗 [Acesse o Circuito no Wokwi](https://wokwi.com/projects/431417188916801537)

## 📂 Estrutura do Projeto
projeto-agricola/
├── ESP32/
│ ├── main.cpp # Lógica de controle
│ ├── circuito.png # Diagrama esquemático
│ └── README.md # Especificações técnicas
└── Python/
├── database.py # Gerenciamento do banco
└── README.md # Documentação SQL


## 💻 Código Fonte

### ESP32 (Controle de Sensores)
```cpp
#include <DHT.h>
#define DHTPIN 13         // Conexão do DHT22
#define DHTTYPE DHT22     // Modelo do sensor

void setup() {
  pinMode(4, INPUT_PULLUP); // Configura botão Fósforo
  Serial.begin(9600);       // Inicia comunicação serial
}

void loop() {
  float umidade = dht.readHumidity();
  
  // Aciona bomba se umidade < 30%
  if(umidade < 30) {
    digitalWrite(12, HIGH); 
    Serial.println("Bomba ativada");
  }
  delay(2000);
}
Python (Banco de Dados)
python
import sqlite3
from datetime import datetime

def criar_tabela():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leituras (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        umidade REAL,
        ph REAL
    )''')
    conn.commit()
    conn.close()
🛠 Como Executar
Simulação Hardware:

Acesse o projeto no Wokwi

Clique em ▶️ para iniciar

Banco de Dados:

bash
cd Python
python database.py
