"""
Uma das forças motoras que auxiliaram no desenvolvimento da região sul do Brasil foi a força equina. Talvez por isso a região tem uma cultura de criação de cavalos de raça, sendo possível encontrar fazendas de cavalos tanto no estado do Paraná, quanto em Santa Catarina e no Rio Grande do Sul.

Uma dessas fazendas pretende realizar um mapeamento genealógico de seus animais e melhorar a característica genética das reproduções. A ideia do veterinário responsável é não cruzar animais que tenham relação de parentesco, ou seja, antes de cruzar dois animais, os veterinários pretendem verificar se eles tem algum ascendente em comum. Se este for o caso, os animais não deverão formar um casal para reprodução. Para realizar tal mapeamento, o veterinário solicitou um programa que, dada uma lista de parentesco e um par de animais, decida se eles têm parentesco ou não.

Imagem: https://resources.beecrowd.com/gallery/images/contests/UOJ_3682.png

Na figura exemplo, Alice e Bob geraram dois filhos, Gina e Bonnie. Ainda, um teste entre Elis e Ped deve retornar verdadeiro (existe parentesco) e entre Zec e Perf deve retornar falso (não existe parentesco).

Entrada
A primeira linha da entrada possui três números inteiros N (3 ≤ N ≤ 15), C (0 < C ≤ N) e T (0 < T ≤ N*(N-1)), que representam, respectivamente, o número de animais, o número de relações de parentesco conhecidas e o número de casos de teste. Em seguida, são fornecidas as C relações de parentesco com os dois nomes dos pais e o respectivo filho gerado. Depois dos cruzamentos são fornecidos os T casos de teste, cada um composto pelos nomes dos dois animais que se pretende cruzar. Cada nome de animal é composto por até 10 letras do alfabeto português (26 letras) e todos os nomes são separados por um único espaço entre si.

Saída
Seu programa deve imprimir, para cada caso de teste, "verdadeiro" se existir parentesco entre os animais e "falso" se não existir.
"""

class ReproducaoControlada:
    label_grafo: dict
    grafo: list
    cavalos_orfaos: set # Raízes do grafo, armazenados para facilitar a busca

    def __init__(self, n: int) -> None:
        self.label_grafo = dict()
        self.grafo = [list() for _ in range(n)]
        self.cavalos_orfaos = set(range(n))

    def _insere_cavalo(self, cavalo, cavalo_filho=None) -> None:
        if cavalo in self.label_grafo:
            index = self.label_grafo[cavalo]
        else:
            index = len(self.label_grafo)
            self.label_grafo[cavalo] = index
            
        if cavalo_filho:
            index_filho = self.label_grafo[cavalo_filho]
            self.grafo[index].append(index_filho)

        else: # Ele é filho, então o remove da lista de órfãos
            self.cavalos_orfaos.remove(index)
    
    def insere_cavalos(self, lista_de_parentescos) -> None:
        for pai, mae, filho in lista_de_parentescos:
            self._insere_cavalo(filho)
            self._insere_cavalo(pai, filho)
            self._insere_cavalo(mae, filho)

    def _pega_parentescos(self, cavalo) -> list:
        parentes = list()
        index_cavalo = self.label_grafo[cavalo]

        for raiz in self.cavalos_orfaos:
            parentes_cavalo_raiz = []
            nos_a_serem_percorridos = [raiz]

            while len(nos_a_serem_percorridos) > 0:
                no_atual = nos_a_serem_percorridos.pop(0)
                nos_a_serem_percorridos.extend(self.grafo[no_atual])
                parentes_cavalo_raiz.append(no_atual)

            label_invertido = {v: k for k, v in self.label_grafo.items()}
            print(f"Cavalo {label_invertido[raiz]}: {[label_invertido[x] for x in parentes_cavalo_raiz]}")

            if index_cavalo in parentes_cavalo_raiz:
                parentes.extend(parentes_cavalo_raiz)

        return parentes
    
    def _verifica_parentesco(self, cavalo_a, cavalo_b) -> bool:
        parentes_de_a = self._pega_parentescos(cavalo_a)
        index_cavalo_b = self.label_grafo[cavalo_b]

        if index_cavalo_b in parentes_de_a:
            return True
        else:
            return False
    
    def executa_testes(self, lista_de_testes) -> None:
        for cavalo_a, cavalo_b in lista_de_testes:
            resultado_teste = self._verifica_parentesco(cavalo_a, cavalo_b)
            print('verdadeiro' if resultado_teste else 'falso')


def print_grafo(g: ReproducaoControlada) -> None:
    if len(g.label_grafo) == 0:
        print(f"Grafo vazio!")
        return

    label_invertido = {v: k for k, v in g.label_grafo.items()}
    print(f"Labels: {g.label_grafo}")
    print(f"Cavalos Órfãos: {g.cavalos_orfaos}")
    print(f"Grafo:")
    for i, l in enumerate(g.grafo):
        print(f"\t{label_invertido[i]}: {[label_invertido[x] for x in l]}")

if __name__ == '__main__':
    primeira_linha_de_entrada = input().split()
    N = int(primeira_linha_de_entrada[0])
    C = int(primeira_linha_de_entrada[1])
    T = int(primeira_linha_de_entrada[2])

    r = ReproducaoControlada(N)
    # print_grafo(r)

    linhas_de_parentesco = [input().split() for _ in range(0, C)]
    r.insere_cavalos(linhas_de_parentesco)
    # print_grafo(r)

    linhas_de_teste = [input().split() for _ in range(0, T)]
    r.executa_testes(linhas_de_teste)
    # print_grafo(r)