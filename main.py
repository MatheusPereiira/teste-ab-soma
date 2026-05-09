"""
Teste A/B — Soma Recursiva vs Soma Iterativa
=============================================
Gera uma lista com 5 000 números inteiros aleatórios, executa ambas as
abordagens de soma (recursiva e iterativa) utilizando exatamente a mesma
massa de dados, repete o experimento 200 vezes, mede o tempo de execução,
compara os resultados e exporta tudo para um arquivo TXT.

Autor : Seu Nome
Data  : 2026-05-09
"""

import sys
import time
import random
import os
from tabulate import tabulate

# ---------------------------------------------------------------------------
# Configurações do experimento
# ---------------------------------------------------------------------------
sys.setrecursionlimit(20000)

TAMANHO_LISTA = 5000        # quantidade de números inteiros aleatórios
REPETICOES = 200            # quantidade de repetições do experimento
VALOR_MIN = 1               # valor mínimo dos números gerados
VALOR_MAX = 1000            # valor máximo dos números gerados
ARQUIVO_RESULTADO = os.path.join("resultados", "resultado-experimentos.txt")


# ---------------------------------------------------------------------------
# Funções de soma
# ---------------------------------------------------------------------------
def soma_recursiva(lista, indice=0):
    """Calcula a soma dos elementos da lista de forma recursiva."""
    if indice == len(lista):
        return 0
    return lista[indice] + soma_recursiva(lista, indice + 1)


def soma_iterativa(lista):
    """Calcula a soma dos elementos da lista de forma iterativa."""
    total = 0
    for numero in lista:
        total += numero
    return total


# ---------------------------------------------------------------------------
# Função auxiliar — execução cronometrada
# ---------------------------------------------------------------------------
def medir_tempo(funcao, *args):
    """Executa a funcao com os argumentos fornecidos e retorna (tempo_s, resultado)."""
    inicio = time.perf_counter()
    resultado = funcao(*args)
    fim = time.perf_counter()
    return fim - inicio, resultado


# ---------------------------------------------------------------------------
# Execução do experimento
# ---------------------------------------------------------------------------
def executar_experimento():
    """
    Executa o experimento A/B completo e devolve uma lista de registros
    com os dados de cada rodada.
    """
    registros = []

    for rodada in range(1, REPETICOES + 1):
        # Gera a mesma massa de dados para ambas as abordagens
        lista = [random.randint(VALOR_MIN, VALOR_MAX) for _ in range(TAMANHO_LISTA)]

        tempo_rec, resultado_rec = medir_tempo(soma_recursiva, lista)
        tempo_iter, resultado_iter = medir_tempo(soma_iterativa, lista)

        # Validação: ambas as somas devem ser iguais
        assert resultado_rec == resultado_iter, (
            "Divergencia na rodada {}: recursiva={}, iterativa={}".format(
                rodada, resultado_rec, resultado_iter
            )
        )

        mais_rapida = "Recursiva" if tempo_rec < tempo_iter else "Iterativa"

        registros.append([
            rodada,
            "{:.6f}".format(tempo_rec),
            "{:.6f}".format(tempo_iter),
            resultado_rec,
            mais_rapida,
        ])

    return registros


# ---------------------------------------------------------------------------
# Formatação e exibição dos resultados
# ---------------------------------------------------------------------------
CABECALHOS = [
    "Rodada",
    "Tempo Recursiva (s)",
    "Tempo Iterativa (s)",
    "Soma",
    "Mais Rapida",
]


def formatar_tabela(registros):
    """Retorna a tabela formatada como string."""
    return tabulate(registros, headers=CABECALHOS, tablefmt="grid")


def calcular_estatisticas(registros):
    """Calcula e retorna as estatisticas resumidas do experimento."""
    tempos_rec = [float(r[1]) for r in registros]
    tempos_iter = [float(r[2]) for r in registros]

    media_rec = sum(tempos_rec) / len(tempos_rec)
    media_iter = sum(tempos_iter) / len(tempos_iter)

    vitorias_rec = sum(1 for r in registros if r[4] == "Recursiva")
    vitorias_iter = REPETICOES - vitorias_rec

    vencedora = "Soma Recursiva" if media_rec < media_iter else "Soma Iterativa"
    diferenca = abs(media_rec - media_iter)
    percentual = (diferenca / max(media_rec, media_iter)) * 100

    linhas = [
        "",
        "=" * 60,
        "  ESTATISTICAS DO EXPERIMENTO",
        "=" * 60,
        "  Repeticoes realizadas       : {}".format(REPETICOES),
        "  Tamanho da lista            : {} numeros".format(TAMANHO_LISTA),
        "  Intervalo dos valores       : [{}, {}]".format(VALOR_MIN, VALOR_MAX),
        "",
        "  Tempo medio - Recursiva     : {:.6f} s".format(media_rec),
        "  Tempo medio - Iterativa     : {:.6f} s".format(media_iter),
        "",
        "  Vitorias - Recursiva        : {}/{}".format(vitorias_rec, REPETICOES),
        "  Vitorias - Iterativa        : {}/{}".format(vitorias_iter, REPETICOES),
        "",
        "  * Abordagem mais rapida     : {}".format(vencedora),
        "    Diferenca media           : {:.6f} s ({:.2f}%)".format(diferenca, percentual),
        "=" * 60,
    ]
    return "\n".join(linhas)


# ---------------------------------------------------------------------------
# Exportação para arquivo TXT
# ---------------------------------------------------------------------------
def exportar_resultados(tabela, estatisticas):
    """Salva a tabela e as estatisticas em um arquivo TXT."""
    os.makedirs(os.path.dirname(ARQUIVO_RESULTADO), exist_ok=True)

    cabecalho_arquivo = (
        "Teste A/B - Soma Recursiva vs Soma Iterativa\n"
        "Data de execucao: {}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"))
        + "Repeticoes: {} | Tamanho da lista: {}\n".format(REPETICOES, TAMANHO_LISTA)
        + "=" * 60 + "\n\n"
    )

    with open(ARQUIVO_RESULTADO, "w", encoding="utf-8") as arquivo:
        arquivo.write(cabecalho_arquivo)
        arquivo.write(tabela)
        arquivo.write("\n")
        arquivo.write(estatisticas)
        arquivo.write("\n")

    print("\n>> Resultados exportados para: {}".format(ARQUIVO_RESULTADO))


# ---------------------------------------------------------------------------
# Ponto de entrada
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("  Teste A/B - Soma Recursiva vs Soma Iterativa")
    print("=" * 60)
    print("  Tamanho da lista : {} numeros".format(TAMANHO_LISTA))
    print("  Repeticoes       : {}".format(REPETICOES))
    print("  Limite recursao  : {}".format(sys.getrecursionlimit()))
    print("=" * 60)
    print("\n  Executando experimento...\n")

    registros = executar_experimento()
    tabela = formatar_tabela(registros)
    estatisticas = calcular_estatisticas(registros)

    print(tabela)
    print(estatisticas)

    exportar_resultados(tabela, estatisticas)


if __name__ == "__main__":
    main()
