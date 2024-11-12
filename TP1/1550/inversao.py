"""
Pedro é um garoto curioso que gostava de eletrônica. Certo dia, o menino estava mexendo no laboratório de sua escola e encontrou uma caixa cheia de pequenos aparelhos eletrônicos feitos por outros alunos em anos anteriores.

Dentro dessa caixa havia um aparelho que possuía apenas um visor e dois botões. Esse visor apresentava um número inteiro. Mexendo nos botões, Pedro descobriu para que servia cada um deles. O primeiro botão adicionava uma unidade ao número no visor. O segundo botão invertia os dígitos do número, por exemplo, 123 invertido resulta em 321 e 150 invertido resulta em 51 (ignora-se os zeros a esquerda).

Inicialmente, o visor apresentava o número A. Após a descoberta da função dos botões, Pedro quer saber como fazer o número do visor mudar de A para um número maior igual a B. O seu trabalho nesse problema é ajudar Pedro a descobrir qual é o número mínimo de apertos de botão para que o número no visor passe a ser igual a B.

Entrada
A entrada é iniciada por um inteiro T, 0 < T ≤ 500, que indica a quantidade de casos de teste a ser processados. Segue-se T linhas cada uma contendo dois inteiros A e B, 0 < A < B < 10000, indicando respectivamente o número inicial no visor e o número que deve ser mostrado no visor depois de apertar os botões.

Saída
Para cada caso de teste, o programa deve imprimir um inteiro indicando o número mínimo de apertos de botão para que o número do visor passe de A para B.
"""

class Aparelho:
    A: int
    B: int
    numero_atual: int
    numero_de_botoes_apertados: int

    def __init__(self, a: int, b: int) -> None:
        self.A = a
        self.B = b

        self.numero_de_botoes_apertados = 0
        self.numero_atual = a

    def _incrementa(self) -> None:
        self.numero_de_botoes_apertados += 1
        self.numero_atual += 1

    def _inverte(self) -> None:
        self.numero_de_botoes_apertados += 1
        numero_str = str(self.numero_atual)
        numero_invertido_str = numero_str[::-1]
        self.numero_atual = int(numero_invertido_str)

    def __str__(self) -> str:
        _s = f"A: {self.A}\n"
        _s += f"B: {self.B}\n"
        _s += f"numero_de_botoes_apertados: {self.numero_de_botoes_apertados}\n"
        _s += f"numero_atual: {self.numero_atual}\n"
        return _s

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        linha_com_a_b = input().split()
        A = int(linha_com_a_b[0])
        B = int(linha_com_a_b[1])

        aparelho = Aparelho(A, B)
        print(aparelho)