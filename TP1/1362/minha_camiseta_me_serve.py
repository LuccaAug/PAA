"""
Nosso amigo Victor é instrutor em um programa ambiental voluntário. O chefe de Victor pediu para ele distribuir N camisetas para M voluntários (N é múltiplo de seis, e N ≥ M). Cada voluntário deve receber exatamente uma camiseta (se N ≠ M, algumas camisetas podem sobrar). Há o mesmo número de camisetas disponíveis para cada tamanho de camiseta possível: XXL, XL, L, M, S e XS (siglas em inglês para P, M, G, etc.). Victor tem um pequeno problema: apenas dois tamanhos de camisetas servem para cada voluntário.

Você deve escrever um programa que decide se Victor pode distribuir as camisetas de tal forma que todo voluntário tenha uma camiseta que lhe serve.

Entrada
A primeira linha da entrada contém o número de casos de teste.

Para cada caso de teste, há uma linha contendo os números N e M. O número N é múltiplo de seis, 1 ≤ N ≤ 36, e indica o número total de camisetas disponíveis. O número M, 1 ≤ M ≤ 30, indica o número de voluntários, com N ≥ M. As próximas M linhas descrevem os voluntários, um por linha. Cada linha contém dois tamanhos de camiseta possíveis (XXL, XL, L, M, S ou XS) separados por um espaço, indicando quais tamanhos servem para o voluntário.

Saída
Para cada caso teste, imprima uma linha contendo YES se existe pelo menos uma maneira de distribuir as camisetas de tal forma que todo voluntário tenha uma camiseta que lhe serve, ou NO caso contrário.
"""
class DistribuicaoDeCamisetas:
    N: int
    M: int
    grafo_capacidade: list[list[int]]
    grafo_residual: list[list[int]]

    def __init__(self, n: int, m: int, linhas_de_voluntarios: list[tuple[int, int]]) -> None:
        self.N = n
        self.M = m

        numero_de_vertices = 2 + 6 + m  # Fonte, sumidouro, cada tamanho, cada voluntario
        self.grafo_capacidade = [[0 for _ in range(numero_de_vertices)] for _ in range(numero_de_vertices)]

        x = int(n/6)
        for i in range(1, 7):  # Número de camisas disponíveis
            self.grafo_capacidade[0][i] = x

        for i in range(7, numero_de_vertices-1):  # Possibilidade de usar uma única camisa
            self.grafo_capacidade[i][-1] = 1

        voluntario = 7  # Primeiro vertice de voluntario
        for a, b in linhas_de_voluntarios:  # Possibilidade de usar os tamanhos
            self.grafo_capacidade[a][voluntario] = 1
            self.grafo_capacidade[b][voluntario] = 1
            voluntario +=1

    def _acha_caminho(self) -> list[tuple[int, int, int]]:
        # print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
        # print(self)
        def _DFS(v: int, vertices_visitados:list[bool], caminho: list[tuple[int, int, int]]):
            vertices_visitados[v] = True
            # print('\t V: ', v)
            # print('\t Vertices visitados: ', vertices_visitados)
            # print('\t caminho: ', caminho)
            # print()
            for u, c in enumerate(self.grafo_residual[v]):
                if c == 0:
                    continue

                if u == (len(self.grafo_residual)-1):  # É o sumidouro
                    return caminho+[(v, u, c)]

                if not vertices_visitados[u]:
                    ret = _DFS(u, vertices_visitados.copy(), caminho+[(v, u, c)])
                    if ret is not None:
                        return ret

            return None

        return _DFS(
            v=0,
            vertices_visitados=[False] * len(self.grafo_capacidade),
            caminho=[]
        )

    def _acha_capacidade_minima(self, caminho: list) -> int:
        caminho_ordenado_por_custo = sorted(caminho, key=lambda x: x[2])
        aresta_de_menor_capacidade = caminho_ordenado_por_custo[0]
        menor_capacidade = aresta_de_menor_capacidade[2]
        return menor_capacidade

    def _atualiza_grafo_residual(self, caminho: list[tuple[int, int, int]], capacidade_aumentante: int) -> None:
        for fonte, destino, _ in caminho:
            self.grafo_residual[destino][fonte] += capacidade_aumentante
            self.grafo_residual[fonte][destino] -= capacidade_aumentante

    def _fluxo_maximo(self) -> int:  # Ford-Fulkerson
        f = 0
        self.grafo_residual = self.grafo_capacidade.copy()

        caminho_aumentante = self._acha_caminho()
        # print('\tCaminho Achado: ', caminho_aumentante)
        while caminho_aumentante is not None:
            c = self._acha_capacidade_minima(caminho_aumentante)

            f += c

            self._atualiza_grafo_residual(caminho_aumentante, c)

            caminho_aumentante = self._acha_caminho()
            # print('\tCaminho Achado: ', caminho_aumentante)

        return f

    def verifica_disponibilidade(self) -> bool:
        fluxo_maximo = self._fluxo_maximo()

        if fluxo_maximo == self.M:
            return True

        return False

    def __str__(self) -> str:
        _s = f"M: {self.M}\n"
        _s += f"N: {self.N}\n"
        _s += f"Grafo:\n"
        for i, l in enumerate(self.grafo_residual):
            _s += f"\t{i}: {l}\n"
        return _s


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        linha_com_n_m = input().split()
        N = int(linha_com_n_m[0])
        M = int(linha_com_n_m[1])

        from enum import Enum
        class Tamanho(Enum):
            XS = 1
            S = 2
            M = 3
            L = 4
            XL = 5
            XXL = 6

        voluntarios:list[tuple[int, int]]  = [(Tamanho[x].value for x in input().split()) for _ in range(0, M)]

        d = DistribuicaoDeCamisetas(N, M, voluntarios)
        # print(d)

        resp = 'YES' if d.verifica_disponibilidade() else 'NO'
        print(resp)