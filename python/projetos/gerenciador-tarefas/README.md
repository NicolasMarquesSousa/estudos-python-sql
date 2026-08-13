# Gerenciador de tarefas

Projeto de terminal desenvolvido em Python para praticar funções, classes, listas, dicionários, arquivos JSON e tratamento de erros.

## Funcionalidades

- Cadastrar tarefas.
- Listar tarefas pendentes e concluídas.
- Marcar uma tarefa como concluída.
- Remover tarefas.
- Salvar os dados automaticamente em `tarefas.json`.

## Como executar

Na pasta deste projeto, execute:

```bash
python gerenciador.py
```

Não é necessário instalar bibliotecas externas.

## Testes

```bash
python -m unittest -v test_gerenciador.py
```

O arquivo `tarefas.json` é criado somente durante o uso e não precisa ser enviado ao GitHub.
