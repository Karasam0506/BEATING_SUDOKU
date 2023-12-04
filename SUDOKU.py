import numpy as np 


list_incomp =[0,0,7,0,8,3,6,0,0,0,3,9,7,0,6,8,0,0,8,2,6,4,1,9,7,5,3,6,4,0,1,9,0,3,8,7,0,8,0,3,6,7,0,0,0,0,7,3,0,4,8,0,6,0,3,9,0,8,7,0,0,2,6,7,6,4,9,0,0,1,3,8,2,0,8,6,3,0,9,7,0]

matrix_incomp =  np.matrix(np.array(list_incomp).reshape(9,9))
matrix_incomp
tabuleiro =matrix_incomp
pre_tabuleiro()

list_comp = [1,4,9,3,6,8,5,7,2,7,2,8,1,5,4,3,9,6,5,3,6,9,2,7,1,4,8,2,5,4,6,7,3,8,1,9,8,9,3,2,4,1,6,5,7,6,7,1,8,9,5,2,3,4,9,8,5,7,3,6,4,2,1,3,1,2,4,8,9,7,6,5,4,6,7,5,1,2,9,8,3]

matrix_comp =  np.matrix(np.array(list_comp).reshape(9,9))
matrix_comp

tabuleiro = np.matrix(np.repeat( 0 , 81).reshape((9,9)))
tabuleiro = matrix_comp
tabuleiro =matrix_incomp
#tabuleiro = np.matrix(np.arange(81).reshape((9,9)))
ind = 0
ind_two = 0
tabuleiro[0:1, 0:1]= 0

acceptable_list = [1,2,3,4,5,6,7,8,9]

tabuleiro == matrix_comp

def print_lines(line_number: 0):
    """ Printa as linhas tabuleiro do SUDOKU para o usuário.
    ...
    
    Atributes
    ---------
    number: int
        Repetidor que indicara qual a linha deve ser criada no tabuleiro.
    
    Returns
    -------
        Print da linha do tabuleiro de SUDOKU.
    """
    global tabuleiro
    generator= (f"{item} │" for item in tabuleiro[line_number,].tolist()[0])
    result_string = ' '.join(generator)
    print(f'│ {result_string}')

def pre_tabuleiro():
    """ Printa o tabuleiro do SUDOKU para o usuário.
    ...
    
    Atributes
    ---------
    number: int
        Repetidor que indicara qual o tipo de linha deve ser criada.
    
    Returns
    ------
        Print do tabuleiro de SUDOKU.
    """
    for number in range(0,10):
        if number == 0: 
            print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
            print_lines(number)
        elif number in range(1,9): 
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print_lines(number)
        else: 
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")


def linhas(ind: int , tip = 'L', tabuleiro = tabuleiro) -> list:
    """Retorna os valores da linha do tabuleiro informadas pelo índice
    ...
    
    Atributes
    ---------
    ind: int
    Indicador para o qual o número da linha deve ser criada.
    tip: string
    Indicador para mostrar se é necessário fazer para o setor ou para a linha.
    
    Returns
    ------
    Para tip = 'L' Lista com os valores da linha, caso 'S' matrix contendo as linhas do setor.
    """
    match tip.upper():
        case 'L': 
            lin = tabuleiro[ind:ind+1, :];
        case 'S':
            for_linhas = pre_setor(ind)
            lin = tabuleiro[for_linhas[0]:for_linhas[1], :];
        case _: []
    return lin;

def colunas(ind_two: int, tip = 'L', tabuleiro = tabuleiro)-> list:
    """Retorna os valores da coluna do tabuleiro informadas pelo índice
    ...
    
    Atributes
    ---------
    ind_two: int
    Indicador para o qual o número da coluna deve ser criada.
    
    Returns
    ------
    Lista com os valores da coluna."""
    match tip.upper():
        case 'L': 
            colun = tabuleiro[:,ind_two : ind_two+1].tolist();
            colun_end = list(item[0] for item in colun )
        case 'S':
            for_linhas = pre_setor(ind_two)
            colun_end = tabuleiro[:, for_linhas[0]:for_linhas[1]];
        case _: []
    return colun_end;



def pre_setor(ind_tree: int, tabuleiro) -> list:
    """Cria os limites do setor 3x3 contido dentro da matriz 9x9
    ...
    
    Atributes
    ---------
    ind_tree: int
    Posição da linha ou coluna que da célula informada.
    
    Returns
    ------
    Lista com os valores do setor."""
    if ind_tree<=2 : 
        return [0, 1, 2,3]
    elif ind_tree <= 5: 
        return [3, 4, 5, 6]
    else: 
        return [6,7,8,9]

def setor(ind:int, ind_two: int, tabuleiro = tabuleiro):
    """Cria a matrix do setor 3x3.
    ...
    
    Atributes
    ---------
    ind: int
    Posição da linha da célula informada.
    ind_two: int
    Posição da coluna da célula informada.

    
    Returns
    ------
    Lista com os valores do setor."""
    for_linhas = pre_setor(ind)
    for_col  = pre_setor(ind_two)
    mat_setor = tabuleiro[for_linhas[0]: for_linhas[3], for_col[0]: for_col[3] ]
    return mat_setor

