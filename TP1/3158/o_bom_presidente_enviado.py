class Livrolandia:
    N: int
    M: int
    custo_biblioteca: int
    custo_estrada: int
    grafo: list

    def __init__(self, n: int, m: int, b: int, e: int) -> None:
        self.N = n
        self.M = m
        self.custo_biblioteca = b
        self.custo_estrada = e

        # Instancia o grafo sem estradas a serem reparadas (arestas com peso do preço de reparo),
        # iniciando-o com os valores de criar uma biblioteca naquele local
        self.grafo = [list() for _ in range(self.N)]

    def insere_aresta(self, a: int, b: int) -> None:
        # Força os vértices iniciados em 1 à iniciarem em 0
        a -= 1
        b -= 1

        self.grafo[a].append(b)
        self.grafo[b].append(a)

    def calcula_custo_minimo(self) -> int:
        numero_componentes_conexas = 0
        vertices_visitados = [False] * self.N

        def _DFS(v):
            vertices_visitados[v] = True
            for u in self.grafo[v]:
                if not vertices_visitados[u]:
                    _DFS(u)

        for vertice in range(self.N):
            if not vertices_visitados[vertice]:
                numero_componentes_conexas += 1
                _DFS(vertice)

        numero_arestas = self.N - numero_componentes_conexas

        return (self.custo_biblioteca * numero_componentes_conexas) + (self.custo_estrada * numero_arestas)


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        linha_com_variaveis_do_mapa = input().split()
        N = int(linha_com_variaveis_do_mapa[0])
        M = int(linha_com_variaveis_do_mapa[1])
        B = int(linha_com_variaveis_do_mapa[2])
        E = int(linha_com_variaveis_do_mapa[3])

        # Se o custo da biblioteca é menor ou igual o da estrada, não precisa manipular o grafo,
        # pois construir biblioteca em todos os locais é melhor
        if B <= E:
            print(N*B)
            for _ in range(M):
                input()
            continue

        l = Livrolandia(N, M, B, E)

        for _ in range(M):
            linha_com_variaveis_da_estrada = input().split()
            X = int(linha_com_variaveis_da_estrada[0])
            Y = int(linha_com_variaveis_da_estrada[1])
            l.insere_aresta(X, Y)

        print(l.calcula_custo_minimo())
