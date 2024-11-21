if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        linha_com_a_b = input().split()
        A = int(linha_com_a_b[0])
        B = int(linha_com_a_b[1])

        lista_nivel: list[int] = [0]
        lista_numero: list[int] = [A]
        lista_numeros_ja_enfileirados: set[int] = {A}

        while lista_numero[0] != B:
            nivel_atual = lista_nivel.pop(0)
            numero_atual = lista_numero.pop(0)

            proximo_numero = numero_atual + 1
            if proximo_numero not in lista_numeros_ja_enfileirados:
                lista_nivel.append(nivel_atual + 1)
                lista_numero.append(proximo_numero)
                lista_numeros_ja_enfileirados.add(proximo_numero)

            proximo_numero = int(str(numero_atual)[::-1])
            if proximo_numero not in lista_numeros_ja_enfileirados:
                lista_nivel.append(nivel_atual + 1)
                lista_numero.append(proximo_numero)
                lista_numeros_ja_enfileirados.add(proximo_numero)

        print(lista_nivel[0])