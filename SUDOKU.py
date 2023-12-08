import numpy as np 
import pandas as pd

list_incomp =[5,4,3,0,1,7,6,9,0,0,1,7,9,0,0,0,5,4,0,8,9,4,0,5,1,3,7,4,3,6,1,5,0,7,0,9,7,5,0,6,9,4,0,1,3,1,9,0,0,7,0,5,4,6,9,6,5,0,0,1,4,7,0,8,7,4,5,0,9,3,0,1,3,2,1,7,4,0,9,0,5]
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

def reten_lista(lo_setor ):
    if(type(   lo_setor  ) == list):
        return lo_setor
    elif( type(lo_setor.ravel().tolist()[0]) == list  ):
        return lo_setor.ravel().tolist()[0]
    else: return lo_setor.ravel().tolist()

def print_lines(line_number: 0, tab_print = tabuleiro):
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
    generator= (f"{item} │" for item in tab_print[line_number,].tolist()[0])
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
            print_lines(number, tab_print = tabuleiro)
        elif number in range(1,9): 
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print_lines(number, tab_print = tabuleiro)
        else: 
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")


def linhas(ind: int , tip = 'L', tab_lin = tabuleiro) -> list:
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
            lin = tab_lin[ind:ind+1, :];
        case 'S':
            for_linhas = pre_setor(ind)
            lin = tab_lin[for_linhas[0]:for_linhas[1], :];
        case _: []
    return lin;

def colunas(ind_two: int, tip = 'L', tab_col = tabuleiro)-> list:
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
            colun = tab_col[:,ind_two : ind_two+1].tolist();
            colun_end = list(item[0] for item in colun )
        case 'S':
            for_linhas = pre_setor(ind_two)
            colun_end = tab_col[:, for_linhas[0]:for_linhas[1]];
        case _: []
    return colun_end;



def pre_setor(ind_tree: int) -> list:
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

def setor(ind:int, ind_two: int, tab_setor  = tabuleiro):
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
    mat_setor = tab_setor[for_linhas[0]: for_linhas[3], for_col[0]: for_col[3] ]
    return mat_setor

def filtering(column:list, verify_list = acceptable_list, tip = None)-> list:
    """Retorna o valor que não se encontra no lista de aceitáveis
    ...
    
    Atributes
    ---------
    column: list
    Lista de valores incluídos na linha/coluna/setor
    
    Returns
    ------
    numpy.matrix 3x3."""
    if tip == 'in':
        verificado = list(filter(lambda number: number  in column , verify_list ))
        return verificado
    else:
        verificado = list(filter(lambda number: number not in column , verify_list ))
        return verificado

def resolver_cell(tab_cell = None)-> None:
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
    Atributes
    ---------
    tab: numpy.matrix
    Matriz que será utilizada para execução das alterações da função
    Returns
    None
    ------
    """
    global tabuleiro
    if tab_cell == None:
        tab_cell = tabuleiro
    for ind in range(0,9):
        for ind_two in range(0,9):
            if(tab_cell[ind:ind+1 , ind_two:ind_two+1] == 0 ):
                vet_lin = reten_lista(linhas(ind, tab_lin= tab_cell))
                vet_colun = reten_lista(colunas(ind_two, tab_col=tab_cell))
                setor_objeto = reten_lista(setor(ind, ind_two, tab_setor = tab_cell))
                validation = np.unique(setor_objeto+vet_colun+vet_lin)
                if len(filtering(vet_lin)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_lin)[0]; print('linha')
                elif len(filtering(vet_colun) )== 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_colun)[0];print('coluna')
                elif len(filtering(setor_objeto)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(setor_objeto)[0];print('setor')
                elif len(filtering(validation)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(validation)[0];print('conjunto')


def resolver_setor( tab_end_setor = None):
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
        
    Returns
    None
    ------
    """
    global tabuleiro
    if tab_end_setor == None:
        tab_end_setor = tabuleiro
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two, tab_setor = tab_end_setor)
            resto = filtering(setor_objeto)
            for i in resto:
                sem_linhas , sem_coluns = np.where(tab_end_setor == i)
                linhas_setor = pre_setor(ind)[0:3]
                colunas_setor  = pre_setor(ind_two)[0:3]
                linha_desejadas = [elemento for elemento in linhas_setor if elemento not in sem_linhas.tolist()]
                coluna_desejadas = [elemento for elemento in colunas_setor if elemento not in sem_coluns.tolist()]
                lin_zero , col_zero = np.where(tab_end_setor == 0)
                positions = list(zip(lin_zero.tolist(), col_zero.tolist()))
                inputer = [nao_drop for nao_drop in positions if(nao_drop[0] in linha_desejadas and nao_drop[1] in  coluna_desejadas )]
                match len(inputer):
                    case 1:
                        if i not in setor_objeto:
                            tab_end_setor[inputer[0]] = i;#print(f'alterado{( inputer[0][0], inputer[0][1])}')

