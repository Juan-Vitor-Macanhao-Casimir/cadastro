#confere se o arquivo existe
def arquivoexiste(arquivo):
    try:
        arq = open(arquivo, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


#cria o arquivo com o nome que foi passado
def criararquivo(arquivo):
    try:
        arq = open(arquivo, 'wt+')
        arq.close()
    except:
        print('houve um erro na criação do arquivo')
    else:
        print(f'arquivo {arquivo} criado com sucesso')


#le o arquivo e deixax ele de forma mais estilizada
def lerarquivo(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        for linha in arq:
            dado = linha.split(';')
            c = 0
            for d in dado:
                if c == 0:
                    print(f'{d:<{len(d)}}:', end='')
                    c += 1
                else:
                    print(f'{d:>{len(d)+3}}', end='')
    finally:
        arq.close()


#ela recebe o tanto de variaveis para cadastro quanto forem nescessarias e armazena no arquivo
def cadastrar(arquivo, *cadastro):
    try:
        for i in cadastro:
            with open(arquivo, 'a+') as arq:
                arq.write(f'{i};')
        with open(arquivo, 'a+') as arq:
            arq.write('\b\n')
        arq.close()
    except:
        print('Não consegui cadastrar')