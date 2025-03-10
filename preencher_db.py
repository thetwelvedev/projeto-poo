import os
import django
from datetime import datetime, timedelta

# Configura o Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from trave.models import Aeroporto, Voo

# Lista de capitais do Brasil
CAPITAIS_BRASIL = [
    {"codigo_aeroporto": "GRU", "nome": "Aeroporto de Guarulhos", "cidade": "São Paulo", "estado": "SP", "pais": "Brasil"},
    {"codigo_aeroporto": "GIG", "nome": "Aeroporto do Galeão", "cidade": "Rio de Janeiro", "estado": "RJ", "pais": "Brasil"},
    {"codigo_aeroporto": "BSB", "nome": "Aeroporto de Brasília", "cidade": "Brasília", "estado": "DF", "pais": "Brasil"},
    {"codigo_aeroporto": "CNF", "nome": "Aeroporto de Confins", "cidade": "Belo Horizonte", "estado": "MG", "pais": "Brasil"},
    {"codigo_aeroporto": "POA", "nome": "Aeroporto de Porto Alegre", "cidade": "Porto Alegre", "estado": "RS", "pais": "Brasil"},
    {"codigo_aeroporto": "SSA", "nome": "Aeroporto de Salvador", "cidade": "Salvador", "estado": "BA", "pais": "Brasil"},
    {"codigo_aeroporto": "FOR", "nome": "Aeroporto de Fortaleza", "cidade": "Fortaleza", "estado": "CE", "pais": "Brasil"},
    {"codigo_aeroporto": "REC", "nome": "Aeroporto do Recife", "cidade": "Recife", "estado": "PE", "pais": "Brasil"},
    {"codigo_aeroporto": "CGH", "nome": "Aeroporto de Congonhas", "cidade": "São Paulo", "estado": "SP", "pais": "Brasil"},
    {"codigo_aeroporto": "CWB", "nome": "Aeroporto de Curitiba", "cidade": "Curitiba", "estado": "PR", "pais": "Brasil"},
    {"codigo_aeroporto": "MAO", "nome": "Aeroporto de Manaus", "cidade": "Manaus", "estado": "AM", "pais": "Brasil"},
    {"codigo_aeroporto": "BEL", "nome": "Aeroporto de Belém", "cidade": "Belém", "estado": "PA", "pais": "Brasil"},
    {"codigo_aeroporto": "VCP", "nome": "Aeroporto de Viracopos", "cidade": "Campinas", "estado": "SP", "pais": "Brasil"},
    {"codigo_aeroporto": "FLN", "nome": "Aeroporto de Florianópolis", "cidade": "Florianópolis", "estado": "SC", "pais": "Brasil"},
    {"codigo_aeroporto": "GYN", "nome": "Aeroporto de Goiânia", "cidade": "Goiânia", "estado": "GO", "pais": "Brasil"},
    {"codigo_aeroporto": "NAT", "nome": "Aeroporto de Natal", "cidade": "Natal", "estado": "RN", "pais": "Brasil"},
    {"codigo_aeroporto": "CGB", "nome": "Aeroporto de Cuiabá", "cidade": "Cuiabá", "estado": "MT", "pais": "Brasil"},
    {"codigo_aeroporto": "BPS", "nome": "Aeroporto de Porto Seguro", "cidade": "Porto Seguro", "estado": "BA", "pais": "Brasil"},
    {"codigo_aeroporto": "SLZ", "nome": "Aeroporto de São Luís", "cidade": "São Luís", "estado": "MA", "pais": "Brasil"},
    {"codigo_aeroporto": "AJU", "nome": "Aeroporto de Aracaju", "cidade": "Aracaju", "estado": "SE", "pais": "Brasil"},
    {"codigo_aeroporto": "JPA", "nome": "Aeroporto de João Pessoa", "cidade": "João Pessoa", "estado": "PB", "pais": "Brasil"},
    {"codigo_aeroporto": "THE", "nome": "Aeroporto de Teresina", "cidade": "Teresina", "estado": "PI", "pais": "Brasil"},
    {"codigo_aeroporto": "PMW", "nome": "Aeroporto de Palmas", "cidade": "Palmas", "estado": "TO", "pais": "Brasil"},
    {"codigo_aeroporto": "MCZ", "nome": "Aeroporto de Maceió", "cidade": "Maceió", "estado": "AL", "pais": "Brasil"},
    {"codigo_aeroporto": "PVH", "nome": "Aeroporto de Porto Velho", "cidade": "Porto Velho", "estado": "RO", "pais": "Brasil"},
    {"codigo_aeroporto": "RBR", "nome": "Aeroporto de Rio Branco", "cidade": "Rio Branco", "estado": "AC", "pais": "Brasil"},
    {"codigo_aeroporto": "CGR", "nome": "Aeroporto de Campo Grande", "cidade": "Campo Grande", "estado": "MS", "pais": "Brasil"},
    {"codigo_aeroporto": "VIX", "nome": "Aeroporto de Vitória", "cidade": "Vitória", "estado": "ES", "pais": "Brasil"},
]

def criar_aeroportos():
    """Cria aeroportos para todas as capitais do Brasil."""
    for capital in CAPITAIS_BRASIL:
        Aeroporto.objects.get_or_create(**capital)

def criar_voos():
    """Cria voos entre todas as capitais do Brasil."""
    for origem in CAPITAIS_BRASIL:
        for destino in CAPITAIS_BRASIL:
            if origem["codigo_aeroporto"] != destino["codigo_aeroporto"]:
                # Voos de ida (12h e 23h)
                Voo.objects.get_or_create(
                    codigo_voo=f"{origem['codigo_aeroporto']}-{destino['codigo_aeroporto']}-12",
                    origem=Aeroporto.objects.get(codigo_aeroporto=origem["codigo_aeroporto"]),
                    destino=Aeroporto.objects.get(codigo_aeroporto=destino["codigo_aeroporto"]),
                    data_partida=datetime.now() + timedelta(days=1),
                    data_chegada=datetime.now() + timedelta(days=1, hours=2),
                    preco=300.00,  # Preço base
                    assentos_disponiveis=100,
                )
                Voo.objects.get_or_create(
                    codigo_voo=f"{origem['codigo_aeroporto']}-{destino['codigo_aeroporto']}-23",
                    origem=Aeroporto.objects.get(codigo_aeroporto=origem["codigo_aeroporto"]),
                    destino=Aeroporto.objects.get(codigo_aeroporto=destino["codigo_aeroporto"]),
                    data_partida=datetime.now() + timedelta(days=1, hours=11),
                    data_chegada=datetime.now() + timedelta(days=1, hours=13),
                    preco=350.00,  # Preço base
                    assentos_disponiveis=80,
                )

if __name__ == "__main__":
    criar_aeroportos()
    criar_voos()
    print("Banco de dados populado com sucesso!")