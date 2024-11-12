"""
Pedro é um garoto curioso que gostava de eletrônica. Certo dia, o menino estava mexendo no laboratório de sua escola e encontrou uma caixa cheia de pequenos aparelhos eletrônicos feitos por outros alunos em anos anteriores.

Dentro dessa caixa havia um aparelho que possuía apenas um visor e dois botões. Esse visor apresentava um número inteiro. Mexendo nos botões, Pedro descobriu para que servia cada um deles. O primeiro botão adicionava uma unidade ao número no visor. O segundo botão invertia os dígitos do número, por exemplo, 123 invertido resulta em 321 e 150 invertido resulta em 51 (ignora-se os zeros a esquerda).

Inicialmente, o visor apresentava o número A. Após a descoberta da função dos botões, Pedro quer saber como fazer o número do visor mudar de A para um número maior igual a B. O seu trabalho nesse problema é ajudar Pedro a descobrir qual é o número mínimo de apertos de botão para que o número no visor passe a ser igual a B.

Entrada
A entrada é iniciada por um inteiro T, 0 < T ≤ 500, que indica a quantidade de casos de teste a ser processados. Segue-se T linhas cada uma contendo dois inteiros A e B, 0 < A < B < 10000, indicando respectivamente o número inicial no visor e o número que deve ser mostrado no visor depois de apertar os botões.

Saída
Para cada caso de teste, o programa deve imprimir um inteiro indicando o número mínimo de apertos de botão para que o número do visor passe de A para B.
"""


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        linha_com_a_b = input().split()
        A = int(linha_com_a_b[0])
        B = int(linha_com_a_b[1])