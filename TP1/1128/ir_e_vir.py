"""
Numa certa cidade há N intersecções ligadas por ruas de mão única e ruas com mão dupla de direcão. É uma cidade moderna, de forma que muitas ruas atravessam túneis ou têm viadutos. Evidentemente é necessário que se possa viajar entre quaisquer duas intersecções, isto é, dadas duas intersecções V e W, deve ser possível viajar de V para W e de W para V.

Sua tarefa é escrever um programa que leia a descrição do sistema de tráfego de uma cidade e determine se o requisito de conexidade é satisfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros N e M, separados por um espaço em branco, indicando respectivamente o número de intersecções (2 ≤ N ≤ 2000) e o número de ruas (2 ≤ M ≤ N(N−1)/2). O caso de teste tem ainda mais M linhas, que contêm, cada uma, uma descrição de cada uma das M ruas. A descrição consiste de três inteiros V, W e P, separados por um espaço em branco, onde V e W são identificadores distintos de intersecções (1 ≤ V, W ≤ N , V ≠ W ) e P pode ser 1 ou 2; se P = 1 então a rua é de mão única, e vai de V para W; se P = 2 então a rua é de mão dupla, liga V e W. Não existe duas ruas ligando as mesmas intersecções.

O ultimo caso de teste é seguido por uma linha que contém apenas dois números zero separados por um espaço em branco.

class Grafo:
Saída
Para cada caso de teste seu programa deve imprimir uma linha contendo um inteiro G, onde G é igual a 1 se o requisito de conexidade está satisfeito, ou G é igual a 0, caso contrário.
"""

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