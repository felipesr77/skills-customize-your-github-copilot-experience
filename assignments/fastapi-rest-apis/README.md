# 📘 Tarefa: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa APIs REST modernas e eficientes usando o framework FastAPI em Python, aprendendo sobre roteamento, validação de dados, documentação automática e boas práticas de desenvolvimento de APIs.

## 📝 Tarefas

### 🛠️ Criar API Básica com Endpoints GET e POST

#### Descrição
Crie uma API simples para gerenciar uma lista de tarefas (TODO items) com endpoints para listar e criar novas tarefas.

#### Requisitos
O programa concluído deve:

- Definir um modelo `Task` com campos `id`, `title`, `description` e `completed`
- Implementar um endpoint `GET /tasks` que retorna todas as tarefas
- Implementar um endpoint `POST /tasks` que cria uma nova tarefa
- Armazenar tarefas em memória (lista em Python)
- Retornar respostas JSON válidas com status HTTP apropriado (200, 201)
- Incluir documentação automática acessível em `/docs`

### 🛠️ Adicionar Validação e Tratamento de Erros

#### Descrição
Expanda a API anterior adicionando validação de dados, endpoints para atualizar e deletar tarefas, e tratamento robusto de erros.

#### Requisitos
O programa concluído deve:

- Validar dados de entrada usando Pydantic models
- Implementar endpoint `GET /tasks/{task_id}` para obter uma tarefa específica
- Implementar endpoint `PUT /tasks/{task_id}` para atualizar uma tarefa
- Implementar endpoint `DELETE /tasks/{task_id}` para deletar uma tarefa
- Retornar status 404 quando uma tarefa não for encontrada
- Retornar mensagens de erro descritivas
- Validar que `title` não é vazio e `description` é opcional

### 🛠️ Implementar Filtragem, Paginação e Autenticação Básica

#### Descrição
Implemente recursos avançados de API como filtragem, paginação e autenticação básica para proteger endpoints sensíveis.

#### Requisitos
O programa concluído deve:

- Adicionar query parameters para filtrar tarefas por status (`completed=true/false`)
- Implementar paginação com query parameters `skip` e `limit`
- Usar HTTP Bearer Token para autenticação básica em endpoints de escrita
- Retornar erro 401 Unauthorized quando o token for inválido
- Manter documentação automática atualizada com todas as funcionalidades
- Incluir exemplos de request/response na documentação

