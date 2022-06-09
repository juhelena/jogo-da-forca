import random
import time

print("Bem vindo ao jogo da forca!")
palavras = ['limonada', 'borboleta', 'maracuja', 'piscina', 'bombom', 'biblioteca', 'rucula', 'pijama', 'xícara', 'irlanda']
dicas = ['bebida','animal', 'fruta', 'lazer', 'doce', 'lugar', 'verdura', 'roupa', 'objeto', 'país']
lista_acertos = []
lista_erros = []

erro = 0
pontos = 0
opcao = 0

def jogo():  
    global sortear
    global chute
    sortear = random.randint(0,10)
    print(f'\n\33[32mDica:\33[m {dicas[sortear]}')
    desenho()    

def tempo():
    fim = time.time() 
    tempo = fim-inicio
    return tempo

def verifica_erro():
    global erro
    global opcao
    global total
    
    while len(lista_acertos) != len(palavras[sortear]):
        chute = input("Escolha uma letra: ") 
        total = tempo()
        if opcao == 1:
            if tempo > 120:
                print("Tempo esgotado!")
                exit()
        if opcao == 2:
            if tempo > 90:
                print("Tempo esgotado!")
                exit()
        if opcao == 3:
            if tempo > 60:
                print("Tempo esgotado!")
                exit()
       
        if chute in palavras[sortear]:
            quantidade_letras = palavras[sortear].count(chute)
            for i in range(quantidade_letras):
                lista_acertos.append(chute)
        else:
            erro += 1
            lista_erros.append(chute)
            print(lista_erros)
            desenho()

        for i in palavras[sortear]:
            if i in lista_acertos:
                print(i, end=' ')
            else:
                print("_", end=' ')

        if len(lista_acertos) != len(palavras[sortear]):
            desenho()
        else:
            print("\nVocê acertou!!")
            exit()

def dificuldade():

    global inicio

    print("1-Fácil")
    print("2-Médio")
    print("3-Difícil")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        inicio = time.time()
        jogo()
    elif opcao == 2:
        inicio = time.time()
        jogo()
    elif opcao == 3:
        inicio = time.time()
        jogo()
     
def desenho():

    global erro 
    letras = len(palavras[sortear])

    if erro == 0:
        print("\n---------------")
        print("|               ")
        print("|               ")
        print("|")
        print("|")
        print("|")   
        print("_ " * letras)
        verifica_erro()

    if erro == 1:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|")
        print("|")
        print("|")
        verifica_erro()

    if erro == 2:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|              |")
        print("|")
        print("|")
        verifica_erro()

    if erro == 3:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|             /|")
        print("|             ")
        print("|")
        verifica_erro()

    if erro == 4:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|             /|\\")
        print("|                ")
        print("|")
        verifica_erro()

    if erro == 5:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|             /|\\")
        print("|             /  ")
        print("|")
        verifica_erro()

    if erro == 6:
        print("\n----------------")
        print("|              |")
        print("|             (_)")
        print("|             /|\\")
        print("|             / \ ")
        print("|")
        print(f'Você perdeu! A palavra correta era \33[32m{palavras[sortear]}\33[m')
        exit()

if __name__ == "__main__":
    dificuldade()
    jogo()
