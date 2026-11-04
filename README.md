# Controle de Materiais do Laboratório

Projeto introdutório de programação em Python para cadastrar materiais, registrar entradas e saídas e avisar quando a quantidade chega ao limite mínimo. O cenário é didático e simulado. O código foi mantido simples e não salva os dados depois que o programa é fechado.

## Arquivos da versão atual

- `DOCUMENTACAO_PROJETO_AMPLIADA.pdf`: relatório de 18 páginas, destinado à entrega após conferência da capa.
- `DOCUMENTACAO_PROJETO_AMPLIADA.docx`: cópia editável do relatório.
- `controle_materiais.py`: código executável do programa.
- `README.md`: instruções de execução e resumo do projeto.

Os arquivos `DOCUMENTACAO_PROJETO.pdf` e `DOCUMENTACAO_PROJETO.docx`, caso apareçam neste repositório, são versões anteriores mais curtas. Para a entrega atual, usar os arquivos com o sufixo `AMPLIADA`. O código também está reproduzido no Apêndice A do PDF. Se a entrega aceitar apenas um arquivo, enviar somente o PDF ampliado.

## Executar o programa

É necessário ter Python 3 instalado. No terminal, dentro da pasta do arquivo, executar:

```bash
python3 controle_materiais.py
```

No Windows, caso necessário, usar:

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

Demonstração: cadastrar “Cabo HDMI” com quantidade 4 e mínimo 1; registrar uma saída de 3 unidades; consultar a opção de reposição. O material deve aparecer com saldo 1.

## Limitação da primeira versão

Os dados ficam em uma lista na memória do programa e são apagados ao fechar o programa. Salvamento em arquivo, histórico de movimentações e interface gráfica não fazem parte desta versão.

## Repositório online

https://github.com/franciellyneyane/controle-materiais-laboratorio

O repositório está público. O professor pode abrir o link e consultar ou baixar o código sem convite. Qualquer pessoa com o endereço também poderá ver os arquivos.
