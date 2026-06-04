# Padroes do Projeto

## Python

- Seguir PEP 8 para formatacao e organizacao do codigo.
- Usar type hints em funcoes, dependencias e retornos sempre que possivel.
- Incluir docstrings em endpoints, dependencias e funcoes de suporte.
- Manter nomes descritivos e consistentes com o dominio de tarefas.

## Estrutura

- `app/main.py`: instancia FastAPI, eventos e endpoints.
- `app/database.py`: engine, sessao, base declarativa e dependency `get_db`.
- `app/models.py`: modelos SQLAlchemy.
- `app/schemas.py`: schemas Pydantic para entrada e saida.
- `requirements.txt`: dependencias diretas do projeto.

## FastAPI

- Usar `Depends(get_db)` para obter sessoes de banco.
- Definir `response_model` em endpoints que retornam dados.
- Usar `HTTPException` para erros de dominio, especialmente `404`.
- Agrupar endpoints de tarefas com `tags=["Tasks"]`.
- Manter endpoints pequenos, claros e com uma unica responsabilidade.

## Validacao

- Validar payloads de entrada com Pydantic.
- Aplicar limites de tamanho em campos textuais.
- Usar schemas diferentes para criacao, atualizacao e resposta.
- Em atualizacoes parciais, usar `model_dump(exclude_unset=True)`.

## Banco de Dados

- Declarar modelos com SQLAlchemy ORM.
- Fazer `commit` apenas depois das alteracoes necessarias.
- Usar `refresh` depois de criar ou atualizar registros retornados pela API.
- Fechar sessoes por meio da dependency `get_db`.
