class cubo:
    def __init__(self, valor):
        self.x = valor
        print('Objeto criado!')

    def calculaCubo(self):
        cubo = self.x * self.x * self.x
        return 'cubo calculado: ' + str(cubo)

teste = cubo(10)
c = teste.calculaCubo()
print(c)

