n = int(input("Digite a quantidade de sequências: "))
cont1 = 0
cont2 = 1
if (n == 1):
   print(cont1)
   exit()
print("{} {}".format(cont1, cont2), end= " ")

for i in range(n-2):
    cont3 = cont1 + cont2
    cont1 = cont2
    cont2 = cont3 
    print("{}".format(cont3), end=" ")
    
print(" fim")