# 🏋️‍♂️ FitTrack — Preparação Pré-Bariátrica

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-orange)](https://sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Aplicação web para acompanhamento de saúde e exercícios no pré-operatório de cirurgia bariátrica.**

O **FitTrack** foi desenvolvido para apoiar pacientes durante a preparação para cirurgia bariátrica, reunindo **exercícios adaptados**, **conteúdo educativo** e **monitoramento de progresso** em uma única plataforma.

---

## 🚀 Visão Geral

- 👤 Acompanhamento individual do usuário  
- 📊 Monitoramento de evolução física  
- 🏃 Exercícios seguros e adaptados  
- 📚 Conteúdo educativo especializado  

---

## ✨ Funcionalidades

### 🔐 Autenticação
- Login com sessão segura  
- Proteção de rotas privadas  
- Logout com confirmação  

### 📊 Dashboard
- Estatísticas de exercícios  
- Sequência de dias ativos  
- Estimativa de calorias  
- Dicas de saúde diárias  

### 🏃 Exercícios
- 8 exercícios organizados por categoria:
  - Cardio
  - Aquático
  - Flexibilidade
  - Fortalecimento  
- Instruções passo a passo  
- Controle de intensidade  
- Tempo recomendado  

### 📚 Conteúdo Educativo
- Artigos sobre:
  - Pré-operatório  
  - Nutrição  
  - Comportamento  
  - Exercícios  
- Conteúdo organizado e acessível  

### 🎨 Interface
- Responsiva (mobile, tablet, desktop)  
- Layout moderno com Bootstrap  
- Animações leves em CSS  
- Ícones com Font Awesome  

---

## 🛠️ Tecnologias

| Camada        | Tecnologias |
|---------------|------------|
| Back-end      | Python + Flask |
| Banco de Dados| SQLite |
| Front-end     | HTML, CSS, JavaScript |
| Estilo        | Bootstrap 5 |
| Templates     | Jinja2 |

---

## 📁 Estrutura do Projeto

```bash
fittrack/
├── app.py
├── init_db.py
├── requirements.txt
├── fittrack.db
├── static/
│   ├── css/style.css
│   └── js/main.js
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── dashboard.html
    ├── exercicios.html
    ├── artigos.html
    ├── artigo_detalhe.html
    └── demo_exercicios.html
🚀 Como Executar
# Clone o projeto
git clone https://github.com/seu-usuario/fittrack.git
cd fittrack

# Crie ambiente virtual
python -m venv venv

# Ative o ambiente
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Instale dependências
pip install -r requirements.txt

# Inicialize o banco
python init_db.py

# Execute o projeto
python app.py

Acesse: http://127.0.0.1:5000

🔑 Acesso de Teste
Campo	Valor
Email	admin@fit.com

Senha	123456
📱 Rotas do Sistema
Tela	Rota
Início	/
Login	/login
Dashboard	/dashboard
Exercícios	/exercicios
Artigos	/artigos
Artigo	/artigo/<id>
Demo	/demo
🎯 Público-Alvo
Pacientes pré-bariátricos
Clínicas e hospitais
Nutricionistas
Educadores físicos
Equipes multidisciplinares
🧘 Exercícios Disponíveis
Caminhada leve
Hidroginástica
Alongamento
Pilates iniciante
Bicicleta ergométrica
Yoga adaptada
Treino leve
Natação terapêutica
📚 Conteúdos
Preparação física pré-bariátrica
Nutrição antes da cirurgia
Mudança de hábitos
Exercícios para iniciantes
Checklist pré-operatório
🔒 Segurança

⚠️ Projeto educacional

Atualmente inclui:

Controle de sessão
Proteção de rotas
Validação básica
Para produção, implementar:
Hash de senha (bcrypt/argon2)
HTTPS
Logs de auditoria
Validações avançadas
