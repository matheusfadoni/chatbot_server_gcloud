import json
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from fuzzywuzzy import process
from collections import OrderedDict

# Configuracoes da API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
creds = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)

def buscar_produto(search_term, setor):
    # IDs das planilhas para cada setor
    spreadsheet_ids = {
        'BEBIDAS': '1Tvi73W85NpqbRFxhMQWlq2_-D1d3PAp1KZ2Iej6alk4',
        'PERFUMES': '1Vt7Q9Qy9djHhVYhIZa64JMfJf3bnqatMJxx-2_NJqfo',
        'COMESTIVEIS': '1t3aYnWKok0G4A_GtwYSaZ007WUozflDkkqmCTptKCPY',
        'CASA E COZINHA': '1l-vEHPwAu0JcLDcbaxaarIr-XwQua-JlZlgtMpWYOno',
        'ELETRÔNICOS': '14KnaCb9D9SeCU-imtKk36IUaTPC4slbHeDtQdpv8HvI',
        'MODA': '1drlVmNLKGP-oe6jIUkSecv29GF5fJoFUvnanqQ0yi60',
        'ESPORTE': '1Kzyy5ZOMuyXWKVtlchroEHsFRVz0TLEhQfwqpyvw5G0',
        'CAMPING E PESCA': '1cCaViGYU_027Pl3z2j2ThKCCj6wGlbxEtxZQzvrUfUQ',
        'COSMETICOS': '1KaWVLm1J-s13XXdjsYvFxEW1NynV1PirxVyPTTRPujI',
        'CRIANÇAS': '1tsWjoz1wrTzF3eqrIIAMp4EpDkxqQ4XZBYarZfA8Qo4'
    }

    # Seleciona a planilha correta com base no setor
    SPREADSHEET_ID = spreadsheet_ids.get(setor.upper())

    if not SPREADSHEET_ID:
        raise ValueError(f"Setor '{setor}' inválido. Opções disponíveis: {', '.join(spreadsheet_ids.keys())}.")

    # Lendo dados da planilha
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A:C').execute()
    values = result.get('values', [])

    # Criando um dicionário com SKU como chave e nome e preco como valores
    products = {item[0]: {"produto": item[1], "preco": item[2]} for item in values if len(item) > 2}

    # Buscando as 5 melhores correspondencias no nome do produto
    best_matches = process.extract(search_term, [info["produto"] for info in products.values()], limit=5)

    # Preparando o resultado com similaridade para ordenar
    result = [
        OrderedDict([
            ("sku", sku),
            ("produto", info["produto"]),
            ("preco", info["preco"]),
            ("similaridade", match[1])  # Adicionando similaridade para ordenar
        ])
        for match in best_matches
        for sku, info in products.items()
        if info["produto"] == match[0]
    ]

    # Ordenando os resultados pela similaridade (do maior para o menor)
    result.sort(key=lambda x: x["similaridade"], reverse=True)

    # Removendo a chave "similaridade" antes de retornar
    for item in result:
        item.pop("similaridade")

    return result  # Retorna a lista de dicionarios diretamente