def filtering(column:list)-> list:
    """Retorna o valor que não se encontra no lista de aceitáveis
    ...
    
    Atributes
    ---------
    column: list
    Lista de valores incluídos na linha/coluna/setor
    
    Returns
    ------
    numpy.matrix 3x3."""
    global acceptable_list
    verificado = list(filter(lambda number: number not in column , acceptable_list ))
    return verificado

def resolver_cell(tabuleiro = tabuleiro)-> None:
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
        
    Returns
    None
    ------
    """
    for ind in range(0,9):
        for ind_two in range(0,9):
            if(tabuleiro[ind:ind+1 , ind_two:ind_two+1] == 0 ):
                vet_lin = linhas(ind)
                vet_colun = colunas(ind_two)
                setor_objeto = setor(ind, ind_two)
                validation = np.unique(setor_objeto.ravel().tolist()[0]+vet_colun+vet_lin.tolist()[0])
                if len(filtering(vet_lin)) == 1:
                    tabuleiro[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_lin)[0]; print('linha')
                elif len(filtering(vet_colun) )== 1:
                    tabuleiro[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_colun)[0];print('coluna')
                elif len(filtering(setor_objeto)) == 1:
                    tabuleiro[ind:ind+1 , ind_two:ind_two+1] = filtering(setor_objeto)[0];print('setor')
                elif len(filtering(validation)) == 1:
                    tabuleiro[ind:ind+1 , ind_two:ind_two+1] = filtering(validation)[0];print('conjunto')

def resolver_setor(value= None, tabuleiro = tabuleiro):
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
        
    Returns
    None
    ------
    """
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two, tabuleiro= tabuleiro)
            if(value == None):
                resto = filtering(setor_objeto)
            elif( value in filtering(setor_objeto)):
                resto = [value]
            else: break
            for i in resto:
                sem_linhas , sem_coluns = np.where(tabuleiro == i)
                linhas_setor = pre_setor(ind)[0:3]
                colunas_setor  = pre_setor(ind_two)[0:3]
                setorizado = setor(ind, ind_two, tabuleiro= tabuleiro )
                linha_desejadas = [elemento for elemento in linhas_setor if elemento not in sem_linhas.tolist()]
                coluna_desejadas = [elemento for elemento in colunas_setor if elemento not in sem_coluns.tolist()]
                lin_zero , col_zero = np.where(tabuleiro == 0)
                positions = list(zip(lin_zero.tolist(), col_zero.tolist()))
                inputer = [nao_drop for nao_drop in positions if(nao_drop[0] in linha_desejadas and nao_drop[1] in  coluna_desejadas )]
                match len(inputer):
                    case 1:
                        if i not in setor_objeto:
                            tabuleiro[inputer[0]] = i;#print(f'alterado{( inputer[0][0], inputer[0][1])}')

value = 1
def listagem_numbers(value:0, setor) -> list:
    possiveis_possicoes = np.where(setor == value)
    return list(zip(possiveis_possicoes[0],possiveis_possicoes[1]))

def cadeia_forcada(tabuleiro = tabuleiro):
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two)
            resto = filtering(setor_objeto)
            for i in resto:
                if 1/len(resto) == 0.5:
                    posicoes = listagem_numbers(setor = setor_objeto, value= 0 )
                    estructure= {}
                    counter = 0
                    while counter < len(posicoes):
                        clone =np.copy( tabuleiro)
                        print(clone)
                        clone[posicoes[counter][0]+ ind,posicoes[counter][1]+ ind_two ] = i
                        print(clone)
                        resolver_setor(tabuleiro=clone, value = i)
                        resolver_setor(tabuleiro=clone, value = i)
                        resolver_setor(tabuleiro=clone, value = i)
                        new_posicoes = listagem_numbers(setor = clone, value = i)
                        print(new_posicoes)
                        print(clone)
                        estructure[str(posicoes[counter])]=new_posicoes
                        estructure
                        counter = counter+1
                    #if (len(structure[str(posicoes[0])]) > 0 and len(structure[str(posicoes[0])]) > 0  )
                    clone
                    returners = [posicao for posicao in estructure[str(posicoes[0])] if posicao in estructure[str(posicoes[1])] and posicao not in posicoes]
                    if returners == []:
                        pass
                    else:
                        prev = 0
                        while prev < len(returners):
                            tabuleiro[returners[prev][0], returners[prev][1]] = i
                            print(ind, ind_two, returners )
                            prev = prev+1
                else: pass

cadeia_forcada()

nputer = [nao_drop for nao_drop in positions if(nao_drop[0] in linha_desejadas and nao_drop[1] in  coluna_desejadas )]
resultado = [(posicao, outra_posicao) for posicoes in estrutura['1'] for outra_posicao in estrutura['2'] if posicoes == outra_posicao]


valores_iguais = [valor for valor in meu_dicionario['vetor1'] if valor in meu_dicionario['vetor2']]

[posicao for posicao in estructure[str(posicoes[0])] if posicao in estructure[str(posicoes[1])]]

estructure[posicoes[1]]

estr
i = 5
ind = 6
ind_two = 0

pre_tabuleiro()


tabuleiro = atualize_matrix()

tabuleiro
cadeia_forcada()

resolver_cell()
resolver_setor()

pre_tabuleiro()

