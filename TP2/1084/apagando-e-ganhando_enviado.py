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

        for digito in numero:
            while (remocoes_restantes > 0) and (len(numero_final) > 0) and (digito > numero_final[-1]):
                numero_final.pop()
                remocoes_restantes -= 1

            numero_final.append(digito)

        if remocoes_restantes > 0:
            numero_final = numero_final[:-remocoes_restantes]

        numero_final_str = [str(d) for d in numero_final]
        print(''.join(numero_final_str))