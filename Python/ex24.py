produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade do produto: "))

total = preco * quantidade

print(f"Produto: {produto}")
print(f"Quantidade:  R$ {preco:.2f}")
print(f"Total a pagar: R$ {total:.2f}")