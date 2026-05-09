# Issue: Requisito Não Funcional — Usabilidade

## Título

RNF-002: Requisito Não Funcional de Usabilidade

## Descrição

O sistema deve apresentar os resultados de forma clara, organizada e de fácil compreensão, tanto no terminal quanto no arquivo TXT exportado, facilitando a análise dos dados pelo usuário.

## Requisitos

### RNF-002.1 — Exibição em tabela

- Os resultados devem ser exibidos em formato de tabela utilizando a biblioteca `tabulate`
- A tabela deve conter as colunas: Rodada, Tempo Recursiva (s), Tempo Iterativa (s), Soma, Mais Rápida
- O formato da tabela deve ser `grid` para melhor legibilidade

### RNF-002.2 — Estatísticas resumidas

- Ao final da execução, o sistema deve exibir um resumo estatístico contendo:
  - Número de repetições realizadas
  - Tamanho da lista utilizada
  - Intervalo dos valores gerados
  - Tempo médio de cada abordagem
  - Número de vitórias de cada abordagem
  - Abordagem vencedora (mais rápida na média)
  - Diferença percentual entre as abordagens

### RNF-002.3 — Exportação para arquivo

- Os resultados completos (tabela + estatísticas) devem ser exportados para um arquivo TXT
- O arquivo deve incluir cabeçalho com data de execução e parâmetros do experimento
- O arquivo deve ser salvo em `resultados/resultado-experimentos.txt`
- O diretório `resultados/` deve ser criado automaticamente se não existir

### RNF-002.4 — Feedback durante a execução

- O sistema deve exibir informações de configuração antes de iniciar o experimento
- O sistema deve informar que o experimento está em andamento
- O sistema deve confirmar a exportação do arquivo ao final

## Critérios de Aceitação

- [ ] A tabela é exibida corretamente no terminal com formato `grid`
- [ ] As estatísticas resumidas são claras e completas
- [ ] O arquivo TXT é gerado automaticamente com todos os dados
- [ ] O sistema exibe feedback durante todas as etapas da execução
- [ ] O arquivo exportado é legível e bem formatado

## Prioridade

Média

## Labels

`non-functional`, `usability`