def listagem_numbers(value:0, setor) -> list:
    possiveis_possicoes = np.where(setor == value)
    return list(zip(possiveis_possicoes[0],possiveis_possicoes[1]))


def pre_cadeia(tab_pre_cad= tabuleiro, value = 1):
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two, tab_setor = tab_pre_cad)
            resto = filtering(setor_objeto)
            posicoes = listagem_numbers(setor = setor_objeto, value= 0 )
            if value in resto and 1/len(resto) == 0.5 and posicoes != []:
                verifier(x = posicoes[0][0] + ind, y = posicoes[0][1]+ ind_two , verify_tab=tab_pre_cad, value = value)


def cadeia_forcada(tab_end_cadeia = tabuleiro):
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two, tab_setor= tab_end_cadeia)
            resto = filtering(setor_objeto)
            for i in resto:
                if 1/len(resto) == 0.5:
                    posicoes = listagem_numbers(setor = setor_objeto, value= 0 )
                    estructure= {}
                    counter = 0
                    while counter < len(posicoes):
                        clone =np.copy( tab_end_cadeia)
                        print(clone)
                        clone[posicoes[counter][0]+ ind,posicoes[counter][1]+ ind_two ] = i
                        print(clone)
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone)
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone)
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone )
                        new_posicoes = listagem_numbers(setor = clone, value = i)
                        print(new_posicoes)
                        print(clone)
                        estructure[str(posicoes[counter])]=new_posicoes
                        estructure
                        counter = counter+1
                    try:
                        returners = [posicao for posicao in estructure[str(posicoes[0])] if posicao in estructure[str(posicoes[1])]]
                        if returners == []:
                            pass
                        else:
                            prev = 0
                            while prev < len(returners):
                                print(estructure)
                                print(returners)
                                print(prev)
                                verifier(x = returners[prev][0], y = returners[prev][1], verify_tab=tab_end_cadeia, value = i)
                                print(ind, ind_two, returners[prev] , i)
                                prev = prev+1
                    except: pass
                else: pass


def verifier(x = 0, y = 0, value = 0, verify_tab= tabuleiro):
    vet_lin = linhas(x, tab_lin =verify_tab )
    vet_colun = colunas(y, tab_col= verify_tab)
    setor_objeto = setor(x, y, tab_setor = verify_tab)
    setor_correto = reten_lista(setor_objeto)
    linha_correta = reten_lista(vet_lin)
    col_correta = reten_lista(vet_colun)
    validation = np.unique(setor_correto+col_correta+linha_correta)
    if(value not in validation and verify_tab[x, y] == 0 ):
        verify_tab[x,y] =value
    else: pass


vetor_matrizx = atualize_matrix()


pre_tabuleiro()

cadeia_forcada(tab_end_cadeia= tabuleiro)

resolver_cell(tab_cell=  tabuleiro)
resolver_setor( tab_end_setor= tabuleiro)

pre_tabuleiro()



