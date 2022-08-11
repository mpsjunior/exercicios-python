class Teste():
    def __init__(self, valor):
        self.x = valor

    def getValor(self):
        return self.x

    def setValor(self, v):
        self.x

teste = Teste (10)
print("Valor do objeto:",teste.getValor())

val = int(input("digite um valor numérico: "))
teste.setValor(val)
print("Valor do objeto após atribuição:",teste.getValor())


