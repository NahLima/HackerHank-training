
# explicação base para o exercicio 07

from math import factorial
listando = []

while True:
    numeros = int(input('insira a baixo seus números: '))
    if numeros == 10:
        break
    else:
        listando.append(numeros)
print(" ".join(map(str, reversed(listando))))


# -------------------------------------------------------- #
# dict agenda telefonica


phoneBook = {}


def obter_dados():
    for i in range(3):
        data = input(">>> ").split(" ")
        phoneBook[data[0]] = data[1]
    return phoneBook


obter_dados()

print(phoneBook)

while True:
    try:
        data = input(">>> ")
        if data in phoneBook:
            print(data+"="+phoneBook[data])
        elif data == "":
            print("digite um nome: ")
        else:
            print("Not found")
    except EOFError:
        break

# ----------------------------------------------------
# fatorial
# ex: 4! = 4 · 3 · 2 · 1 = 24


numero = int(input(">>> "))


def fatorial(numero):
    return factorial(numero)


print(fatorial(numero))


# fatorial

def main():
    n = int(input("Digite o valor de n: "))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    print("O valor de %d! eh =" % n, fat)


# -----
main()


# ---------------------------------------------------
# binario --> pegando a qtd repetidas de 1
num = int(input(">>> "))


def binario(num):
    numero = bin(int(num))  # metodo bin()
    return numero


binario(num)

print(binario(num))

count = 0
while num:
    num &= num << 1  # bit a bit indo para a esquerda
    count += 1

print(count)

# ------------------------------------------------------
# queue tasks exercicio 18 
string = "racecar"
if string == string[::-1]:
    print(string + " is a palindrome")
else:
    print(string + " is NOT a palindrome")
