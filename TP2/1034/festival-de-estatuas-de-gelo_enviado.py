if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        linha_com_n_e_m = input().split()
        N = int(linha_com_n_e_m[0])
        M = int(linha_com_n_e_m[1])

        a = [int(x) for x in reversed(input().split())]

        lista_solucao = [0] * (M+1)
        melhor_candidato = 0

        for j in range(1, M+1):
            melhor_candidato = melhor_candidato + 1

            for bloco_atual in a[:-1]:
                if bloco_atual > j:
                    continue

                if bloco_atual == j:
                    melhor_candidato = 1
                    break

                com_bloco_atual = lista_solucao[j - bloco_atual] + 1

                if com_bloco_atual < melhor_candidato:
                    melhor_candidato = com_bloco_atual

            lista_solucao[j] = melhor_candidato

        print(lista_solucao[M])
