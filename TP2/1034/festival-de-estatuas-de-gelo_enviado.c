#include <stdio.h>
#include <stdlib.h>

int main() {
    int T;
    scanf("%d", &T);

    for (int _ = 0; _ < T; _++) {
        int N, M;
        scanf("%d %d", &N, &M);

        int *a = (int *)malloc(N * sizeof(int));
        for (int i = N - 1; i >= 0; i--) {
            scanf("%d", &a[i]);
        }

        int *lista_solucao = (int *)calloc(M + 1, sizeof(int));
        int melhor_candidato = 0;

        for (int j = 1; j <= M; j++) {
            melhor_candidato = melhor_candidato + 1;

            for (int k = 0; k < N - 1; k++) {
                int bloco_atual = a[k];
                if (bloco_atual > j) {
                    continue;
                }

                if (bloco_atual == j) {
                    melhor_candidato = 1;
                    break;
                }

                int com_bloco_atual = lista_solucao[j - bloco_atual] + 1;

                if (com_bloco_atual < melhor_candidato) {
                    melhor_candidato = com_bloco_atual;
                }
            }

            lista_solucao[j] = melhor_candidato;
        }

        printf("%d\n", lista_solucao[M]);

        free(a);
        free(lista_solucao);
    }

    return 0;
}