class Ficha:
    def __init__(self):
        self.nomes = {}
        self.notas = []

    def adiciona(self):
        opt = 0
        while True:
            nome = input("Nome: ")
            for n in range(4):
                nota = float(input(f"Nota {n}: "))
                self.notas.append(nota)
            
            self.nomes[nome] = self.notas.copy()
            self.notas.clear()

        
            opt = input("Deseja continuar? s ou n: ")
            if opt in "sS":
                continue
            else:
                self.visualiza()
                break
    
    def visualiza(self):
        print("-=-= Lista de Alunos e Notas -=-=")
        print(self.nomes.items())

        total = 0
        media = 0
        for k in self.nomes.keys():
            print(f"Nome:{k}")
            for i in range(len(self.nomes[k])):
                print(f"Nota: {i+1} : {self.nomes[k][i]:.2f}")
                total += self.nomes[k][i]
            media = total / 4
            print(f"Total: {total} - Média: {media:.2f}")
            media = 0
            total = 0
            


aluno = Ficha()
aluno.adiciona()


