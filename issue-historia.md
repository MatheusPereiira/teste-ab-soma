# Issue: História do Usuário — Teste A/B de Soma

## Título

Implementar teste A/B comparando soma recursiva e soma iterativa

## História do Usuário

**Como** estudante de Engenharia de Software,
**quero** executar um teste A/B que compare o desempenho da soma recursiva com a soma iterativa,
**para que** eu possa analisar qual abordagem é mais eficiente em termos de tempo de execução e apresentar os resultados de forma clara e documentada.

## Critérios de Aceitação

- [ ] O sistema deve gerar automaticamente uma lista com 5.000 números inteiros aleatórios
- [ ] O sistema deve executar a soma recursiva sobre a lista gerada
- [ ] O sistema deve executar a soma iterativa sobre a mesma lista
- [ ] Ambas as abordagens devem utilizar exatamente a mesma massa de dados
- [ ] O experimento deve ser repetido 200 vezes
- [ ] O tempo de execução de cada abordagem deve ser medido com `time.perf_counter()`
- [ ] Os resultados devem ser exibidos em formato de tabela no terminal
- [ ] O sistema deve calcular o tempo médio de cada abordagem
- [ ] O sistema deve informar qual abordagem foi mais rápida
- [ ] Os resultados devem ser exportados para um arquivo TXT

## Regras de Negócio

- O limite de recursão deve ser configurado para 20.000 (`sys.setrecursionlimit(20000)`)
- Os números inteiros gerados devem estar no intervalo de 1 a 1.000
- A validação deve garantir que ambas as somas retornem o mesmo resultado em cada rodada
- O arquivo de resultados deve ser salvo em `resultados/resultado-experimentos.txt`

## Prioridade

Alta

## Labels

`enhancement`, `user-story`
