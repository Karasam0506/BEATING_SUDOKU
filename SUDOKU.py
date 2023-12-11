import numpy as np 
from functools import wraps


list_incomp =[5,4,3,0,1,7,6,9,0,0,1,7,9,0,0,0,5,4,0,8,9,4,0,5,1,3,7,4,3,6,1,5,0,7,0,9,7,5,0,6,9,4,0,1,3,1,9,0,0,7,0,5,4,6,9,6,5,0,0,1,4,7,0,8,7,4,5,0,9,3,0,1,3,2,1,7,4,0,9,0,5]
list_incomp =[0,0,7,0,8,3,6,0,0,0,3,9,7,0,6,8,0,0,8,2,6,4,1,9,7,5,3,6,4,0,1,9,0,3,8,7,0,8,0,3,6,7,0,0,0,0,7,3,0,4,8,0,6,0,3,9,0,8,7,0,0,2,6,7,6,4,9,0,0,1,3,8,2,0,8,6,3,0,9,7,0]

matrix_incomp =  np.matrix(np.array(list_incomp).reshape(9,9))
matrix_incomp
tabuleiro =matrix_incomp
#pre_tabuleiro()

list_comp = [1,4,9,3,6,8,5,7,2,7,2,8,1,5,4,3,9,6,5,3,6,9,2,7,1,4,8,2,5,4,6,7,3,8,1,9,8,9,3,2,4,1,6,5,7,6,7,1,8,9,5,2,3,4,9,8,5,7,3,6,4,2,1,3,1,2,4,8,9,7,6,5,4,6,7,5,1,2,9,8,3]

matrix_comp =  np.matrix(np.array(list_comp).reshape(9,9))
matrix_comp

#tabuleiro = np.matrix(np.repeat( 0 , 81).reshape((9,9)))
#tabuleiro = matrix_comp
#tabuleiro =matrix_incomp
#tabuleiro = np.matrix(np.arange(81).reshape((9,9)))
ind = 0
ind_two = 0
#tabuleiro[0:1, 0:1]= 0

acceptable_list = [1,2,3,4,5,6,7,8,9]

#tabuleiro == matrix_comp

def reten_lista(lo_setor ):
    if(type(   lo_setor  ) == list):
        return lo_setor
    elif( type(lo_setor.ravel().tolist()[0]) == list  ):
        return lo_setor.ravel().tolist()[0]
    else: return lo_setor.ravel().tolist()

def print_lines(line_number: 0, tab_print = tabuleiro) -> None:
    """ Printa as linhas tabuleiro do SUDOKU para o usuário.
    ...
    
    Atributes
    ---------
    number: int
        Repetidor que indicara qual a linha deve ser criada no tabuleiro.
    tab_print: numpy.matrix
        Matriz que sera mostrada pelo código.
    Returns
    -------
        Print da linha do tabuleiro de SUDOKU.
    """
    generator= (f"{item} │" for item in tab_print[line_number,].tolist()[0])
    result_string = ' '.join(generator)
    print(f'│ {result_string}')

def pre_tabuleiro()-> None:
    """ Printa o tabuleiro do SUDOKU para o usuário.
    ...
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
    tab_lin: numpy.matrix
        Matrix de onde a linha será utilizado.
        
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
    tip: str
        Indica se deve ser buscado por setor coluna ou por setor
    
    Returns
    ------
    Lista com os valores da coluna.
    """
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
        Lista com os valores do setor.
    """
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
    tab_setor: numpy.matrix
        Matrix de onde os setores devem ser retirados.
    
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
        Lista de valores incluídos na linha/coluna/setor.
    verify_list: list
        Lista de valores que são aceitaveis.
    tip: str
        Define o tipo de filtro a ser utilizado. Se tip ==  'in' retornaremos com os valores identicos em ambas as listas
    caso tip != 'in' retornara os valores faltantes da verify_list.


    Returns
    ------
    list."""
    if tip == 'in':
        verificado = list(filter(lambda number: number  in column , verify_list ))
        return verificado
    else:
        verificado = list(filter(lambda number: number not in column , verify_list ))
        return verificado

