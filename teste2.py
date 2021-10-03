arr = []
result = []


for _ in range(6):
    dados = input(">>> ")
    arr.append(list(map(int, dados)))
print(arr)


for i in range(1, 5):
    for j in range(1, 5):
        soma = sum(arr[i-1][j-1: j+2] + arr[i+1][j-1: j+2]) + arr[i][j]
        result.append(soma)
    print(arr[i-1][j-1: j+2])
    print(arr[i+1][j-1: j+2])
    print(arr[i][j])
    print(max(result))


