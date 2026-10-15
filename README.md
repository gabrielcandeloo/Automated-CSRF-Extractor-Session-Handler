# 🕵️‍♂️ Analisador de Estado de Sessão e Extração Web (Web Scraper & Session Automator)

## 📖 Sobre o Projeto
Ferramenta desenvolvida em Python para mapear a superfície de ataque de aplicações web, extrair dinamicamente tokens de defesa e automatizar o envio de requisições HTTP mantendo o estado da sessão ativo.

## 🚀 Funcionalidades
* **Spidering HTML:** Utiliza a biblioteca BeautifulSoup para analisar o código-fonte e isolar campos de entrada (`<input>`) visíveis e ocultos.
* **Extração de Tokens:** Localiza e captura programaticamente chaves de segurança CSRF (Cross-Site Request Forgery) geradas dinamicamente pelo servidor na camada de apresentação.
* **Gerenciamento de Sessão:** Implementa túneis contínuos com `requests.Session()` para reter cookies e manipular cabeçalhos de requisição entre os métodos GET e POST.

## 🛠 Tecnologias
* **Linguagem:** Python 3
* **Bibliotecas:** `requests`, `beautifulsoup4`

## 🧠 Conceitos de Cibersegurança Analisados
* **Superfície de Ataque:** Identificação de vetores de entrada de dados.
* **Mecânica de Tokens CSRF:** Estudo sobre como as aplicações utilizam senhas invisíveis e temporárias para impedir ataques de automação e falsificação de requisições.
* **Sanitização de Backend:** Análise teórica das defesas de servidor (Consultas Parametrizadas) utilizadas para mitigar injeções de código.
