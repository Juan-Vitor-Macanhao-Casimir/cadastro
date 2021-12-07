from exercício.lib.visual import *
from exercício.lib.arquivos import *
arq = 'cadastrodaspessoas.txt'
if not arquivoexiste(arq):
    arq = criararquivo(arq)

while True:
    cabeçalho('MENU PRINCIPAL')
    menu('Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do programa')
    linha()
    resp = Leiaint('Sua Opção: ')
    if resp == 1:
        cabeçalho('PESSOAS CADASTRADAS')
        lerarquivo(arq)
    elif resp == 2:
        nome = str(input('nome: '))
        idade = int(input('idade: '))
        ID = int(input('ID: '))
        cadastrar(arq, nome, idade, ID)
    elif resp == 3:
        cabeçalho('Saindo do programa... até logo')
        break
    else:
        print('OPÇÃO INVALIDA')
