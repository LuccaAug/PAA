
class Entrega:
    quantidade_de_pizzas: int
    tempo_de_entrega: int

    def __init__(self, quantidade_de_pizzas: int = 0, tempo_de_entrega: int = 0):
        self.quantidade_de_pizzas = quantidade_de_pizzas
        self.tempo_de_entrega = tempo_de_entrega

    def __add__(self, other):
        return Entrega(
            self.quantidade_de_pizzas + other.quantidade_de_pizzas,
            self.tempo_de_entrega + other.tempo_de_entrega
        )


if __name__ == '__main__':
    while True:
        N = int(input())
        if N == 0:
            break

        P = int(input())

        possiveis_entregas = []
        for _ in range(N):
            linha = input().split()
            tempo = int(linha[0])
            quantidade = int(linha[1])
            possiveis_entregas.append(Entrega(quantidade, tempo))

        matriz = [[Entrega() for _ in range(P + 1)] for _ in range(N + 1)]

        for i in range(1, N + 1):
            for j in range(P + 1):
                entrega_atual = possiveis_entregas[i - 1]
                if entrega_atual.quantidade_de_pizzas > j:
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    sem_incluir = matriz[i - 1][j]
                    com_incluir = matriz[i - 1][j - entrega_atual.quantidade_de_pizzas] + entrega_atual

                    if com_incluir.tempo_de_entrega > sem_incluir.tempo_de_entrega:
                        matriz[i][j] = com_incluir
                    else:
                        matriz[i][j] = sem_incluir

        resultado = matriz[N][P]
        print(f"{resultado.tempo_de_entrega} min.")
