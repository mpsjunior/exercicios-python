
variavel_1 = 0
variavel_2 = 1

while variavel_1 < 10:
    variavel_1 += 1
    variavel_2 *= 2

    if variavel_2 >= 10:
        variavel_1 = int(variavel_2 / 2)

    print(variavel_1, variavel_2)   
    
    