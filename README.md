# Task Management API

API REST para gerenciamento de tarefas criada com FastAPI, SQLAlchemy e SQLite.

## Tecnologias

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

## Estrutura

```text
app/
  __init__.py
  database.py
  main.py
  models.py
  schemas.py
.coderabbit.yaml
.gitignore
AGENTS.md
README.md
requirements.txt
```

## Setup

Clone o repositorio e acesse a pasta do projeto:

```bash
git clone <url-do-repositorio>
cd TESTE_IA
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Execute a API:

```bash
uvicorn app.main:app --reload
```

A API ficara disponivel em:

```text
http://127.0.0.1:8000
```

## Documentacao interativa

Use o Swagger UI para testar os endpoints:

```text
http://127.0.0.1:8000/docs
```

Tambem ha documentacao ReDoc em:

```text
http://127.0.0.1:8000/redoc
```

## Endpoints

- `GET /`: mensagem de boas-vindas.
- `POST /tasks/`: cria uma tarefa.
- `GET /tasks/`: lista tarefas com paginacao e filtro opcional por status.
- `GET /tasks/{task_id}`: busca uma tarefa por ID.
- `PUT /tasks/{task_id}`: atualiza uma tarefa.
- `DELETE /tasks/{task_id}`: remove uma tarefa.

## Exemplos no PowerShell

Criar uma tarefa:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"title":"Estudar FastAPI","description":"Criar uma API CRUD com SQLite"}'
```

Listar tarefas:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/?skip=0&limit=10" `
  -Method GET
```

Filtrar tarefas concluidas:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/?completed=true" `
  -Method GET
```

Buscar uma tarefa:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/1" `
  -Method GET
```

Atualizar uma tarefa:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/1" `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"completed":true}'
```

Excluir uma tarefa:

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:8000/tasks/1" `
  -Method DELETE
```

Se preferir usar o `curl` tradicional no PowerShell, chame `curl.exe` em vez de
`curl`, pois `curl` sozinho costuma ser um alias do `Invoke-WebRequest`.

## Banco de dados

O SQLite usa o arquivo `tasks.db`, criado automaticamente na primeira inicializacao da API.





## Script de Prompt de Comando

Criar projeto FastAPI completo do zero com API de gerenciamento de tarefas.

ESTRUTURA DE ARQUIVOS:
- app/__init__.py (vazio, marca como pacote)
- app/main.py (aplicação FastAPI)
- app/database.py (configuração SQLite)
- app/models.py (modelos SQLAlchemy)
- app/schemas.py (schemas Pydantic)
- .gitignore (incluir: venv/, __pycache__/, *.db, .env, .vscode/)
- requirements.txt
- README.md (com instruções completas de setup e uso)
- AGENTS.md (padrões de código do projeto)
- .coderabbit.yaml (configuração CodeRabbit em português)

DEPENDÊNCIAS A INSTALAR:
- fastapi
- uvicorn[standard]
- sqlalchemy
- pydantic

IMPLEMENTAÇÃO DETALHADA:

1. app/database.py:
   - SQLAlchemy engine com SQLite (arquivo tasks.db)
   - URL: sqlite:///./tasks.db
   - SessionLocal com sessionmaker(autocommit=False, autoflush=False)
   - Base = declarative_base()
   - Função get_db() para dependency injection com yield

2. app/models.py:
   - Importar Base de app.database
   - Classe Task(Base) com __tablename__ = "tasks"
   - Campos: id (Integer, primary_key, index), title (String, nullable=False, index), 
     description (String), completed (Boolean, default=False), 
     created_at (DateTime, default=datetime.utcnow)

3. app/schemas.py:
   - TaskCreate: title (Field min_length=3, max_length=100), 
     description (Optional, max_length=500)
   - TaskUpdate: todos campos Optional
   - TaskResponse: todos campos + from_attributes=True (Pydantic v2)

4. app/main.py:
   - FastAPI(title="Task Management API", description="...", version="1.0.0")
   - models.Base.metadata.create_all(bind=engine) no startup
   - Endpoints CRUD completos com tags=["Tasks"]:
     * POST /tasks/ (response_model=TaskResponse, status_code=201)
     * GET /tasks/ (List[TaskResponse], params: skip=0, limit=10, completed: Optional[bool])
     * GET /tasks/{task_id} (TaskResponse)
     * PUT /tasks/{task_id} (TaskResponse)
     * DELETE /tasks/{task_id} (status_code=204)
   - Tratamento HTTPException 404 para task não encontrada
   - Docstrings em todas as funções
   - Endpoint raiz GET / retorna mensagem de boas-vindas

5. README.md incluir:
   - Descrição do projeto
   - Tecnologias usadas
   - Instruções de setup (clonar, venv, instalar, rodar)
   - Como testar a API (via /docs)
   - Exemplos de requisições

6. AGENTS.md incluir:
   - Padrões Python (PEP 8, type hints, docstrings)
   - Estrutura do projeto
   - Convenções FastAPI
   - Padrões de validação

7. .coderabbit.yaml:
   - language: "pt"
   - reviews.high_level_summary: true
   - path_filters para ignorar venv/, __pycache__/, *.db
   - path_instructions específicas para app/models.py, app/schemas.py, app/main.py

APÓS CRIAR TODOS OS ARQUIVOS:
1. Executar: pip install -r requirements.txt
2. Confirmar que todas dependências foram instaladas
3. Informar que o projeto está pronto para rodar com: uvicorn app.main:app --reload
