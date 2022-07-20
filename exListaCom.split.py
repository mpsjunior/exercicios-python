valorEntrada = input("Digite o valor separado por virgula: ")
print(valorEntrada)

minhaLista = valorEntrada.split(',')

print(minhaLista)

for iten in minhaLista:
    print(f"os itens da lista são: {iten}")
    