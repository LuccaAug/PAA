"""
Livrolândia é um país que, como o nome já diz, preza pela leitura. Nesta cidade há uma regra universal: toda cidade do país deve ter acesso a bibliotecas. Todos os presidentes que passaram por Livrolândia conseguiram manter esta regra.

Roci é o atual presidente, e fez questão de dar manutenção a todas as bibliotecas do país, além de manter a boa qualidade das estradas entre as cidades, para que cidades que não tem biblioteca, consigam acesso a cidades vizinhas que tenham.

Infelizmente, Roci é muito azarado e, logo em seu mandato, um tornado destruiu todas as bibliotecas e obstruiu todas as estradas de Livrolândia. Agora, o presidente terá que bolar um plano para reconstruir o país, seguindo sua regra universal e com o menor custo possível para as obras.

Livrolândia tem N cidades numeradas de 1 a N. As cidades são conectadas por M estradas bidirecionadas. Uma cidade tem acesso a um biblioteca se:

Esta cidade tem uma biblioteca;
É possível, a partir desta cidade, viajar para uma cidade que contém uma biblioteca.
            O custo para reparar uma estrada é E tolkiens (tolkiens é a moeda de Livrolândia) e o custo para construir uma biblioteca é B tolkiens.

            Dado o mapa de Livrolândia e os custos de reparo e construção, escreva um programa que retorne o custo mínimo para reconstruir o país, seguindo a regra universal, e assim, salve Roci.

Entrada
A primeira linha da entrada contém um inteiro T indicando o número de possíveis mapas.

A segunda linha da entrada contém 4 inteiros, N, M, B e E, número de cidades, número de estradas, custo para construir uma biblioteca e o custo para construir uma estrada, respectivamente.

Depois há M linhas indicando as estradas obstruídas, em que cada uma há dois inteiros X e Y, indicando que há uma estrada que liga a cidade X à cidade Y.

Limites:
1 <= T <= 10;
1 <= N <= 10^5;
0 <= M <= min(10^5, (N*(N-1))/2);
1 <=  B, E <= 10^5;
1 <= X,Y <= N.

Saída
Para cada possível mapa, indique o custo mínimo para reconstruir o país.
"""

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

    def __str__(self) -> str:
        _s = f"Grafo:\n"
        for i, l in enumerate(self.grafo):
            _s += f"\t{i}: {l}\n"
        return _s

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
        print(l)

        for _ in range(M):
            linha_com_variaveis_da_estrada = input().split()
            X = int(linha_com_variaveis_da_estrada[0])
            Y = int(linha_com_variaveis_da_estrada[1])
            l.insere_aresta(X, Y)

        print(l)
        print(l.calcula_custo_minimo())