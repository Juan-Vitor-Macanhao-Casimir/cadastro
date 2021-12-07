#Essa função só faz uma linha mesmo(estética é importante)
def linha(tam=42):
     print('—'*tam)


#Essa função deixa uma frase ou palavra em destaque
def cabeçalho(txt):
    linha()
    print(txt.center(42))
    linha()


#Essa função só le um número inteiro, se tentar botar outra coisa é impedido
def Leiaint(numero):
    while True:
        num = str(input(numero))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('ERRO! o valor digitado não é um número')


#cria um menu de opções pro usuario
def menu(*opções):
    c = 1
    for o in opções:
        print(f'{c} - {o}')
        c += 1
