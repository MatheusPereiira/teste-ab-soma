# Teste A/B — Soma Recursiva vs Soma Iterativa 🧪

## Descrição

O **Teste A/B — Soma Recursiva vs Soma Iterativa** é um projeto acadêmico voltado para a análise comparativa de desempenho entre duas abordagens clássicas de soma de elementos em uma lista: **recursiva** e **iterativa**.

O sistema gera automaticamente uma massa de dados com **5.000 números inteiros aleatórios**, executa ambas as abordagens utilizando exatamente os mesmos dados, repete o experimento **200 vezes**, mede o tempo de execução com alta precisão e apresenta os resultados em formato de tabela com estatísticas detalhadas.

## Objetivo

Aplicar conceitos de **Engenharia de Software**, **análise de algoritmos** e **testes comparativos (A/B)**, documentando o processo com **casos de uso**, **diagramas UML** e **issues no GitHub**, simulando um fluxo de trabalho profissional.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `tabulate`
- `time.perf_counter()` (medição de alta precisão)
- `sys.setrecursionlimit(20000)`
- PlantUML
- Markdown
- Git
- GitHub
- GitHub CLI (`gh`)

## Estrutura do Projeto

```
teste-ab-soma/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── issue-historia.md
├── issue-caso-de-uso.md
├── issue-rnf-desempenho.md
├── issue-rnf-usabilidade.md
├── docs/
│   ├── diagramas/
│   │   └── diagrama-teste-ab-soma.puml
│   └── imagens/
│       └── diagrama-teste-ab-soma.png
└── resultados/
    └── resultado-experimentos.txt
```

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/MatheusPereiira/teste-ab-soma.git
cd teste-ab-soma
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar o projeto

```bash
python main.py
```

Os resultados serão exibidos no terminal e exportados automaticamente para `resultados/resultado-experimentos.txt`.

## Funcionalidades

- ✅ Geração automática de 5.000 números inteiros aleatórios
- ✅ Execução da soma recursiva
- ✅ Execução da soma iterativa
- ✅ Mesma massa de dados para ambas as abordagens
- ✅ Repetição do experimento 200 vezes
- ✅ Medição de tempo com `time.perf_counter()`
- ✅ Comparação dos resultados rodada a rodada
- ✅ Exibição em formato de tabela (`tabulate`)
- ✅ Cálculo do tempo médio de cada abordagem
- ✅ Identificação da abordagem mais rápida
- ✅ Exportação dos resultados para arquivo TXT

## Informações do Experimento

| Parâmetro                | Valor            |
|--------------------------|------------------|
| Tamanho da lista         | 5.000 números    |
| Repetições               | 200              |
| Intervalo dos valores    | 1 a 1.000        |
| Limite de recursão       | 20.000           |
| Precisão da medição      | `perf_counter()` |

## Diagrama de Caso de Uso

![Diagrama de Caso de Uso](docs/imagens/diagrama-teste-ab-soma.png)

## Objetivo Acadêmico

Aplicar técnicas de levantamento de requisitos, modelagem UML e análise de desempenho de algoritmos, representando funcionalidades de um sistema real de forma clara e organizada.

Projeto desenvolvido na disciplina de **Fundamentos da Engenharia de Software**, durante o **3º período de Engenharia de Software** na **Faculdade de Nova Serrana (FANS)**.

## Autor

- Matheus Pereira
