from datetime import date
anoAtual = date.today().year
nasc = int(input("ano de nascimento: "))
idade = anoAtual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, anoAtual))
if idade == 18:
    print("Você tem que se alistar")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    ano = anoAtual + saldo
    print("Seu alistamento será em {}.".format(ano))
elif idade > 18:
    saldo = idade - 18
    print("Você deveria se alistar há {} anos.".format(saldo))
    ano = anoAtual - saldo
    print("Seu alistamento foi em {}.".format(ano))
        
