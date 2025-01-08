"""
José é um motoboy e trabalha fazendo entregas para uma pizzaria. Seu salário é baseado no número de pizzas entregues. Só que esta pizzaria está com muito movimento e ele pediu auxílio a seu amigo Roberto para que o ajudasse nas entregas. Como Roberto é camarada e está sem trabalho no momento, ele concordou em pegar aqueles pedidos cujas entregas serão mais demoradas.

Assim, sempre que chegam à pizzaria, antes de partirem para novas entregas José determina a quantidade de pizzas que Roberto deverá entregar e seleciona para ele os pedidos mais demorados. Por exemplo, se há 22 pizzas para serem entregues e José determinar que Roberto entregue no máximo 10 destas pizzas (pode ser menos), estas devem estar obrigatoriamente entre os pedidos que levarão mais tempo para serem entregues. Isso é ilustrado no primeiro caso de teste, onde Roberto deverá fazer a entrega do segundo, terceiro e sexto pedido, somando 8 pizzas e 62 minutos (23 + 21 + 18). Se Roberto fosse realmente entregar 10 pizzas, ele teria que atender o segundo, terceiro e quarto pedido e isto levaria 59 minutos (23 + 21 + 16), o que não é o objetivo de José, pois levaria menos tempo do que a primeira opção, ou seja, a relação pizzas/tempo não importa muito para José (isso pode ser observado no segundo caso de teste do exemplo abaixo).

Para poder fazer a divisão do trabalho, José pediu a um amigo acadêmico em Ciência da Computação que desenvolvesse um programa que determinasse quanto tempo seu amigo Roberto irá levar para entregar estes pedidos mais demorados.

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém na primeira linha um valor inteiro N (1 ≤ N ≤ 20) que indica o número de pedidos. A linha seguinte contém um valor inteiro P (1 ≤ P ≤ 30) indicando o número máximo de pizzas que podem ser entregues por Roberto. Cada uma das próximas N linhas contém um pedido com o tempo total para ser entregue e a quantidade de pizzas do pedido, respectivamente. A final da entrada é determinado por N = 0, e não deverá ser processado.

Saída
Para cada caso de teste de entrada deve ser impresso um valor inteiro que determina o tempo que Roberto irá levar para entregar as suas pizzas seguido de um espaço em branco e do texto “min.”, conforme exemplo abaixo.
"""

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

        # Lista de entregas disponíveis
        possiveis_entregas = []
        for _ in range(N):
            linha = input().split()
            tempo = int(linha[0])
            quantidade = int(linha[1])
            possiveis_entregas.append(Entrega(quantidade, tempo))

        # Matriz de programação dinâmica
        matriz = [[Entrega() for _ in range(P + 1)] for _ in range(N + 1)]

        # Preenchendo a matriz
        for i in range(1, N + 1):
            for j in range(P + 1):
                entrega_atual = possiveis_entregas[i - 1]
                if entrega_atual.quantidade_de_pizzas > j:
                    # Não é possível incluir este pedido
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    # Decidir entre incluir ou não incluir o pedido
                    sem_incluir = matriz[i - 1][j]
                    com_incluir = matriz[i - 1][j - entrega_atual.quantidade_de_pizzas] + entrega_atual

                    # Escolhe a melhor opção em termos de tempo
                    if com_incluir.tempo_de_entrega > sem_incluir.tempo_de_entrega:
                        matriz[i][j] = com_incluir
                    else:
                        matriz[i][j] = sem_incluir

        # Melhor solução está em matriz[N][P], a última célula da matriz
        resultado = matriz[N][P]
        print(f"{resultado.tempo_de_entrega} min.")
