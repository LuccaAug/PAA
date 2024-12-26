"""
Juliano é fã do programa de auditório Apagando e Ganhando, um programa no qual os participantes são selecionados através de um sorteio e recebem prêmios em dinheiro por participarem.

No programa, o apresentador escreve um número de N dígitos em uma lousa. O participante então deve apagar exatamente D dígitos do número que está na lousa; o número formado pelos dígitos que restaram é então o prêmio do participante.

Juliano finalmente foi selecionado para participar do programa, e pediu que você escrevesse um programa que, dados o número que o apresentador escreveu na lousa, e quantos dígitos Juliano tem que apagar, determina o valor do maior prêmio que Juliano pode ganhar.

Entrada
A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém dois inteiros N e D (1 ≤ D < N ≤ 105), indicando a quantidade de dígitos do número que o apresentador escreveu na lousa e quantos dígitos devem ser apagados. A linha seguinte contém o número escrito pelo apresentador, que não contém zeros à esquerda.

O final da entrada é indicado por uma linha que contém apenas dois zeros, separados por um espaço em branco.

Saída
Para cada caso de teste da entrada seu programa deve imprimir uma única linha na saída, contendo o maior prêmio que Juliano pode ganhar.
"""

if __name__ == '__main__':
    while True:
        linha_com_n_d = input().split()
        N = int(linha_com_n_d[0])
        D = int(linha_com_n_d[1])

        if N == 0 and D == 0:
            break

        numero = [int(d) for d in input()]
        i = 0

        # Enquanto tiver dígito para retirar no meio do número ou se chegar ao final da "ordenação"
        while D != 0 and i < (N-1):
            # print(f"i={i}  -  D={D}")
            possiveis_maiores = numero[i:i+D+1]             # Seleciona o range para escolher o maior número
            maior_digito = max(possiveis_maiores)           # Seleciona o maior número
            indice = possiveis_maiores.index(maior_digito)  # Descobre o menor índice deste maior número
            numero = numero[:i] + numero[i+indice:]         # Remove os dígitos entre os já ordenados e o maior dígito
            D -= indice                                     # Remove o número de dígitos apagados da variável D
            i += 1                                          # Soma um no índice que está sendo analisado

        # Caso tenha parado por chegar ao fim da ordenação, deve remover os dígitos faltantes da direita
        if D > 0:
            numero = numero[:-D]

        numero = [str(d) for d in numero]
        print(''.join(numero))
