# Controle de Materiais do Laboratório

Projeto introdutório de programação para acompanhar materiais de um pequeno laboratório de informática. O contexto é simulado e pode ser adaptado a uma organização conhecida pelo estudante.

## Executar

É necessário ter Python 3 instalado. No terminal, dentro desta pasta, execute:

```bash
python3 controle_materiais.py
```

No Windows, caso necessário, use:

```bash
py controle_materiais.py
```

Não é necessário instalar bibliotecas externas.

## O que o programa faz

- Cadastra materiais com quantidade atual e limite mínimo.
- Lista os materiais cadastrados.
- Registra entradas e saídas/uso.
- Impede a retirada de uma quantidade maior que o saldo.
- Mostra quais materiais chegaram ao mínimo ou estão abaixo dele.

Para demonstrar, cadastre “Cabo HDMI” com quantidade 4 e mínimo 1. Registre uma saída de 3 unidades e consulte a opção de reposição: o material deve aparecer com saldo 1.

## Limitação desta primeira versão

Os dados ficam em uma lista na memória do programa. Ao fechar o programa, os registros são apagados. Salvamento em arquivo pode ser uma melhoria posterior, se fizer parte do escopo aceito pelo professor.

## Arquivos

- `controle_materiais.py`: programa executável pelo Python.
- `DOCUMENTACAO_PROJETO.docx` e `DOCUMENTACAO_PROJETO.pdf`: documentação do projeto.

## Repositório online

https://github.com/franciellyneyane/controle-materiais-laboratorio

O repositório está público. O professor pode abrir o link e baixar os arquivos sem convite. Qualquer outra pessoa também poderá ver o código e os documentos.
