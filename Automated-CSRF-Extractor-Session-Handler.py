import requests
from bs4 import BeautifulSoup

sessao = requests.Session()
alvo = 'http://quotes.toscrape.com/login'

# 1. Reconhecimento e Mapeamento
resposta = sessao.get(alvo)
sopa = BeautifulSoup(resposta.text, 'html.parser')

# 2. Definição Base do Pacote de Dados
dados_login = {'username': 'admin', 'password': '12345'}

# 3. Busca e Validação Dinâmica do Token CSRF
token_oculto = sopa.find('input', {'name': 'csrf_token'})

if token_oculto:
    res_token = token_oculto.get('value')
    dados_login['csrf_token'] = res_token
    print(f"[+] Token CSRF detectado e anexado: {res_token}")
else:
    print("[-] Nenhum token CSRF detectado. Prosseguindo com pacote padrão.")

# 4. Execução do Envio com Manutenção de Estado (Sessão)
print("\nPacote final pronto para envio:", dados_login)
tentativa_login = sessao.post(alvo, data=dados_login)

# 5. Validação do Resultado Defensivo
if "Password" not in tentativa_login.text:
    print("\nStatus: Login processado ou redirecionamento bem-sucedido.")
else:
    print("\nStatus: Bloqueado. A página retornou o formulário de login.")