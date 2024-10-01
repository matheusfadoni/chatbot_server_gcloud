from flask import Flask, request, jsonify
from buscar_produto import buscar_produto

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    resultado = buscar_produto(data['produto'], setor=data.get('setor'))
    return jsonify(resultado), 200  # Usar jsonify para retornar JSON corretamente

if __name__ == "__main__":
    # Caminhos para os arquivos de certificado e chave gerados pelo Certbot
    context = ('/etc/letsencrypt/live/chatbotzendeskmapy.dev.br/fullchain.pem', 
               '/etc/letsencrypt/live/chatbotzendeskmapy.dev.br/privkey.pem')
    app.run(ssl_context=context, host='0.0.0.0', port=53329)
