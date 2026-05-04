import pandas as pd
import mysql.connector
import numpy as np
from google.colab import userdata

conn = mysql.connector.connect(
    host="serverless-europe-west3.sysp0000.db2.skysql.com", port=4050,
    user="dbpgf32109072", password=userdata.get('SENHA_SKYSQL'), database="LUMINA",
    ssl_ca="/content/globalsignrootca.pem"
)
cursor = conn.cursor()

anos = [2023]

for ano in anos:
    print(f"📥 Baixando reuniões e votos de {ano}...")
    url_votos = f"https://dadosabertos.camara.leg.br/arquivos/votacoesVotos/csv/votacoesVotos-{ano}.csv"
    url_pautas = f"https://dadosabertos.camara.leg.br/arquivos/votacoes/csv/votacoes-{ano}.csv"

    # 1. Inserir Reuniões
    df_pautas = pd.read_csv(url_pautas, sep=';', low_memory=False)
    dados_reuniao = list(zip(df_pautas['id'], [ano] * len(df_pautas)))

    sql_reuniao = "INSERT IGNORE INTO reuniao (cd_reuniao, ano) VALUES (%s, %s)"
    cursor.executemany(sql_reuniao, dados_reuniao)
    conn.commit()

    # 2. Inserir Presenças (Votos)
    df_votos = pd.read_csv(url_votos, sep=';', low_memory=False).dropna(subset=['deputado_id'])
    dados_presenca = list(zip(
        [ano] * len(df_votos),
        df_votos['deputado_id'].astype(int),
        df_votos['idVotacao']
    ))

    sql_presenca = """INSERT IGNORE INTO presencas (ano, fk_deputado, fk_reuniao)
                      VALUES (%s, %s, %s)"""

    try:
        # Lote por conta do tamanho
        tamanho_lote = 15000
        for i in range(0, len(dados_presenca), tamanho_lote):
            lote = dados_presenca[i:i + tamanho_lote]
            cursor.executemany(sql_presenca, lote)
            conn.commit()
        print(f"✅ Votos de {ano} inseridos!")
    except Exception as e:
        print(f"Erro nas presenças: {e}")
        conn.rollback()

cursor.close()
conn.close()


import mysql.connector
from google.colab import userdata

# Conectar usando a senha segura guardada no painel Secrets do Colab
conn = mysql.connector.connect(
    host="serverless-europe-west3.sysp0000.db2.skysql.com",
    port=4050,
    user="dbpgf32109072",
    password=userdata.get('SENHA_SKYSQL'),
    database="LUMINA",
    ssl_ca="/content/globalsignrootca.pem"
)
cursor = conn.cursor()

# Executar a criação das tabelas
comandos_sql = [
    """CREATE TABLE IF NOT EXISTS despesas (
        cd_despesas INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(100),
        quantidade INT DEFAULT 1,
        gasto_total DECIMAL(10, 2),
        fk_deputado INT,
        FOREIGN KEY (fk_deputado) REFERENCES deputado(cd_deputado)
    );""",

    """CREATE TABLE IF NOT EXISTS top_temas (
        cd_tp_temas INT AUTO_INCREMENT PRIMARY KEY,
        tipo VARCHAR(100),
        quantidade_pautas INT,
        fk_despesas INT,
        FOREIGN KEY (fk_despesas) REFERENCES despesas(cd_despesas)
    );""",

    """CREATE TABLE IF NOT EXISTS desempenho (
        cd_desempenho INT AUTO_INCREMENT PRIMARY KEY,
        score_presenca DECIMAL(5, 2),
        score_gastos DECIMAL(5, 2),
        score_projetos DECIMAL(5, 2),
        aprovadas_proposicoes INT,
        total_proposicoes INT,
        taxa_prop_aprovada DECIMAL(5, 2),
        score_final DECIMAL(5, 2),
        fk_deputado INT UNIQUE,
        FOREIGN KEY (fk_deputado) REFERENCES deputado(cd_deputado)
    );""",

    """CREATE TABLE IF NOT EXISTS tema_proposicoes (
        cd_tema INT PRIMARY KEY,
        nome VARCHAR(100),
        peso INT DEFAULT 1
    );""",

    """CREATE TABLE IF NOT EXISTS proposicoes (
        cd_proposicoes INT PRIMARY KEY,
        keywords TEXT,
        nome VARCHAR(255),
        autoria INT CHECK (autoria IN (0, 1, 2)),
        status VARCHAR(50),
        tipo VARCHAR(50),
        fk_deputado INT,
        fk_tema INT,
        FOREIGN KEY (fk_deputado) REFERENCES deputado(cd_deputado),
        FOREIGN KEY (fk_tema) REFERENCES tema_proposicoes(cd_tema)
    );""",

    """CREATE TABLE IF NOT EXISTS reuniao (
        cd_reuniao INT PRIMARY KEY,
        quantidade_nominal INT,
        ano INT
    );""",

    """CREATE TABLE IF NOT EXISTS presencas (
        cd_presenca INT AUTO_INCREMENT PRIMARY KEY,
        presenca_nominal INT DEFAULT 1,
        ano INT,
        fk_deputado INT,
        fk_reuniao INT,
        FOREIGN KEY (fk_deputado) REFERENCES deputado(cd_deputado),
        FOREIGN KEY (fk_reuniao) REFERENCES reuniao(cd_reuniao)
    );"""
]

for cmd in comandos_sql:
    cursor.execute(cmd)

conn.commit()
print("✅ Todas as tabelas criadas com sucesso!")
cursor.close()
conn.close()