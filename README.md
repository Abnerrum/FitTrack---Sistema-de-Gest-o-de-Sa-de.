# 🏋️‍♂️ FitTrack - Preparação Pré-Bariátrica

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-orange)](https://sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Aplicação web completa para gestão de saúde e exercícios físicos preparatórios para cirurgia bariátrica.**

O **FitTrack** é uma plataforma desenvolvida para auxiliar pacientes no período pré-operatório de cirurgia bariátrica, oferecendo exercícios adaptados, artigos educativos e acompanhamento do progresso físico.

---

## ✨ Funcionalidades

### 🔐 Sistema de Autenticação
- Login seguro com sessões
- Proteção de rotas privadas
- Logout com confirmação

### 📊 Dashboard Personalizado
- Estatísticas de exercícios realizados
- Contador de dias consecutivos
- Calorias queimadas
- Dicas diárias de saúde

### 🏃 Exercícios Especializados
- **8 exercícios** categorizados por tipo:
  - 🏃 Cardio (Caminhada, Bicicleta)
  - 💧 Aquático (Hidroginástica, Natação)
  - 🧘 Flexibilidade (Alongamento, Yoga)
  - 💪 Fortalecimento (Pilates, Musculação leve)
- Instruções passo a passo
- Nível de intensidade (Baixa/Moderada)
- Duração recomendada

### 📚 Artigos Educativos
- **5 artigos** sobre saúde e bariátrica
- Categorias: Pré-Operatório, Nutrição, Comportamento, Exercícios
- Autores especializados
- Data de publicação

### 🎨 Interface Moderna
- Design responsivo (mobile, tablet, desktop)
- Animações CSS interativas
- Tema profissional com Bootstrap 5
- Ícones Font Awesome

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|------------|
| **Back-end** | Python 3.8+ + Flask |
| **Banco de Dados** | SQLite 3 |
| **Front-end** | HTML5, CSS3, JavaScript |
| **Framework CSS** | Bootstrap 5.3 |
| **Ícones** | Font Awesome 6 |
| **Template Engine** | Jinja2 |

---

## 📁 Estrutura do Projeto
fittrack/
├── 📄 app.py                 # Servidor Flask principal
├── 📄 init_db.py             # Script de inicialização do BD
├── 📄 requirements.txt       # Dependências Python
├── 📄 fittrack.db            # Banco de dados SQLite
├── 📁 static/
│   ├── 📁 css/
│   │   └── 📄 style.css      # Estilos personalizados + animações
│   └── 📁 js/
│       └── 📄 main.js        # Scripts JavaScript
└── 📁 templates/
├── 📄 base.html          # Template base
├── 📄 index.html         # Página inicial
├── 📄 login.html         # Tela de login
├── 📄 dashboard.html     # Painel do usuário
├── 📄 exercicios.html    # Lista de exercícios
├── 📄 artigos.html       # Lista de artigos
├── 📄 artigo_detalhe.html # Detalhe do artigo
└── 📄 demo_exercicios.html # Demonstração com animações
plain
common.copy

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- pip (gerenciador de pacotes Python)

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/fittrack.git
cd fittrack

# 2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv

# Ative o ambiente virtual:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicialize o banco de dados (execute uma vez)
python init_db.py

# 5. Inicie o servidor
python app.py

# 6. Acesse no navegador
# http://127.0.0.1:5000
🔑 Credenciais de Teste
Use estas credenciais para acessar o sistema:
segment.table
Campo	Valor
Email	admin@fit.com
Senha	123456
📱 Telas do Sistema
segment.table
Tela	Descrição	Rota
🏠 Início	Apresentação do projeto e destaques	/
🔐 Login	Autenticação de usuários	/login
📊 Dashboard	Painel com estatísticas do usuário	/dashboard
🏃 Exercícios	Lista completa de exercícios	/exercicios
📚 Artigos	Blog com conteúdos educativos	/artigos
📖 Artigo	Leitura completa de um artigo	/artigo/<id>
🎬 Demo	Demonstração visual com animações	/demo
🎯 Público-Alvo
👨‍⚕️ Pacientes em preparação para cirurgia bariátrica
🏥 Clínicas e hospitais de referência em obesidade
👩‍⚕️ Nutricionistas e educadores físicos
🧠 Psicólogos e equipes multidisciplinares
🧘 Exercícios Disponíveis
segment.table
Exercício	Categoria	Duração	Intensidade
Caminhada Leve	Cardio	30 min	Baixa
Hidroginástica	Aquático	45 min	Baixa/Moderada
Alongamento Sentado	Flexibilidade	15 min	Baixa
Pilates Iniciante	Fortalecimento	30 min	Baixa
Bicicleta Ergométrica	Cardio	20 min	Moderada
Yoga Adaptada	Flexibilidade	40 min	Baixa
Treino de Força Leve	Fortalecimento	25 min	Baixa
Natação Terapêutica	Aquático	30 min	Baixa
📚 Artigos Incluídos
Preparação Física para Cirurgia Bariátrica: Guia Completo
Nutrição Pré-Bariátrica: O que Comer nos Meses Anteriores
Mudança de Hábitos: A Base do Sucesso Pós-Bariátrico
Exercícios Aquáticos: A Melhor Opção para Iniciantes
Checklist de Preparação: 30 Dias Antes da Cirurgia
🔒 Segurança
Senhas armazenadas em texto plano (modo demonstração)
Sessões Flask para controle de acesso
Rotas protegidas com decorator @login_required
Validação de formulários no front-end e back-end
⚠️ Nota: Este é um projeto educacional. Para uso em produção, implemente:
Hash de senhas (bcrypt/argon2)
HTTPS/TLS
Validações adicionais
Logs de auditoria
