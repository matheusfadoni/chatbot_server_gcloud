<p>Este projeto implementa um servidor Flask que expõe um webhook para buscar produtos em planilhas do Google Sheets. Ele foi projetado para ser executado em um ambiente Docker com suporte a HTTPS.</p>

<hr>

<h2>Funcionalidades</h2>
<ol>
    <li><strong>Busca de Produtos:</strong>
        <ul>
            <li>Recebe uma requisição com o nome de um produto e um setor.</li>
            <li>Retorna os produtos mais similares ao termo buscado com base nas informações contidas nas planilhas do Google Sheets.</li>
        </ul>
    </li>
    <li><strong>Integração com Google Sheets:</strong>
        <ul>
            <li>Lê dados de diferentes planilhas baseadas no setor informado.</li>
        </ul>
    </li>
    <li><strong>Segurança:</strong>
        <ul>
            <li>Configurado para rodar com HTTPS utilizando certificados SSL.</li>
        </ul>
    </li>
    <li><strong>Hospedagem:</strong>
        <ul>
            <li>Configurado para ser executado no Google Cloud.</li>
        </ul>
    </li>
</ol>

<hr>

<h2>Requisitos</h2>
<ol>
    <li><strong>Certificados SSL:</strong>
        <ul>
            <li>Certificados gerados e armazenados nos caminhos configurados para o domínio do usuário (exemplo: <code>/etc/letsencrypt/live/seu-dominio.com/</code>).</li>
            <li>Certificados devem ser válidos (não auto-assinados) e podem ser gerados por outras ferramentas como Certbot, Let’s Encrypt ou serviços pagos. É necessário possuir um domínio para gerar certificados aceitos pela API do Google.</li>
            <li>Os arquivos de certificado (<code>.pem</code>) precisam estar na mesma pasta do <code>Dockerfile</code> durante o processo de build.</li>
        </ul>
    </li>
    <li><strong>Dependências:</strong>
        <ul>
            <li>Python 3.10</li>
            <li>Flask</li>
            <li>Google API Client</li>
            <li>FuzzyWuzzy</li>
            <li>Levenshtein</li>
        </ul>
    </li>
    <li><strong>Credenciais do Google API:</strong>
        <ul>
            <li>Ative a API do Google Sheets no <a href="https://console.cloud.google.com">Console do Google Cloud</a>.</li>
            <li>Baixe o arquivo <code>credentials.json</code> com suas credenciais e coloque-o no diretório raiz do projeto.</li>
        </ul>
    </li>
    <li><strong>Docker:</strong>
        <ul>
            <li>Configurações especificadas no Dockerfile para criar a imagem do projeto.</li>
        </ul>
    </li>
</ol>

<hr>

<h2>Estrutura do Projeto</h2>
<ul>
    <li><code>buscar_produto.py</code>:
        <ul>
            <li>Contém a lógica de busca de produtos nas planilhas do Google Sheets.</li>
        </ul>
    </li>
    <li><code>projeto_flask.py</code>:
        <ul>
            <li>Servidor Flask que expõe o endpoint <code>/webhook</code>.</li>
        </ul>
    </li>
    <li><code>Dockerfile</code>:
        <ul>
            <li>Configuração para criar o contêiner Docker.</li>
        </ul>
    </li>
    <li><code>.gitignore</code>:
        <ul>
            <li>Define arquivos ignorados pelo Git, como <code>credentials.json</code>.</li>
        </ul>
    </li>
</ul>

<hr>

<h2>Como Usar</h2>
<h3>1. Criar a Imagem Docker</h3>
<p>No diretório do projeto, execute:</p>
<pre><code>docker build -t busca-produto .</code></pre>

<h3>2. Executar o Contêiner</h3>
<p>Execute o contêiner:</p>
<pre><code>docker run -d -p 53329:53329 --name busca-produto busca-produto</code></pre>

<h3>3. Testar o Webhook</h3>
<p>Envie uma requisição POST para o endpoint com o <code>curl</code>:</p>
<pre><code>curl -X POST https://seu-dominio.com:53329/webhook \</code>
-H "Content-Type: application/json" </code>
     -d '{"produto": "gin tanqueray", "setor": "BEBIDAS"}'
Certifique-se de substituir https://seu-dominio.com pelo domínio que você está usando.
<hr>

<h2>Configuração Adicional</h2>
<h3>Configurar o <code>credentials.json</code></h3>
<ol>
    <li>Ative a API do Google Sheets no <a href="https://console.cloud.google.com">Console do Google Cloud</a>.</li>
    <li>Baixe o arquivo <code>credentials.json</code> e coloque-o no diretório raiz do projeto.</li>
</ol>

<h3>Certificados SSL</h3>
<p>Certificados podem ser gerados com o <a href="https://certbot.eff.org/">Certbot</a> ou outras ferramentas e armazenados nos caminhos configurados. Lembre-se de usar um domínio válido.</p>

<hr>

<h2>Avisos</h2>
<ol>
    <li><strong>Segurança:</strong>
        <ul>
            <li>Nunca compartilhe o arquivo <code>credentials.json</code> publicamente.</li>
            <li>Certifique-se de proteger os certificados SSL.</li>
        </ul>
    </li>
    <li><strong>Hospedagem:</strong>
        <ul>
            <li>Este projeto utiliza a API do Google Sheets, que pode gerar um custo adicional de aproximadamente US$ 3 por mês, dependendo do uso.</li>
        </ul>
    </li>
</ol>
