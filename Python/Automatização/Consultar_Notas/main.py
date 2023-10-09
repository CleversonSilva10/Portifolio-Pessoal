
class CalculoNotas():
    def __init__(self):
        print("\nBem vindo!! Feito por: Cleverson Silva")
        self.notaA = 0
        self.notaB = 0
        self.notaC = 0
        self.notaF = 0
        self.notaG = 0
        self.notaH = 0
        self.PARTIC = 0
    
    def InputNotas(self):
        self.notaA = float(input("Digite a Nota A: "))
        self.notaB = float(input("Digite a Nota B: "))
        self.notaC = float(input("Digite a Nota C: "))
        self.notaF = float(input("Digite a Nota F: "))
        self.notaG = float(input("Digite a Nota G: "))
        self.notaH = float(input("Digite a Nota H: "))
        self.PARTIC = float(input("Prova integrada: "))
    
    def menu(self):
        run = True
        while run:
            self.printMaterias()
            materia_desejada = int(input("\nEscolha qual materia deseja: "))
            if materia_desejada == 1:
                print("\nNota A - Prova    | Nota F - Prova")
                print("Nota B - Projeto    | Nota G - Projeto")
                print("Nota B - Atividade  | Nota G - Atividade\n")

                self.InputNotas()
                
                N1 = (self.notaA*5.0 + self.notaB*2.5 + self.notaC*2.5)/10.0
                N2 = (self.notaF*5.0 + self.notaG*2.5 + self.notaH*2.5)/10.0

                self.AnalisarNotas(N1, N2, self.PARTIC)
            
            elif materia_desejada == 2:
                print("\nNota A - Atividade | Nota F - Atividade")
                print("Nota B - Prova       | Nota G - Prova")
                print("Nota C - Projeto     | Nota H - Projeto\n")

                self.InputNotas()

                N1  = (self.notaA*2.5 + self.notaA*5.0 + self.notaA*2.5)/10.0    
                N2  = (self.notaF*2.5 + self.notaG*5.0 + self.notaH*2.5)/10.0

                self.AnalisarNotas(N1, N2, self.PARTIC)
            
            elif materia_desejada == 3:
                print("\nNota A - Prova    | Nota F - Prova")
                print("Nota B - Projeto    | Nota G - Projeto")
                print("Nota C - Atividade  | Nota H - Atividade\n")

                self.InputNotas()

                N1 = (self.notaA*8.0 + self.notaB*2.0 + self.notaC*1.0)/11.0    
                N2 = (self.notaF*8.0 + self.notaG*2.0 + self.notaH*1.0)/11.0

                self.AnalisarNotas(N1, N2, self.PARTIC)
            
            elif materia_desejada == 4:
                print("\n-------------------------")
                print("Não possue formula")
                print("-------------------------\n")
            
            elif materia_desejada == 5:
                print("\nNota A - Prova             | Nota F - Prova")
                print("Nota B - Atividade - Teoria  | Nota G - Projeto")
                print("Nota C - Atividade - Lab     | Nota H - Atividade - Teoria\n")

                self.InputNotas()

                N1 = (self.notaA*6.0 + self.notaB*2.0 + self.notaC*2.0)/10
                N2 = (self.notaF*4.0 + self.notaG*2.0 + self.notaH*2.0)/10

                self.AnalisarNotas(N1, N2, self.PARTIC)
            
            elif materia_desejada == 6:
                print("\nNota A - Atividade Lab  | Nota F - Atividade Lab")
                print("Nota B - Provas Cisco     | Nota G - Provas Cisco")
                print("Nota C - Prova            | Nota H - Prova\n")

                self.InputNotas()
                
                N1  = (self.notaA*2.0 + self.notaB*2.0 + self.notaC*6.0)/10.0    
                N2  = (self.notaF*2.0 + self.notaG*2.0 + self.notaH*6.0)/10.0

                self.AnalisarNotas(N1, N2, self.PARTIC)
            
            elif materia_desejada == 0:
                print("\n-------------------------")
                print("Obrigado por usar software")
                print("-------------------------\n")
                run = False

            else:
                print("\n-------------------------")
                print("Digito inválido!!")
                print("-------------------------\n")
    

    def AnalisarNotas(self, N1, N2, PARTIC):
        print(f'\nNota N1: {N1:.2f} - Nota N2: {N2:.2f}')
        MI = (N1*5.0 + N2*5.0)/10 + PARTIC
        print("--------------------------------")    
        print(f'MI: {MI:.2f}')
        if MI < 6:
            print("Abaixo da média - PF")
        else:
            print("Aprovado")
        print("--------------------------------")   

    def printMaterias(self):
        print("\nGrade 5º Semestre - CC Mackenzie")
        print("---------------------------------------")
        print('1. LINGUAGENS FORMAIS E AUTOMATOS')
        print('2. ENGENHARIA DE SOFTWARE')
        print('3. PARADIGMAS DE LING DE PROGRAMACAO')
        print('4. PRINCIPIOS DE EMPREENDEDORISMO')
        print('5. COMPUTACAO PARALELA')
        print('6. REDES DE COMPUTADORES')
        print('0. ENCERRAR PROGRAMA')
        print("---------------------------------------")

aluno = CalculoNotas()
aluno.menu()