class Cidade:
    N: int
    c: list

    def __init__(self, n: int) -> None:
        self.N = n
        self.grafo = [list() for _ in range(n)]

    def insere_rua(self, a: int, b: int, mao_dupla: bool) -> None:
        a -= 1
        b -= 1

        self.grafo[a].append(b)

        if mao_dupla:
            self.grafo[b].append(a)
    
    def verifica_conexidade(self) -> bool:
        def _DFS(v_inicial: int, v_visitados: list, v: int) -> [bool | list[int]]:
            v_visitados[v] = 1
            for u in self.grafo[v]:
                if u < v_inicial:
                    return True
                if not v_visitados[u]:
                    v_visitados = _DFS(v_inicial, v_visitados, u)
                    if isinstance(v_visitados, bool):
                        return True
            return v_visitados

        for vertice in range(self.N):
            vertices_visitados = _DFS(vertice, [0] * self.N, vertice)
            if isinstance(vertices_visitados, bool):
                continue
            if sum(vertices_visitados) < self.N:
                return False

        return True

if __name__ == '__main__':
    while True:
        linha_com_n_m = input().split()
        N = int(linha_com_n_m[0])
        M = int(linha_com_n_m[1])

        if N == 0 and M == 0:
            break

        c = Cidade(N)

        linhas_de_arestas = [(int(x) for x in input().split()) for _ in range(0, M)]
        for A, B, sentidos in linhas_de_arestas:
            c.insere_rua(A, B, (sentidos == 2))

        G = int(c.verifica_conexidade())
        print(G)