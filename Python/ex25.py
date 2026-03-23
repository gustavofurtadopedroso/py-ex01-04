produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
quantidade = int(input("Digite a quantidade do produto: "))

total = preco * quantidade

if total > 50:
    desconto= total * 0.10
    total_final = total - desconto
    print("Desconto de 10% aplicado!")
else:
    total_final = total = total
    print("Nenhum desconto aplicado.")

print(f"Produto: {produto}")
print(f"Total a pagar: R$ {total_final:.2f}")