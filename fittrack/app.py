from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = 'fittrack_secret_key_2024'

DATABASE = 'fittrack.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    conn = get_db_connection()
    artigos = conn.execute('SELECT * FROM artigos ORDER BY id DESC LIMIT 3').fetchall()
    exercicios = conn.execute('SELECT * FROM exercicios ORDER BY id DESC LIMIT 4').fetchall()
    conn.close()
    return render_template('index.html', artigos=artigos, exercicios=exercicios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', 
                           (email, senha)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['nome']
            flash(f'Bem-vindo, {user["nome"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Você saiu da sua conta.', 'info')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db_connection()
    total_exercicios = conn.execute('SELECT COUNT(*) as total FROM exercicios').fetchone()['total']
    total_artigos = conn.execute('SELECT COUNT(*) as total FROM artigos').fetchone()['total']
    
    progresso = {
        'exercicios_realizados': 12,
        'dias_consecutivos': 5,
        'calorias_queimadas': 2450
    }
    conn.close()
    
    return render_template('dashboard.html', 
                         total_exercicios=total_exercicios,
                         total_artigos=total_artigos,
                         progresso=progresso)

@app.route('/exercicios')
@login_required
def exercicios():
    conn = get_db_connection()
    exercicios = conn.execute('SELECT * FROM exercicios ORDER BY categoria, nome').fetchall()
    conn.close()
    return render_template('exercicios.html', exercicios=exercicios)

@app.route('/artigos')
def artigos():
    conn = get_db_connection()
    artigos = conn.execute('SELECT * FROM artigos ORDER BY data_publicacao DESC').fetchall()
    conn.close()
    return render_template('artigos.html', artigos=artigos)

@app.route('/artigo/<int:id>')
def artigo_detalhe(id):
    conn = get_db_connection()
    artigo = conn.execute('SELECT * FROM artigos WHERE id = ?', (id,)).fetchone()
    conn.close()
    if artigo is None:
        flash('Artigo não encontrado.', 'danger')
        return redirect(url_for('artigos'))
    return render_template('artigo_detalhe.html', artigo=artigo)

@app.route('/demo')
def demo():
    """Página de demonstração visual dos exercícios com animações CSS"""
    return render_template('demo_exercicios.html')

@app.route('/exercicio-3d')
def exercicio_3d():
    """Página de exercícios em 3D com Three.js"""
    return render_template('exercicio_3d.html')

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        import init_db
    app.run(debug=True, host='0.0.0.0', port=5000)