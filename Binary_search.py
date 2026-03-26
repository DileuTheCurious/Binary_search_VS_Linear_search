import time

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


def busca_linear(lista, item):
    for i, value in enumerate(lista):
        if value == item:
            return i
    return None


lista_grande = list(range(1, 1000001))  # 1 até 1 milhão

print('Test 1:', pesquisa_binaria(lista_grande, 500000))   # => 499999
print('Test 2:', pesquisa_binaria(lista_grande, 1000001))  # => None

item = int(input("Type the number to be searched: "))

inicio = time.time()
resultado = pesquisa_binaria(lista_grande, item)
fim = time.time()

if resultado is not None:
    print(f'The number {item} was found at position {resultado}')
else:
    print(f'The number {item} was not found')

tempo_ms = (fim - inicio) * 1000
print("Time of Binary Search:", round(tempo_ms, 6), "ms")

inicio = time.time()
resultado_linear = busca_linear(lista_grande, item)
fim = time.time()

print("Time of Linear Search:", round((fim - inicio) * 1000, 6), "ms")