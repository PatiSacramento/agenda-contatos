# Agenda de contatos

Aplicação de linha de comando escrita em Python para cadastrar, consultar, editar, excluir, importar e exportar contatos.

Os contatos são mantidos em memória durante a execução e persistidos no arquivo `database.csv`.

## Requisitos

- Python 3 (testado com Python 3.14.3)
- Nenhuma dependência externa

## Como executar

No diretório do projeto, execute:

```bash
python agenda.py
```

Ao iniciar, a aplicação tenta carregar os contatos de `database.csv` e exibe um menu interativo:

```text
1 - Mostrar todos os contatos da agenda
2 - Buscar contato
3 - Incluir contato
4 - Editar contato
5 - Excluir contato
6 - Exportar contatos para CSV
7 - Importar contatos CSV
0 - Fechar agenda
```

## Funcionalidades

- **Mostrar contatos:** lista todos os contatos carregados.
- **Buscar contato:** procura um contato pelo nome exato.
- **Incluir contato:** cadastra um novo nome, telefone, e-mail e endereço. Nomes já cadastrados não são duplicados.
- **Editar contato:** substitui os dados de um contato existente.
- **Excluir contato:** remove um contato pelo nome.
- **Exportar contatos:** grava a agenda em um arquivo informado pelo usuário.
- **Importar contatos:** lê contatos de um arquivo CSV e adiciona ou atualiza os registros.

As operações de inclusão, edição e exclusão salvam automaticamente o estado atual em `database.csv`.

## Formato dos arquivos CSV

Cada linha deve conter quatro campos, nesta ordem:

```text
nome, telefone, email, endereco
```

Exemplo:

```text
Patricia, 99999-9999, patricia@email.com, av. 1
```

Os arquivos `contatos.csv` e `importar.csv` servem como exemplos de dados para exportação e importação. O arquivo `database.csv` é a base carregada automaticamente pela aplicação.

## Estrutura do projeto

```text
.
├── agenda.py      # Aplicação principal e operações da agenda
├── contatos.py    # Exemplo independente de um dicionário de contatos
├── database.csv   # Base persistida e carregada na inicialização
├── contatos.csv   # Exemplo de arquivo CSV
└── importar.csv   # Exemplo de arquivo para importação
```

`contatos.py` não é utilizado por `agenda.py`; ele apenas demonstra uma estrutura simples de dados em Python.

## Observações

- A busca de nomes diferencia maiúsculas e minúsculas e exige o nome completo digitado da mesma forma que foi cadastrado.
- Os campos são separados por vírgulas. Portanto, não use vírgulas dentro de um nome, e-mail, telefone ou endereço.
- Se `database.csv` não existir, a aplicação informa o erro e inicia com a agenda vazia; o arquivo será criado quando uma operação que salva dados for realizada.