def reverse_tab():
    global tabuleiro
    grounded = []
    contador = 1
    for ind in range(0,9):
        for ind_two in range(0,9):
            vet_lin = reten_lista(linhas(ind, tab_lin= tabuleiro))
            vet_colun = reten_lista(colunas(ind_two, tab_col=tabuleiro))
            setor_objeto = reten_lista(setor(ind, ind_two, tab_setor = tabuleiro))
            validation = np.unique(setor_objeto+vet_colun+vet_lin)
            resto = filtering(validation)
            if tabuleiro[ind, ind_two]>0:
                resto.clear()
            grounded.append( [ind ,  ind_two, resto])
            contador += 1
    return grounded

ponto = list_rest[21]
def duplicate_pattern():
    global list_rest
    for ind in range(0, len(list_rest)):
        ponto = list_rest[ind]
        if ponto == []:
            pass
        elif(len(ponto[2]) == 2):
            la_coluna = [vetor for vetor in list_rest if vetor[1] == ponto[1] and vetor[2] ==ponto[2] ]
            la_linha = [vetor for vetor in list_rest if vetor[0] == ponto[0] and vetor[2] ==ponto[2] ]
            if len(la_coluna) == 2:
                for vetor in list_rest:
                    retirada( listas = vetor, remover = ponto, tip = '')
            if len(la_linha) == 2:
                for vetor in list_rest:
                    retirada( listas = vetor, remover = ponto, tip = 'L')


def retirada(listas: list, remover: list, tip='L') -> list:
    if tip == 'L':
        alterador = remover[0]
        code = 0
    else:
        alterador = remover[1]  
        code = 1
    if listas[2] == []:
        pass
    elif listas[2] == remover[2]:
        pass
    else:
        try:
            if (listas[code] == alterador):
                listas[2].remove(remover[2][0])
        except:
            pass
        try:
            if (listas[code] == alterador):
                listas[2].remove(remover[2][1])
        except:
            pass

def x_vector(vetor:list , not_equal = None)-> list:   
    if vetor == []:
        return []
    elif(len(vetor[2]) == 2 and not_equal== None):
        return vetor
    elif (len(vetor[2]) == 2 and vetor != not_equal and len(filtering(vetor[2], not_equal[2], 'in')) >= 0  ):
        return vetor
    else: return []


def x_wings():
    global list_rest
    ind = 0
    while ind in range(0,9):
        pre_vector = list_rest[(0+9*ind): (9+9*ind)]
        for vec in pre_vector:
            pivot = x_vector(vec)
            if len(pivot)> 0:
                for second_vec in pre_vector:
                    x_wind = x_vector(second_vec, not_equal=pivot)
                    if len(x_wind) > 0:
                        value_x = filtering(pivot[2], x_wind[2] , tip = 'in')
                        y_list = [vetor for vetor in list_rest if vetor[1] == pivot[1]]
                        for first_yvec in y_list:
                            y_wind = x_vector(first_yvec, not_equal=pivot)
                            if len(y_wind)> 0 :
                                y_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                xy_wind = [vetor for vetor in list_rest if vetor[1] == x_wind[1] and vetor[0] == y_wind[0] ][0]
                                xy_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                if len(xy_wind[2])  ==2  :
                                    for verify_value in pivot[2]:
                                        if( verify_value in y_value and verify_value in xy_value and verify_value in value_x ):
                                            for end_vector in list_rest:
                                                coluns_to_drop  = [pivot[1], x_wind[1]]
                                                if(end_vector not in [pivot, x_wind, y_wind, xy_wind ] and end_vector[1] in coluns_to_drop and verify_value in end_vector[2] ):
                                                    print(pivot, x_wind, y_wind, xy_wind , end_vector)
                                                    end_vector[2].remove(verify_value)
        ind += 1 


