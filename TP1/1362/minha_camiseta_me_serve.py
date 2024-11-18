"""
Nosso amigo Victor é instrutor em um programa ambiental voluntário. O chefe de Victor pediu para ele distribuir N camisetas para M voluntários (N é múltiplo de seis, e N ≥ M). Cada voluntário deve receber exatamente uma camiseta (se N ≠ M, algumas camisetas podem sobrar). Há o mesmo número de camisetas disponíveis para cada tamanho de camiseta possível: XXL, XL, L, M, S e XS (siglas em inglês para P, M, G, etc.). Victor tem um pequeno problema: apenas dois tamanhos de camisetas servem para cada voluntário.

Você deve escrever um programa que decide se Victor pode distribuir as camisetas de tal forma que todo voluntário tenha uma camiseta que lhe serve.

Entrada
A primeira linha da entrada contém o número de casos de teste.

Para cada caso de teste, há uma linha contendo os números N e M. O número N é múltiplo de seis, 1 ≤ N ≤ 36, e indica o número total de camisetas disponíveis. O número M, 1 ≤ M ≤ 30, indica o número de voluntários, com N ≥ M. As próximas M linhas descrevem os voluntários, um por linha. Cada linha contém dois tamanhos de camiseta possíveis (XXL, XL, L, M, S ou XS) separados por um espaço, indicando quais tamanhos servem para o voluntário.

Saída
Para cada caso teste, imprima uma linha contendo YES se existe pelo menos uma maneira de distribuir as camisetas de tal forma que todo voluntário tenha uma camiseta que lhe serve, ou NO caso contrário.
"""
from enum import Enum

class Tamanho(Enum):
    XS = 0
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5

class DistribuicaoDeCamisetas:
    N: int
    M: int
    camisetas_disponiveis: list[int]

    def __init__(self, n: int, m: int) -> None:
        self.N = n
        self.M = m

        x = int(n/6)
        self.camisetas_disponiveis = [x, x, x, x, x, x]
        self.camisetas_pedidas = [0, 0, 0, 0, 0, 0]

    def insere_voluntario(self, a: Tamanho, b: Tamanho) -> None:
        self.camisetas_pedidas[a.value] += 1
        self.camisetas_pedidas[b.value] += 1

    def verifica_disponibilidade(self) -> bool:
        # TODO: Implementar lógica de verificar e mais d um tamanho está com rquisição maior que disponibilidade
        pass

    def __str__(self) -> str: # todo: modificar esta função
        _s = f"A: {self.A}\n"
        _s += f"B: {self.B}\n"
        _s += f"numero_de_botoes_apertados: {self.numero_de_botoes_apertados}\n"
        _s += f"numero_atual: {self.numero_atual}\n"
        return _s


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        linha_com_n_m = input().split()
        N = int(linha_com_n_m[0])
        M = int(linha_com_n_m[1])

        d = DistribuicaoDeCamisetas(N, M)

        linhas_de_voluntarios = [(int(x) for x in input().split()) for _ in range(0, M)]
        for A, B in linhas_de_voluntarios:
            d.insere_voluntario(A, B)

        resp = 'YES' if d.verifica_disponibilidade() else 'NO'
        print(resp)