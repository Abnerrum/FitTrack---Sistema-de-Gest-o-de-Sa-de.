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
## 📁 Estrutura do Projeto

```bash
fittrack/
├── app.py                 # Servidor Flask principal
├── init_db.py             # Inicialização do banco de dados
├── requirements.txt       # Dependências do projeto
├── fittrack.db            # Banco SQLite
│
├── static/
│   ├── css/
│   │   └── style.css      # Estilos personalizados
│   └── js/
│       └── main.js        # Scripts JavaScript
│
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── dashboard.html
    ├── exercicios.html
    ├── artigos.html
    ├── artigo_detalhe.html
    └── demo_exercicios.html
