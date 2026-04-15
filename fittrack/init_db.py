import sqlite3

def init_db():
    conn = sqlite3.connect('fittrack.db')
    cursor = conn.cursor()
    
    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Tabela de exercícios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercicios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            categoria TEXT NOT NULL,
            duracao_minutos INTEGER,
            intensidade TEXT,
            instrucoes TEXT,
            beneficios TEXT,
            imagem_url TEXT
        )
    ''')
    
    # Tabela de artigos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS artigos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            resumo TEXT,
            conteudo TEXT,
            categoria TEXT,
            autor TEXT,
            imagem_url TEXT,
            data_publicacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Usuário de teste
    cursor.execute('''
        INSERT OR IGNORE INTO usuarios (id, nome, email, senha) 
        VALUES (1, 'Administrador', 'admin@fit.com', '123456')
    ''')
    
    # Exercícios
    exercicios = [
        ('Caminhada Leve', 'Excelente exercício cardiovascular de baixo impacto', 
         'Cardio', 30, 'Baixa', 
         '1. Aqueça por 5 minutos\n2. Caminhe em ritmo confortável\n3. Mantenha postura ereta\n4. Respire naturalmente\n5. Retorne devagar',
         'Melhora capacidade cardiovascular, queima calorias, reduz estresse', None),
        
        ('Hidroginástica', 'Exercícios na água que reduzem impacto nas articulações',
         'Aquático', 45, 'Baixa a Moderada',
         '1. Entre na água até a cintura\n2. Faça movimentos de caminhada\n3. Use halteres aquáticos\n4. Execute abdominais na vertical\n5. Termine com relaxamento',
         'Zero impacto, trabalha todo o corpo, melhora circulação', None),
        
        ('Alongamento Sentado', 'Série de alongamentos para melhorar flexibilidade',
         'Flexibilidade', 15, 'Baixa',
         '1. Sente-se em uma cadeira firme\n2. Alongue braços para cima\n3. Gire o tronco suavemente\n4. Alongue pernas estendidas\n5. Respire profundamente',
         'Melhora flexibilidade, reduz tensão muscular, prepara para exercícios', None),
        
        ('Pilates Iniciante', 'Fortalecimento do core com baixo impacto',
         'Fortalecimento', 30, 'Baixa',
         '1. Deite-se de costas\n2. Eleve uma perna de cada vez\n3. Faça abdominal supra leve\n4. Trabalhe a respiração\n5. Progressão gradual',
         'Fortalece core, melhora postura, protege coluna', None),
        
        ('Bicicleta Ergométrica', 'Cardio sentado com controle de intensidade',
         'Cardio', 20, 'Moderada',
         '1. Ajuste o banco adequadamente\n2. Comece sem resistência\n3. Mantenha ritmo constante\n4. Aumente gradualmente\n5. Resfriamento de 5 min',
         'Fortalece pernas, melhora resistência, queima calorias', None),
        
        ('Yoga Adaptada', 'Prática de yoga para iniciantes e sobrepeso',
         'Flexibilidade', 40, 'Baixa',
         '1. Use blocos e apoios\n2. Posturas sentadas\n3. Respiração consciente\n4. Meditação guiada\n5. Relaxamento final',
         'Reduz ansiedade, melhora sono, aumenta consciência corporal', None),
        
        ('Treino de Força Leve', 'Exercícios com pesos leves ou elásticos',
         'Fortalecimento', 25, 'Baixa',
         '1. Aquecimento articular\n2. Agachamento assistido\n3. Rosca bíceps leve\n4. Desenvolvimento ombro\n5. Alongamento',
         'Preserva massa muscular, acelera metabolismo, fortalece ossos', None),
        
        ('Natação Terapêutica', 'Nado adaptado para condicionamento físico',
         'Aquático', 30, 'Baixa',
         '1. Aquecimento na borda\n2. Nado crawl adaptado\n3. Costas com prancha\n4. Exercícios de respiração\n5. Flutuação relaxante',
         'Trabalho cardiovascular completo, zero impacto articular', None)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO exercicios 
        (nome, descricao, categoria, duracao_minutos, intensidade, instrucoes, beneficios, imagem_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', exercicios)
    
    # Artigos
    artigos = [
        ('Preparação Física para Cirurgia Bariátrica: Guia Completo',
         'Descubra como a atividade física pré-operatória pode melhorar seus resultados cirúrgicos e recuperação.',
         '''<h2>Por que se exercitar antes da cirurgia?</h2>
         <p>A preparação física pré-bariátrica é fundamental para:</p>
         <ul>
             <li>Reduzir riscos cirúrgicos</li>
             <li>Acelerar a recuperação pós-operatória</li>
             <li>Estabelecer hábitos saudáveis</li>
             <li>Melhorar resultados a longo prazo</li>
         </ul>
         <h2>Quando começar?</h2>
         <p>O ideal é iniciar de 3 a 6 meses antes da cirurgia, com autorização médica.</p>
         <h2>Tipos de exercícios recomendados</h2>
         <p>Priorize atividades de baixo impacto como caminhada, hidroginástica, natação e pilates.</p>''',
         'Pré-Operatório', 'Dr. Ana Silva', None),
        
        ('Nutrição Pré-Bariátrica: O que Comer nos Meses Anteriores',
         'Orientações alimentares essenciais para preparar seu corpo para a cirurgia de emagrecimento.',
         '''<h2>Objetivos da dieta pré-operatória</h2>
         <p>A nutrição antes da bariátrica visa:</p>
         <ul>
             <li>Reduzir tamanho do fígado</li>
             <li>Corrigir deficiências nutricionais</li>
             <li>Perder peso inicial</li>
             <li>Adaptar hábitos alimentares</li>
         </ul>
         <h2>Alimentos prioritários</h2>
         <p>Proteínas magras, vegetais, frutas e grãos integrais devem ser a base.</p>
         <h2>Evite</h2>
         <p>Açúcares refinados, bebidas calóricas, alimentos ultraprocessados e álcool.</p>''',
         'Nutrição', 'Nutricionista Carlos Mendes', None),
        
        ('Mudança de Hábitos: A Base do Sucesso Pós-Bariátrico',
         'Entenda como a transformação comportamental começa muito antes do dia da cirurgia.',
         '''<h2>A jornada começa agora</h2>
         <p>O sucesso da cirurgia bariátrica depende 80% da mudança de comportamento.</p>
         <h2>Hábitos a desenvolver</h2>
         <ul>
             <li>Alimentação consciente</li>
             <li>Exercícios regulares</li>
             <li>Hidratação adequada</li>
             <li>Sono de qualidade</li>
             <li>Gestão do estresse</li>
         </ul>
         <h2>Apoio psicológico</h2>
         <p>Acompanhamento com psicólogo especializado é essencial durante todo o processo.</p>''',
         'Comportamento', 'Psicóloga Maria Oliveira', None),
        
        ('Exercícios Aquáticos: A Melhor Opção para Iniciantes',
         'Conheça os benefícios da hidroginástica e natação para quem está começando a se exercitar.',
         '''<h2>Vantagens da água</h2>
         <p>A água oferece resistência natural sem impacto nas articulações.</p>
         <h2>Benefícios específicos</h2>
         <ul>
             <li>Suporta até 90% do peso corporal</li>
             <li>Reduz risco de lesões</li>
             <li>Melhora circulação sanguínea</li>
             <li>Trabalha todos os grupos musculares</li>
         </ul>
         <h2>Como começar</h2>
         <p>Procure academias com piscina aquecida e professores especializados.</p>''',
         'Exercícios', 'Prof. Ricardo Santos', None),
        
        ('Checklist de Preparação: 30 Dias Antes da Cirurgia',
         'Lista completa de cuidados e preparativos para a reta final antes da operação.',
         '''<h2>Cuidados médicos</h2>
         <ul>
             <li>Exames laboratoriais atualizados</li>
             <li>Consulta com anestesista</li>
             <li>Avaliação cardiológica</li>
             <li>Última revisão nutricional</li>
         </ul>
         <h2>Preparativos práticos</h2>
         <ul>
             <li>Comprar vitaminas e suplementos</li>
             <li>Preparar alimentos pós-cirurgia</li>
             <li>Organizar casa para repouso</li>
             <li>Programar acompanhantes</li>
         </ul>
         <h2>Mentalidade</h2>
         <p>Mantenha o foco, visualize o sucesso e confie na equipe médica.</p>''',
         'Pré-Operatório', 'Equipe FitTrack', None)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO artigos (titulo, resumo, conteudo, categoria, autor, imagem_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', artigos)
    
    conn.commit()
    conn.close()
    print("✅ Banco de dados inicializado com sucesso!")

if __name__ == '__main__':
    init_db()