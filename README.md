# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

## 📌 Descrição do Projeto
Este projeto simula o desenvolvimento de um sistema web básico de gerenciamento de tarefas, criado para uma startup fictícia do setor de logística. O objetivo é demonstrar, de forma prática, a aplicação dos conceitos de Engenharia de Software, metodologias ágeis, versionamento de código, testes automatizados e integração contínua utilizando o GitHub.

## 🎯 Objetivo
Permitir o gerenciamento de tarefas por meio de operações básicas (CRUD), possibilitando o acompanhamento do fluxo de trabalho e a priorização de atividades críticas.

## 📦 Escopo Inicial (MVP)
- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Excluir tarefas
- Alterar status da tarefa (A Fazer, Em Progresso, Concluído)

## 🔄 Metodologia Ágil
Foi adotada a metodologia **Kanban**, utilizando o GitHub Projects para organização das atividades nas colunas:
- To Do
- In Progress
- Done

## 🧠 Mudança de Escopo (Simulação)
Durante o desenvolvimento, foi identificada a necessidade de **filtrar tarefas por status**, facilitando a visualização de tarefas críticas.

### Justificativa
A startup de logística necessita identificar rapidamente tarefas pendentes ou em andamento, otimizando o tempo de resposta da equipe.

### Alterações Realizadas
- Criação de novo card no Kanban
- Implementação do filtro por status no código
- Commit específico documentando a mudança
- O filtro foi implementado no método `filter_by_status` do TaskManager.


## 🧪 Testes Automatizados
Os testes foram implementados utilizando **PyTest**, validando:
- Criação de tarefas
- Validação de título obrigatório
- Alteração de status
- Filtro por status

## ⚙️ Integração Contínua
Foi configurado um pipeline de CI com **GitHub Actions**, executando automaticamente os testes a cada push ou pull request.

## ▶️ Como Executar
1. Clone o repositório
2. Instale o PyTest:
   ```bash
   pip install pytest
## ✅ Requisitos
- Python 3.10+ instalado
- PyTest instalado (pip install pytest)
