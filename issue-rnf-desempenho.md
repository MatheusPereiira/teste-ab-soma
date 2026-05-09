# Issue: Requisito Não Funcional — Desempenho

## Título

RNF-001: Requisito Não Funcional de Desempenho

## Descrição

O sistema deve executar o experimento completo (200 repetições com listas de 5.000 elementos) em tempo aceitável, garantindo medições precisas e confiáveis do tempo de execução de cada abordagem.

## Requisitos

### RNF-001.1 — Precisão na medição de tempo

- O tempo de execução deve ser medido utilizando `time.perf_counter()`
- A precisão deve ser de pelo menos 6 casas decimais (microsegundos)
- A medição deve incluir apenas o tempo de execução da função de soma, excluindo tempo de geração de dados

### RNF-001.2 — Limite de recursão

- O limite de recursão do Python deve ser configurado para `20.000` via `sys.setrecursionlimit(20000)`
- O valor deve suportar listas de até 5.000 elementos sem causar `RecursionError`

### RNF-001.3 — Tempo total de execução

- O experimento completo (200 repetições) deve ser concluído em tempo razoável
- O sistema não deve apresentar travamentos ou lentidão excessiva durante a execução

### RNF-001.4 — Integridade dos resultados

- Ambas as abordagens devem retornar exatamente o mesmo valor de soma para cada rodada
- O sistema deve validar a integridade dos resultados com `assert`

## Critérios de Aceitação

- [ ] `time.perf_counter()` é utilizado para todas as medições de tempo
- [ ] O limite de recursão está configurado para 20.000
- [ ] O experimento completo é executado sem erros de recursão
- [ ] Os resultados de ambas as abordagens são idênticos em cada rodada
- [ ] O tempo total de execução é razoável (inferior a 5 minutos)

## Prioridade

Alta

## Labels

`non-functional`, `performance`
