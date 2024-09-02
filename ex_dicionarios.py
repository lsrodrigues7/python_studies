pessoa = {
    'nome': 'Leonardo',
    'idade': '26',
    'cidade': 'lutécia'
}




def main():
    print('Bem vindo ao exercicio de dicionario')
    
    pessoa['cidade']='assis'
    print(pessoa)
    pessoa['profissao']='pedreiro'
    print(pessoa)
    del pessoa['idade']
    print(pessoa)
    
    print('verificando a chave')
    
    if 'idade' in pessoa:
        print('achamos a chave')
        print(pessoa)
    else:
        print('chave nao existe')
if __name__ == '__main__':
    main()
    
quadrados = {
    '1':'1',
    '2':'4',
    '3':'9',
    '4':'16',
    '5':'25'
}