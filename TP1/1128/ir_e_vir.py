"""
Numa certa cidade há N intersecções ligadas por ruas de mão única e ruas com mão dupla de direcão. É uma cidade moderna, de forma que muitas ruas atravessam túneis ou têm viadutos. Evidentemente é necessário que se possa viajar entre quaisquer duas intersecções, isto é, dadas duas intersecções V e W, deve ser possível viajar de V para W e de W para V.

Sua tarefa é escrever um programa que leia a descrição do sistema de tráfego de uma cidade e determine se o requisito de conexidade é satisfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros N e M, separados por um espaço em branco, indicando respectivamente o número de intersecções (2 ≤ N ≤ 2000) e o número de ruas (2 ≤ M ≤ N(N−1)/2). O caso de teste tem ainda mais M linhas, que contêm, cada uma, uma descrição de cada uma das M ruas. A descrição consiste de três inteiros V, W e P, separados por um espaço em branco, onde V e W são identificadores distintos de intersecções (1 ≤ V, W ≤ N , V ≠ W ) e P pode ser 1 ou 2; se P = 1 então a rua é de mão única, e vai de V para W; se P = 2 então a rua é de mão dupla, liga V e W. Não existe duas ruas ligando as mesmas intersecções.

O ultimo caso de teste é seguido por uma linha que contém apenas dois números zero separados por um espaço em branco.

Saída
Para cada caso de teste seu programa deve imprimir uma linha contendo um inteiro G, onde G é igual a 1 se o requisito de conexidade está satisfeito, ou G é igual a 0, caso contrário.
"""

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
            # print(vertice, ': ', vertices_visitados)
            if isinstance(vertices_visitados, bool):
                continue
            if sum(vertices_visitados) < self.N:
                return False

        return True

    def __str__(self) -> str:
        _s = f"Grafo:\n"
        for i, l in enumerate(self.grafo):
            _s += f"\t{i}: {l}\n"
        return _s

if __name__ == '__main__':
    while True:
        linha_com_n_m = input().split()
        N = int(linha_com_n_m[0])
        M = int(linha_com_n_m[1])

        if N == 0 and M == 0:
            break

        c = Cidade(N)
        # print(c)

        linhas_de_arestas = [(int(x) for x in input().split()) for _ in range(0, M)]
        for A, B, sentidos in linhas_de_arestas:
            c.insere_rua(A, B, (sentidos == 2))

        # print(c)
        G = int(c.verifica_conexidade())
        print(G)