def par_de_pontos( ):
    global tabuleiro , list_rest
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            absolutes = []
            setor_objeto = setor(ind, ind_two, tab_setor = tabuleiro)
            list_obgs = listagem_numbers(value= 0, setor = setor_objeto)    
            if len(list_obgs) >=2:
                for obgs in list_obgs:
                    absolutes.append([rest for rest in list_rest if rest[0] == (obgs[0] + ind) and  rest[1] == (obgs[1] + ind_two) ][0])
                values = [coluns[2] for coluns in absolutes]
                rest_values = list(set(item for sublist in values for item in sublist))
                for value_rest in rest_values:
                    para_exumacao = [exum for exum in  absolutes if value_rest in exum[2]]
                    if len(para_exumacao) == 2 and para_exumacao[0][1]  ==  para_exumacao[1][1] : 
                        for end_vector in list_rest:
                            if(end_vector not in para_exumacao  and end_vector[1] ==para_exumacao[0][1] and  value_rest in end_vector[2] ):
                                end_vector[2].remove(value_rest)



pre_tabuleiro()
tabuleiro = None
tabuleiro
list_rest = None
list_rest = reverse_tab() 
result_rest()



pre_tabuleiro()

cadeia_forcada(tab_end_cadeia= tabuleiro)

resolver_cell( tab_cell=None)
resolver_setor()

pre_tabuleiro()



def result_rest():
    global tabuleiro, list_rest
    duplicate_pattern()
    x_wings()
    par_de_pontos()
    xy_wings()
    for vetores in list_rest:
        if len(vetores[2]) == 1:
            tabuleiro[vetores[0], vetores[1]] = vetores[2][0]
    pre_tabuleiro()


result_rest()

def xy_wings():
    global list_rest
    ind = 0
    while ind in range(0,9):
        x_lin = list_rest[(0+9*ind): (9+9*ind)]
        for vec in x_lin:
            pivot = x_vector(vec)
            if len(pivot)> 0:
                for second_vec in x_lin:
                    x_wind = x_vector(second_vec, not_equal=pivot)
                    if len(x_wind) > 0:
                        value_x = filtering(pivot[2], x_wind[2] , tip = 'in')
                        y_col = [vetor for vetor in list_rest if vetor[1] == pivot[1]]
                        setor_pivo = setor_com_faltantes(pivot)
                        setorizado = setor_pivo+y_col
                        for first_yvec in setorizado:
                            y_wind = x_vector(first_yvec, not_equal=pivot)
                            y_wind = x_vector(y_wind, not_equal=x_wind)
                            if len(y_wind)> 0 :
                                y_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                y_no_value = filtering(pivot[2], y_wind[2] )
                                value_no_x = filtering(pivot[2], x_wind[2] )
                                if(y_value != value_x and len(y_value) == 1 and  y_no_value == value_no_x and len(value_no_x)==1):
                                    x_col = [vetor for vetor in list_rest if vetor[1] == x_wind[1]]
                                    setor_x = setor_com_faltantes(x_wind)
                                    y_lin = list_rest[(0+9*y_wind[0]): (9+9*y_wind[0])]
                                    setor_y = setor_com_faltantes(y_wind)
                                    for end_vector in list_rest:
                                        if (end_vector not in [pivot, x_wind, y_wind] and
                                        y_no_value[0] in end_vector[2] and
                                        (end_vector in x_lin or end_vector in x_col or end_vector in setor_x) and
                                        (end_vector in y_lin or end_vector in y_col or end_vector in setor_y)):
                                            print( pivot,  x_wind  ,y_wind , end_vector )
                                            end_vector[2].remove(y_no_value[0])
        ind += 1

def setor_com_faltantes(vec:list)-> list :
    absolutes = []
    ind = pre_setor(vec[0])[0]
    ind_two = pre_setor(vec[1])[0]
    setor_objeto = setor(ind, ind_two, tab_setor = tabuleiro)
    list_obgs = listagem_numbers(value= 0, setor = setor_objeto)    
    if len(list_obgs) >=2:
        for obgs in list_obgs:
            absolutes.append([rest for rest in list_rest if rest[0] == (obgs[0] + ind) and  rest[1] == (obgs[1] + ind_two) ][0])
    return absolutes