@decorate_matriz
def resolver_cell(tab_cell = None)-> None:
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
    Atributes
    ---------
    tab: numpy.matrix
        Matriz que será utilizada para execução das alterações da função.
    Returns
    ------
    None
    """
    global tabuleiro
    if tab_cell  is None:
        tab_cell = tabuleiro
    for ind in range(0,9):
        for ind_two in range(0,9):
            if(tab_cell[ind:ind+1 , ind_two:ind_two+1] == 0 ):
                vet_lin = reten_lista(linhas(ind, tab_lin= tab_cell))
                vet_colun = reten_lista(colunas(ind_two, tab_col=tab_cell))
                setor_objeto = reten_lista(setor(ind, ind_two, tab_setor = tab_cell))
                validation = np.unique(setor_objeto+vet_colun+vet_lin)
                if len(filtering(vet_lin)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_lin)[0];
                elif len(filtering(vet_colun) )== 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(vet_colun)[0];
                elif len(filtering(setor_objeto)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(setor_objeto)[0];
                elif len(filtering(validation)) == 1:
                    tab_cell[ind:ind+1 , ind_two:ind_two+1] = filtering(validation)[0];

@decorate_matriz
def resolver_setor( tab_end_setor = None):
    """Atualiza a informação no tabuleiro, passa por todas as células da matriz 
    verifica-se na coluna/linha/setor e o conjunto de todos com a lista de variáveis aceitáveis.
    ...
    tab_end_setor: numpy.matrix
        Matrix que será utilizada para execução das alterações da função.

        
    Returns
    ------
    None
    """
    global tabuleiro
    if tab_end_setor is None:
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
                            tab_end_setor[inputer[0]] = i;

def listagem_numbers(value:0, setor) -> list:
    """Retorna a lista de posições ou células de uma matriz que tem o valor indicado
    
    Args:
    value(int): Valor que será procurado dentro da matriz
    setor (numpy.matrix): Matrix que será utilizada para procura do valor(value) requisitado.
    
    Returns:
        list
    """
    possiveis_possicoes = np.where(setor == value)
    return list(zip(possiveis_possicoes[0],possiveis_possicoes[1]))


def pre_cadeia(tab_pre_cad= None, value = 1) -> None:
    """Para aplicação da técnica "cadeia forçada", inplantamos um valor que tem 50% de chance de estar na célula.
    
    Args:
    value(int): Valor que será aplicado na célula se ele tiver 50% de chance de estar na posição correta.
    tab_pre_cad (numpy.matrix): Matrix onde o valor sera implantado.
    
    Returns:
        None
    """
    global tabuleiro
    if tab_pre_cad is None:
        tab_pre_cad = tabuleiro

    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            setor_objeto = setor(ind, ind_two, tab_setor = tab_pre_cad)
            resto = filtering(setor_objeto)
            posicoes = listagem_numbers(setor = setor_objeto, value= 0 )
            if value in resto and 1/len(resto) == 0.5 and posicoes != []:
                verifier(x = posicoes[0][0] + ind, y = posicoes[0][1]+ ind_two , verify_tab=tab_pre_cad, value = value)

def cadeia_forcada(tab_end_cadeia = None) -> None:
    """Aplicação da técnica "cadeia forçada", verifica-se se em um setor é possível encontrar um valor que tenha
    50% de chance de ser implementado em duas células, daí esse valor é implementado separadamente em vezes distintas,
    em ambas implementações o tabuleiro é concluído ou avançado, se em ambas as implementações o um mesmo valor for
    encontrado em outros locais do tabuleiro ele é implementado.
    
    Args:
    tab_end_cadeia (numpy.matrix): Matrix onde o valor sera implantado.
    
    Returns:
        None
    """
    if tab_end_cadeia is None:
        tab_end_cadeia = tabuleiro
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
                        clone[posicoes[counter][0]+ ind,posicoes[counter][1]+ ind_two ] = i
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone)
                        resolver_rest(the_tabuleiro= clone)
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone)
                        resolver_rest(the_tabuleiro= clone)
                        resolver_setor(tab_end_setor=clone)
                        resolver_cell(tab_cell = clone )
                        new_posicoes = listagem_numbers(setor = clone, value = i)
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
                                verifier(x = returners[prev][0], y = returners[prev][1], verify_tab=tab_end_cadeia, value = i)
                                prev = prev+1
                    except: pass
                else: pass


def verifier(x = 0, y = 0, value = 0, verify_tab= None) -> None:
    """Verifica se o valor a ser implementado segue as regras do sudoku, caso seguir o valor é implementado
    
    Args:
    x (int): Número da linha onde o valor vai ser verificado.
    y (int): Número da coluna onde o valor vai ser verificado.
    value (int): Número que vai ser validado.
    verify_tab (numpy.matrix): Matrix onde o valor sera implantado.
    
    Returns:
        None
    """
    global tabuleiro
    if verify_tab is None:
        verify_tab = tabuleiro
    
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

def reverse_tab(for_reverse_tab = None) -> None:
    """Cria um vetor contendo as posições x e y da matriz e os respectívos valores que podem ser implementados na célula.
    
    Args:
    for_reverse_tab (numpy.matrix): Matrix onde os valores possíveis seram encontrados.
    
    Returns:
        None
    """
    global tabuleiro
    if for_reverse_tab is None:
        for_reverse_tab = tabuleiro
    grounded = []
    contador = 1
    for ind in range(0,9):
        for ind_two in range(0,9):
            vet_lin = reten_lista(linhas(ind, tab_lin= for_reverse_tab))
            vet_colun = reten_lista(colunas(ind_two, tab_col=for_reverse_tab))
            setor_objeto = reten_lista(setor(ind, ind_two, tab_setor = for_reverse_tab))
            validation = np.unique(setor_objeto+vet_colun+vet_lin)
            resto = filtering(validation)
            if for_reverse_tab[ind, ind_two]>0:
                resto.clear()
            grounded.append( [ind ,  ind_two, resto])
            contador += 1
    return grounded

def duplicate_pattern(ret_duplicate = None) -> None:
    """Verifica se há duas células contendo os mesmos 2 valores dentro da mesma linha ou coluna, caso
    houver esses dois valores são retirados da coluna ou da linha em que aparecerem.
    
    Args:
    ret_duplicate (numpy.matrix): Matrix onde o método será aplicado.
    
    Returns:
        None
    """
    global list_rest
    if ret_duplicate is None:
        ret_duplicate = list_rest
    for ind in range(0, len(ret_duplicate)):
        ponto = ret_duplicate[ind]
        if ponto == []:
            pass
        elif(len(ponto[2]) == 2):
            la_coluna = [vetor for vetor in ret_duplicate if vetor[1] == ponto[1] and vetor[2] ==ponto[2] ]
            la_linha = [vetor for vetor in ret_duplicate if vetor[0] == ponto[0] and vetor[2] ==ponto[2] ]
            if len(la_coluna) == 2:
                for vetor in ret_duplicate:
                    retirada( listas = vetor, remover = ponto, tip = '')
            if len(la_linha) == 2:
                for vetor in ret_duplicate:
                    retirada( listas = vetor, remover = ponto, tip = 'L')


def retirada(listas: list, remover: list, tip='L') -> None:
    """Remove os valores possíveis de uma célula a partir dos valores possíveis de outra célula.
    
    Args:
    listas (list): Lista contendo os valores possíveis de uma célula.
    remover (list): Lista contendo os valores que devem ser retirados de outras células.
    tip (str): String que informa se a célula deve estar contida na mesma linha ou coluna da célula removedora.
    
    Returns:
        None
    """
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

def x_vector(vetor:list , not_equal = None, tip = None)-> list:   
    """Retorna uma lista que representa uma célula no tabuleiro de sudoku, são validados regras para seleção de uma
    "wing" de acordo com a teória de x_wing do sudoku.
    
    Args:
    vetor (list): Lista contendo as informações da célula proposta para ser a "wing".
    not_equal (list): Lista contendo as informações da célula que é o "pivot".
    tip (int): Quantidade máxima de possibilidades aceitáveis.
    
    Returns:
        list
    """
    if vetor == []:
        return []
    elif (len(vetor[2]) == 2):
        if(not_equal== None):
            return vetor
        elif (tip is None and len(vetor[2]) == 2 and vetor != not_equal and len(filtering(vetor[2], not_equal[2], 'in')) >= 0  ):
            return vetor
        elif (vetor[2] !=  [] and vetor != not_equal and len(filtering(vetor[2], not_equal[2], 'in')) >= 0  ):
            return vetor
        else: return []
    else: return []


def x_wings(for_xwing = None)-> None:
    """Aplicação do método x_wing, nele é verificado se é possível encontrar 4 células que contém o mesmo valor 
    possível, formando um quadrado entre eles se for encontrado mais células que contém esse mesmo valor dentro
    das colunas e linhas desse quadrado eles vão ser retirados.
    
    Args:
    vetor (list): Lista contendo as informações da célula proposta para ser a "wing".
    not_equal (list): Lista contendo as informações da célula que é o "pivot".
    
    Returns:
        list
    """
    global list_rest
    if for_xwing is None:
        for_xwing = list_rest
    ind = 0
    while ind in range(0,9):
        pre_vector = for_xwing[(0+9*ind): (9+9*ind)]
        for vec in pre_vector:
            pivot = x_vector(vetor = vec)
            if len(pivot)> 0:
                for second_vec in pre_vector:
                    x_wind = x_vector(second_vec, not_equal=pivot, tip = 2)
                    if len(x_wind) > 0:
                        value_x = filtering(pivot[2], x_wind[2] , tip = 'in')
                        y_list = [vetor for vetor in for_xwing if vetor[1] == pivot[1]]
                        for first_yvec in y_list:
                            y_wind = x_vector(vetor = first_yvec, not_equal=pivot, tip = 2)
                            if len(y_wind)> 0 :
                                y_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                xy_wind = [vetor for vetor in for_xwing if vetor[1] == x_wind[1] and vetor[0] == y_wind[0] ][0]
                                xy_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                if len(xy_wind[2])  > 0  :
                                    for verify_value in pivot[2]:
                                        if( verify_value in y_value and verify_value in xy_value and verify_value in value_x ):
                                            for end_vector in for_xwing:
                                                coluns_to_drop  = [pivot[1], x_wind[1]]
                                                if(end_vector not in [pivot, x_wind, y_wind, xy_wind ] and end_vector[1] in coluns_to_drop and verify_value in end_vector[2] ):
                                                    end_vector[2].remove(verify_value)
        ind += 1 




def par_de_pontos(tab = None , restante = None) -> None:
    """Verifica se há duas células dentro de um setor contendo os mesmos 2 valores dentro da mesma linha ou coluna,
    caso houver esses dois valores são retirados da coluna ou da linha em que aparecerem.
    
    Args:
    tab (numpy.matrix): Matrix onde as posições vão ser procuradas.
    restante (list): Lista contendo os valores possíveis para cada célula do tabuleiro.
    Returns:
        None
    """
    global tabuleiro , list_rest

    if tab is None:
        tab = tabuleiro
    if restante is None:
        restante = list_rest
    for ind in range(0,9,3):
        for ind_two in range(0,9,3):
            absolutes = []
            setor_objeto = setor(ind, ind_two, tab_setor = tab)
            list_obgs = listagem_numbers(value= 0, setor = setor_objeto)    
            if len(list_obgs) >=2:
                for obgs in list_obgs:
                    absolutes.append([rest for rest in restante if rest[0] == (obgs[0] + ind) and  rest[1] == (obgs[1] + ind_two) ][0])
                values = [coluns[2] for coluns in absolutes]
                rest_values = list(set(item for sublist in values for item in sublist))
                for value_rest in rest_values:
                    para_exumacao = [exum for exum in  absolutes if value_rest in exum[2]]
                    if len(para_exumacao) == 2 and para_exumacao[0][1]  ==  para_exumacao[1][1] : 
                        for end_vector in restante:
                            if(end_vector not in para_exumacao  and end_vector[1] ==para_exumacao[0][1] and  value_rest in end_vector[2] ):
                                end_vector[2].remove(value_rest)


@decorate_matriz
def resolver_rest(the_tabuleiro = None, the_rest = None) -> None:
    """Aplicação dos métodos que utilizam do resto de cada célula
    
    Args:
    the_tabuleiro (numpy.matrix): Matrix da posição do tabuleiro.
    the_rest (list): Lista contendo os valores possíveis para cada célula do tabuleiro.
    Returns:
        None
    """
    global tabuleiro, list_rest
    if the_tabuleiro is None:
        the_tabuleiro = tabuleiro
    if the_rest is None:
        the_rest = reverse_tab(for_reverse_tab=the_tabuleiro )
    duplicate_pattern(ret_duplicate = the_rest )
    x_wings(for_xwing = the_rest)
    par_de_pontos(tab = the_tabuleiro ,restante = the_rest )
    xy_wings(for_xy_wing=the_rest, great_tab= the_tabuleiro)
    for vetores in the_rest:
        if len(vetores[2]) == 1:
            the_tabuleiro[vetores[0], vetores[1]] = vetores[2][0]

def xy_wings(for_xy_wing = None, great_tab = None):
    """Aplicação do método xy_wing, nele é verificado se é possível encontrar 1 célula pivo, 1 asa na linha e uma 
    asa na coluna ou no setor, em ambas as asas devem haver valores que iguais a um dos valores do pivo, mas esses
    valores devem ser diferentes entre as asas. 
    
    Args:
    for_xy_wing (list): Lista contendo os valores possíveis para cada célula do tabuleiro.
    Returns:
        None
    """
    global list_rest, tabuleiro
    if great_tab is None:
        great_tab = tabuleiro
    if for_xy_wing is None:
        for_xy_wing = list_rest
    ind = 0
    while ind in range(0,9):
        x_lin = for_xy_wing[(0+9*ind): (9+9*ind)]
        for vec in x_lin:
            pivot = x_vector(vec)
            if len(pivot)> 0:
                for second_vec in x_lin:
                    x_wind = x_vector(second_vec, not_equal=pivot)
                    if len(x_wind) > 0:
                        value_x = filtering(pivot[2], x_wind[2] , tip = 'in')
                        y_col = [vetor for vetor in for_xy_wing if vetor[1] == pivot[1]]
                        setor_pivo = setor_com_faltantes(pivot, great_rest= for_xy_wing, tab_falt=great_tab )
                        setorizado = setor_pivo+y_col
                        for first_yvec in setorizado:
                            y_wind = x_vector(first_yvec, not_equal=pivot)
                            y_wind = x_vector(y_wind, not_equal=x_wind)
                            if len(y_wind)> 0 :
                                y_value = filtering(pivot[2], y_wind[2] , tip = 'in')
                                y_no_value = filtering(pivot[2], y_wind[2] )
                                value_no_x = filtering(pivot[2], x_wind[2] )
                                if(y_value != value_x and len(y_value) == 1 and  y_no_value == value_no_x and len(value_no_x)==1):
                                    x_col = [vetor for vetor in for_xy_wing if vetor[1] == x_wind[1]]
                                    setor_x = setor_com_faltantes(x_wind, great_rest= for_xy_wing, tab_falt=great_tab)
                                    y_lin = for_xy_wing[(0+9*y_wind[0]): (9+9*y_wind[0])]
                                    setor_y = setor_com_faltantes(y_wind, great_rest= for_xy_wing, tab_falt=great_tab)
                                    for end_vector in for_xy_wing:
                                        if (end_vector not in [pivot, x_wind, y_wind] and
                                        y_no_value[0] in end_vector[2] and
                                        (end_vector in x_lin or end_vector in x_col or end_vector in setor_x) and
                                        (end_vector in y_lin or end_vector in y_col or end_vector in setor_y)):
                                            end_vector[2].remove(y_no_value[0])
        ind += 1

def setor_com_faltantes(vec:list , tab_falt = None , great_rest = None)-> list :
    """Retorna uma lista de células que podem ser alteradas no setor.
    
    Args:
    vec (list): Lista contendo o vetor validado para o xy_wing.
    great_rest (list): Lista contendo os valores possíveis para cada célula do tabuleiro.
    
    Returns:
        list
    """
    global list_rest, tabuleiro
    if great_rest is None:
        great_rest = list_rest
    if tab_falt is None:
        tab_falt = tabuleiro
    absolutes = []
    ind = pre_setor(vec[0])[0]
    ind_two = pre_setor(vec[1])[0]
    setor_objeto = setor(ind, ind_two, tab_setor = tab_falt)
    list_obgs = listagem_numbers(value= 0, setor = setor_objeto)    
    if len(list_obgs) >=2:
        for obgs in list_obgs:
            absolutes.append([rest for rest in great_rest if rest[0] == (obgs[0] + ind) and  rest[1] == (obgs[1] + ind_two) ][0])
    return absolutes


def decorate_matriz(func)-> None:
    """Decorator que mostra se há alteração nos valores do tabuleiro após a alteração da função.
    
    Args:
    func (func): Função que representa um método para resolução do sudoku.
    
    Returns:
        None
    """
    @wraps(func)

    def wrapper(**kwargs):
        global tabuleiro
        clone =np.copy( tabuleiro)
        in_value = tabuleiro
        for key , value in kwargs.items():
            if isinstance(value, np.matrix):
                clone =np.copy( kwargs)
                in_value = value

        zero_later = len(np.where(clone == 0)[0])

        print(f'Células a serem preenchidas: {zero_later}')

        func(**kwargs)

        alteracoes = len(np.where(clone != in_value)[0])
        zerados = len(np.where( in_value == 0)[0])
        print('Método {}'.format(func.__name__))
        print(f'Células preenchidas: {alteracoes}, Células a serem preenchidas: {zerados}') 
    return wrapper