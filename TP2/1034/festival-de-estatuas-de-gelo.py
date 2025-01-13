"""
Todos os anos, artistas de todo o mundo se reúnem na cidade, onde fazem esculturas de gelo gigantescas. A cidade vira uma galeria de arte ao céu aberto, uma vez que as esculturas ficam expostas na rua por semanas, sem derreter. Afinal, a temperatura média no inverno de Harbin (época em que ocorrerá a final mundial do ICPC) é de -20 graus.

O primeiro passo para fazer a escultura é montar um grande bloco de gelo da dimensão pedida pelo artista. Os blocos são recortados das geleiras de Harbin em blocos de altura e profundidade padrão e vários comprimentos diferentes. O artista pode determinar qual o comprimento que ele deseja que tenha o seu bloco de gelo para que a escultura possa começar a ser esculpida.

Os comprimentos disponíveis dos blocos são {a1; a2; ...;  aN} e o comprimento que o artista deseja é M. O bloco de comprimento 1 é muito usado, por este motivo ele sempre aparece na lista de blocos disponíveis. Sua tarefa é determinar o número mínimo de blocos tal que a soma de seus comprimentos seja M.

Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de instâncias. A primeira linha de cada instância contém dois inteiros N (1 ≤ N ≤ 25) e M (1 ≤ M ≤ 1000000) representando o número de tipos de blocos e o comprimento desejado pelo artista, respectivamente. A próxima linha contém os inteiros a1; a2; ...; aN , onde (1 ≤ ai ≤ 100) para todo i (1,2,...N) separados por espaço.

Saída
Para cada instância, imprima o número mínimo de blocos necessários para obter um bloco de comprimento M.
"""

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        linha_com_n_e_m = input().split()
        N = int(linha_com_n_e_m[0])
        M = int(linha_com_n_e_m[1])

        a = [int(x) for x in reversed(input().split())]  # Inverte a ordem pra otimizar o for
        lista_solucao = [0] * (M+1)  # Lista da programação dinâmica
        melhor_candidato = 0

        # Preenchimento da lista
        for j in range(1, M+1):
            melhor_candidato = melhor_candidato + 1

            for bloco_atual in a[:-1]:
                if bloco_atual > j:  # Não é possível incluir este pedido, segue para o próximo bloco
                    continue

                if bloco_atual == j:  # A melhor solução é apenas este bloco
                    melhor_candidato = 1
                    break  # Não precisa testar os demais blocos, ja que é a solução ideal

                com_bloco_atual = lista_solucao[j - bloco_atual] + 1

                if com_bloco_atual < melhor_candidato:
                    melhor_candidato = com_bloco_atual

            lista_solucao[j] = melhor_candidato

        #print("Lista: ", lista_solucao)

        # Melhor solução está na última posição da lista, que é igual ao tamanho do bloco fornecido na entrada
        print(lista_solucao[M])
