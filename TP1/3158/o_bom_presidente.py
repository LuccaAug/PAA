# -*- coding: utf-8 -*-

class Grafo:
    N: int
    grafo: list

    def __init__(self, n: int) -> None:
        self.N = n
        self.grafo = [list() for _ in range(n)]

    def _insere_aresta(self, fonte, destino) -> None:
        # Força os vértices iniciados em 1 à iniciarem em 0
        fonte -= 1
        destino -= 1

        self.grafo[fonte].append(destino)

    def insere_arestas(self, lista_de_arestas: list) -> None:
        for A, B, sentidos in lista_de_arestas:
            self._insere_aresta(A, B)

            mao_dupla = sentidos == 2
            if mao_dupla:
                self._insere_aresta(B, A)
    
    def verifica_conexidade(self) -> bool:
        # TODO: lógica de conexidade

        return True

    def print_grafo(self) -> None:
        print(f"Grafo:")
        for i, l in enumerate(self.grafo):
            print(f"\t{i}: {self.grafo[i]}")

if __name__ == '__main__':
    while True:
        linha_com_n_m = input().split()
        N = int(linha_com_n_m[0])
        M = int(linha_com_n_m[1])

        if N == 0 and M == 0:
            break

        grafo = Grafo(N)
        # print_grafo(r)

        linhas_de_arestas = [(int(x) for x in input().split()) for _ in range(0, M)]
        grafo.insere_arestas(linhas_de_arestas)
        grafo.print_grafo()

        resultado_bool = grafo.verifica_conexidade()
        resultado_int = '1' if resultado_bool else '0'
        print(resultado_int)