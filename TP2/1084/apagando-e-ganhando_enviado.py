if __name__ == '__main__':
    while True:
        linha_com_n_d = input().split()
        N = int(linha_com_n_d[0])
        D = int(linha_com_n_d[1])

        if N == 0 and D == 0:
            break

        numero = [int(d) for d in input()]
        i = 0

        while D != 0 and (i+1) <= (len(numero)-D):
            possiveis_maiores = numero[i:i+D+1]
            maior_digito = max(possiveis_maiores)
            indice = possiveis_maiores.index(maior_digito)
            numero = numero[:i] + numero[i+indice:]
            D -= indice
            i += 1

        if D > 0:
            numero = numero[:-D]

        numero = [str(d) for d in numero]
        print(''.join(numero))
