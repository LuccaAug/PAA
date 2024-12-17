def resolve_problema_da_mochila(pesos: list[int], valores: list[int], peso_maximo: int) -> int:
    pesos_valores = [(pesos[i], valores[i]) for i in range(len(pesos))]
    pesos_valores = sorted(pesos_valores, key=lambda x: x[0])

    lista_auxiliar = [0] * (peso_maximo+1)

    for i in range(1, peso_maximo+1):
        a = lista_auxiliar[-1]
        candidatos = [a]

        for peso, valor in pesos_valores:
            if peso > i:
                continue

            b = valor + lista_auxiliar[i-peso]

            if b > a:
                candidatos.append(b)

        lista_auxiliar[i] = max(candidatos)

    return lista_auxiliar[-1]


if __name__ == '__main__':
    i = 0
    while True:
        linha_com_n_t = input().split()
        N = int(linha_com_n_t[0])
        T = int(linha_com_n_t[1])

        if N == 0 and T == 0:
            break

        duracoes = list()
        pontuacoes = list()

        for _ in range(N):
            linha_com_d_p = input().split()

            D = int(linha_com_d_p[0])
            duracoes.append(D)

            P = int(linha_com_d_p[1])
            pontuacoes.append(P)

        valor_total = resolve_problema_da_mochila(duracoes, pontuacoes, T)

        i += 1
        print(f"Instancia {i}")
        print(valor_total)
        print()