if __name__ == '__main__':
    X = int(input())
    entradas = [int(input()) for _ in range(X)]

    maior_fibonacci = max(entradas)

    fib = (maior_fibonacci+1) * [0]
    calls = (maior_fibonacci+1) * [0]

    for i in range(maior_fibonacci+1):
        if i == 0:
            fib[i] = 0
            calls[i] = 1

        elif i == 1:
            fib[i] = 1
            calls[i] = 1

        else:
            fib[i] = fib[i-1] + fib[i-2]
            calls[i] = calls[i-1] + calls[i-2] + 1

    for n in entradas:
        result = fib[n]
        num_calls = calls[n] - 1
        print(f"fib({n}) = {num_calls} calls = {result}")
