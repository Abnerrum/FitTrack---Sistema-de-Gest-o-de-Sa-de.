from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'chave_super_secreta' # Para gerenciar sessões de login

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
DB_NAME = 'fittrack.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Tabela de Usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    # Tabela de Pesquisas/Artigos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pesquisas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')
    
    # Inserir dados iniciais para teste
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", ('admin@fit.com', '123456'))
        
        artigos = [
            ('OMS — Atividade Física', 'https://www.who.int/news-room/fact-sheets/detail/physical-activity'),
            ('MedlinePlus — Exercício e Fitness', 'https://medlineplus.gov/exerciseandphysicalfitness.html'),
            ('NHLBI — Qualidade do Sono', 'https://www.nhlbi.nih.gov/health/heart-healthy-living/sleep')
        ]
        cursor.executemany("INSERT INTO pesquisas (titulo, url) VALUES (?, ?)", artigos)
        
    conn.commit()
    conn.close()

# --- ROTAS ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        user = conn.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_email'] = user['email']
            return redirect(url_for('painel'))
        else:
            return "Login inválido. <a href='/login'>Tente novamente</a>"

    return render_template('login.html')

@app.route('/painel')
def painel():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    artigos = conn.execute('SELECT * FROM pesquisas').fetchall()
    conn.close()
    
    return render_template('painel.html', artigos=artigos)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)