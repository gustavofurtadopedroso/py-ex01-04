# Solicitando dados do usuário
name = input("digite seu nome: ") 
age = int(input("digite sua idade: "))

#Mostrando os dados coletados
print(f"bem vindo {name} , voce tem {age} anos")
if age == 18:
    print("Olá, você tem 18 anos! Parabéns por alcançar a maioridade!")
else:
    print("Você não acabou de fazer 18 anos, mas tudo bem, aproveite sua juventude!")