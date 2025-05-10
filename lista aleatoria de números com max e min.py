from random import randint

lista = [randint(1, 100) for _ in range(20)]  # Lista aleatória de 20 números

maximo = max(lista)
minimo = min(lista)

print(f"Lista: {lista}")
print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")

