# Usar uma imagem base do Python 3.10
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos do projeto para o diretório de trabalho
COPY . .

# Instalar as bibliotecas necessárias diretamente no Dockerfile
RUN pip install --no-cache-dir Flask \
    && pip install --no-cache-dir google-auth \
    && pip install --no-cache-dir google-auth-oauthlib \
    && pip install --no-cache-dir google-auth-httplib2 \
    && pip install --no-cache-dir google-api-python-client \
    && pip install --no-cache-dir fuzzywuzzy \
    && pip install --no-cache-dir python-Levenshtein

# Expor a porta que o Flask usará
EXPOSE 53329

# Adicionar um certificado SSL/TLS (autogenerado ou fornecido)
# Neste exemplo, assumimos que você tenha um certificado SSL autoassinado em um arquivo chamado 'cert.pem' e uma chave privada em 'key.pem'
COPY cert.pem /etc/ssl/certs/cert.pem
COPY key.pem /etc/ssl/private/key.pem

# Definir a variável de ambiente FLASK_APP
ENV FLASK_APP=projeto_flask.py

# Comando para rodar o servidor Flask com HTTPS
CMD ["flask", "run", "--host=0.0.0.0", "--port=53329", "--cert=/etc/ssl/certs/cert.pem", "--key=/etc/ssl/private/key.pem"]
