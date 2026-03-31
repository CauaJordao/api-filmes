# Projeto: API de Catálogo de Filmes Clássicos
**Instituição**: Universidade de Vassouras  
**Disciplina**: Desenvolvimento Back-end

## 1. Tema do Sistema
Um sistema de catálogo para gerenciar os melhores filmes de todos os tempos, permitindo a classificação por categorias técnicas e consulta via API REST.

## 2. Funcionalidades Esperadas
* Cadastro e edição de filmes via Django Admin.
* Endpoint JSON para listagem completa de filmes.
* Endpoint de consulta filtrada por gênero cinematográfico.

## 3. Dados Armazenados
* **Título**: Nome da obra.
* **Diretor**: Responsável pela direção.
* **Ano**: Data de lançamento original.
* **Gênero**: Categoria do filme (Drama, Ação, etc).
* **Nota IMDb**: Avaliação técnica.
* **Categoria**: Status de controle (Lançamento, Clássico ou Cult) via parâmetro *choices*.