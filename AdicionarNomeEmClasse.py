class QualSeuNome:
    def __init__(self, nome):
        self.nome = nome
        print("Você se chama:",self.nome)

seuNome = input("Digite seu nome: ")
n1 = QualSeuNome(seuNome)
