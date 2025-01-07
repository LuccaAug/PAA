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

        numero = [int(digito) for digito in input()]
        numero_final = []
        remocoes_restantes = D

        # Percorre cada dígito (dos mais significativos pros menos significativos)
        for digito in numero:
            # Se ainda puder remover dígitos, remove caso o atual da resposta seja menor que o atual candidato
            while (remocoes_restantes > 0) and (len(numero_final) > 0) and (digito > numero_final[-1]):
                numero_final.pop()
                remocoes_restantes -= 1

            # Insere o atual candidato na resposta
            numero_final.append(digito)

        # Caso não tenha removido tudo remove os dígitos menos significativos
        if remocoes_restantes > 0:
            numero_final = numero_final[:-remocoes_restantes]

        # Converte a resposta para string e imprime
        numero_final_str = [str(d) for d in numero_final]
        print(''.join(numero_final_str))
