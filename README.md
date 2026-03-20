# 🏋️‍♂️ FitTrack - Gestão de Saúde e Exercícios

O **FitTrack** é uma aplicação web Full Stack projetada para centralizar informações de saúde e organizar rotinas de exercícios de forma simples e eficiente. Este projeto demonstra a integração de um front-end responsivo com um back-end funcional em Python.

---

## 🚀 Funcionalidades

- **Autenticação de Usuários:** Sistema de login seguro com gerenciamento de sessões.
- **Área Logada (Dashboard):** Espaço restrito para usuários visualizarem conteúdos exclusivos.
- **Banco de Dados Dinâmico:** Os artigos de saúde e tipos de exercícios são carregados diretamente do banco de dados SQLite.
- **Design Responsivo:** Interface limpa e adaptável para diferentes tamanhos de tela.
- **Segurança de Rotas:** Proteção que impede o acesso à área interna sem a realização do login.

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** [Python](https://www.python.org/) + [Flask](https://flask.palletsprojects.com/)
- **Banco de Dados:** [SQLite](https://sqlite.org/)
- **Front-end:** HTML5, CSS3 e Jinja2 (Engine de Templates)
- **Ambiente:** Servidor WSGI de desenvolvimento do Flask

---

## 📂 Estrutura do Projeto

- `app.py`: Lógica principal do servidor, rotas e conexão com banco de dados.
- `fittrack.db`: Arquivo do banco de dados relacional.
- `/templates`: Arquivos HTML (Página Inicial, Login, Painel).
- `/static`: Arquivos CSS de estilização.

---

## 🔧 Como Executar o Projeto

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/fittrack.git


1. Instale o framework Flask:
code
Bash
pip install flask
2.  Inicie o servidor:
code
Bash
python app.py

3. Acesse no seu navegador: http://127.0.0.1:5000
🔑 Credenciais de Teste
E-mail: admin@fit.com
Senha: 123456

📝 Licença
Este projeto foi desenvolvido para fins de estudo e portfólio. Sinta-se à vontade para clonar e modificar!
code
Code
---

