class aluno:
    def __init__(self, nome):
        self.nome = nome
        print('O aluno se chama', self.nome)

    def pesoAluno(self, peso):
        self.peso = peso
        if(self.peso >= 80):
            print('Aluno acima do peso', self.peso)
        elif(self.peso >= 60):
            print('peso normal!')
        else:
            print('Aluno abaixo do peso!')

    def dietaAluno(self):
        self.msg = 'Tudo ok!'
        if(self.peso < 60):
            self.msg = 'Almentar a alimentação'
        if(self.peso >= 61):
            self.msg = 'Diminuir a alimentação'

    def dadosAluno(self):
        print('\n O aluno', self.nome, 'Está com', self.peso, 'kg')
        print(self.dietaAluno())

nomeDoAluno = input('Digite o nome do aluno: ')
aluno1 = aluno(nomeDoAluno)

peso = int(input('\nQual o peso do aluno: '))
aluno1.pesoAluno(peso)

aluno1.dadosAluno()






