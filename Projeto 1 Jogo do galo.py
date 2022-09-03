# ist199265


def eh_tabuleiro(tab):#le o tuplo principal
    ''' Verifica se e um tabuleiro'''
    numeros_poss = (1, -1, 0)
    if len(tab) != 3:         # Verifica o tamanho do tuplo principal.  
            return False    
    for i in range(len(tab)): # define para i os tuplos dentro do tuplo princ.
        if len(tab[i]) != 3:# Verifica o tamanho dos tuplos interiores. 
            return False
        for el in tab[i]:  #define para el os elementos dos tres tuplos interiores
            if type(el) != int:# verifica se os el dos tuple sao int.
                return False
            if el not in numeros_poss:
                return False
    return True
                
    
        
                
                
                 
def eh_posicao(n):#le um numero digitado pe
    '''Verificar se o digitado e uma posicao do tabuleiro'''
    num_disp = (1, 2, 3, 4, 5, 6, 7 ,8 ,9) # num de posicoes no tabuleiro
    if type(n) != int:   # verificacao que o n e uma possicao                  
        return False 
    else:
        for i in range(len(num_disp)):#define para i todos os el do tuplo
            if n == num_disp[i]: # verifica se n pertence ao tuplo
                return True
        else:
            return False

def obter_coluna(tab, n):
    if eh_tabuleiro(tab) == False:# Verificar se n pertence ao tuplo
        raise ValueError ('obter_coluna: algum dos argumentos e invalido')    
    colun = () # Acumulador de tuplos
    num_dispo = (1,2,3) # num de colunas disponiveis
    if n in num_dispo:
        for i in range(len(tab)):#definir para i os tuplos do tuplo principal
            colun += (tab[i][n - 1],) 
        return colun
    else:
        raise ValueError('obter_coluna: algum dos argumentos e invalido')
    


def obter_linha(tab, n):# le o tabuleiro e um valor n 
    '''Apresenta os elementos da linha selecionada pelo n'''
    if eh_tabuleiro(tab) == False:# Verificar se e um tabuleiro
        raise ValueError ('obter_linha: algum dos argumentos e invalido')    
    num_disp = (1, 2, 3) #valores que o n pode tomar devido ha haver tres linhas
    if n in num_disp: # verifica se n corresponde a uma linha da tabela
        return tab[n-1] # Apresenta a linha do correspondente n 
    else:
        raise ValueError('obter_linha: Algum dos argumentos e invalido')
    
def obter_diagonal(tab, n):
    '''indentificar as diagonais'''
    diagonal = () # Acumulador onde vai ficar a diagonal
    if eh_tabuleiro(tab) == False:# Verificar se e um tabuleiro
        raise ValueError ('obter_diagonal: algum dos argumentos e invalido')
    if n == 1:# selecionar se queremos a primeira diagonal
        for i in range(len(tab)):# defenir para i os tuplos interiores
#somar o primeiro elemento do 1tuplo, o segundo elemento do 2tuplo e o /terceiro elemento do 3tuplo
            diagonal += (tab[i][i],)
        return diagonal
    elif n == 2:
        for i in range(len(tab)):# defenir para i os tuplos interiores
            diagonal += (tab[n-i][i],)# inverso da soma referida
        return diagonal 
        
    else:
        raise ValueError('obter_diagonal: algum dos argumentos e invalido')
    
def tabuleiro_str(tab):
    '''Apresentar o tabuleiro na sua forma externa'''
    tab1 = '' #onde vai ser apresentado todos os elementos do tab 
    tab2 = '' #onde se vai concatenar os elementos com stings necessarias para o print funcionar bem
    if eh_tabuleiro(tab) == False: # Verificar se e um tabuleiro
        raise ValueError ('tabuleiro_str: o argumento e invalido')
    else:
        for i in tab:
            for i in range(len(tab)):
                for e in tab[i]:#substituir os termos de numeros para simbolos
                    if e == 1:
                        e = ' X '
                    elif e == -1:
                        e = ' O '
                    else:
                        e = '  '
                    tab1 = tab1 + e + '|'#Para os simbolos serem separados por |
            tab2 = (tab1[0:9]+' \n-----------\n '+ tab1[11:20] +' \n-----------\n '+ tab1[22:32])
            return tab2 # separacao da str nas respetivas linhas por []
def eh_posicao_livre(tab, n):#argumentos:tabela e a posicao no tab
    '''Verificar se o n e uma posicao livre no tabuleiro'''
    seq_nums = ()# acumulador para colocar os todos os numeros dos tuplos interiores
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
    if eh_posicao(n) == False:# Verificar se a posicao existe
        raise ValueError ('eh_posicao_livre: algum dos argumentos e invalido')
    for i in range(len(tab)):
        seq_nums += tab[i] # colocar os elementos dos tuplos interiores num so tuplo
    if seq_nums[n-1] == 0:# verificar se o numero do tuplo e uma posicao livre
        return True
    else:
        return False
def obter_posicoes_livres(tab):
    '''Determinar quais as posicoes livres no tabuleiro'''
    seq_pos = () # acumulador dos elementos pretendidos
    posicoes = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('obter_posicoes_livres: o argumentos e invalido')
    for n in posicoes: # definir para n os elementos do tuplo posicoes
        if eh_posicao_livre(tab, n) == True:# selecionar as posicoes que sao livres
            seq_pos += (posicoes[n-1], ) # colocar essas pos no tuplo acumulador
    return seq_pos
def jogador_ganhador(tab):
    '''Verificar de acordo com o tabuleiro'''
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('jogador_ganhador: o argumentos e invalido')
    num_lin_colun =(1,2,3) #numero associado as linhas e as colunas
    for l in num_lin_colun:#possibilidades de o jogador ganhar por preencher uma linha 
        if obter_linha(tab, l) == (1,1,1):
            return 1
        if obter_linha(tab, l) == (-1,-1,-1):
            return -1
    for c in num_lin_colun:#possibilidades de o jogador ganhar por preencher uma coluna 
        if obter_coluna(tab, c) == (1,1,1):
            return 1
        if obter_coluna(tab, c) == (-1,-1,-1):
            return -1
    num_diagonal = (1,2)#possibilidades de o jogador ganhar por preencher uma diagonal
    for d in num_diagonal:
        if obter_diagonal(tab, d) == (1,1,1):
            return 1
        if obter_diagonal(tab, d) == (-1,-1,-1):
            return -1
    return 0
   #nenhum dos casos anteriores foram verificados portanto ha impate
def marcar_posicao(tab, j, p):# tab-tabuleiro, j= jogador, p= posicao
    '''Marcar a decisao de um dos jogadores numa posicao livre'''
    tab1 = () # local para colocar todos os numeoros dos tuplos num so tuplo 
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('marcar_posicao: algum dos argumentos e invalido')
    if eh_posicao(p) == False: # Varificar se a posicao existe no tabuleiro
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    if j != -1 and j != 1:# varificar se foi selecionado um dos jogadores
        raise ValueError('marcar_posicao: algum dos argumentos e invalido')
    for i in range(len(tab)):#defenir para i as posicoes do tabuleiro
        tab1 += tab[i] # transforma os tuplos interiores num so tuplo 
    tabf = list(tab1)# transforma o tuplo referido numa lista para o manipular
    if j == 1: # caso seja escolhido o jogador 'X'
        if tabf[p-1] != 0:#(verificar se foi selecionado para marcar uma posicao livre
            raise ValueError('marcar_posicao: algum dos argumentos e invalido')
        else:
            tabf[p-1] = 1 #marcar a posicao livre com o numero do jogador 
            tab1 = (tuple(tabf[0:3]), tuple(tabf[3:6]), tuple(tabf[6:]))
            # colocar num tuplo tres tuplos contendo a marcacao feita
            # tabf - tabuleiro em lista que e depois transformado em tuplos 
        
    if j == -1:
        #verificar se foi selecionado para marcar uma posicao livre
        if tabf[p-1] != 0:
            raise ValueError('marcar_posicao: algum dos argumentos e invalido')
        else:
            tabf[p-1] = -1 #marcar a posicao livre com o numero do jogador 
            tab1 = (tuple(tabf[0:3]), tuple(tabf[3:6]) , tuple(tabf[6:])) 
            # colocar num tuplo tres tuplos contendo a marcacao feita
    return tab1


def escolher_posicao_manual(tab):
    '''Verificar e colocar um simbolo do jogador numa posicao livre'''  
    tab1 = [] # tuplo onde todos os numeros dos tuplos int ficam num so tuplo
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('escolher_posicao_manual: o argumentos e invalido')
    # introduzir a posicao livre por parte do jogador
    pl = eval(input('Turno do jogador. Escolha uma posicao livre: '))
    for i in range(len(tab)):
        tab1+= tab[i]
    if tab1[pl-1] == 0:# caso um dos elementos do tuplo total ser 0
            return pl  # corresponde a uma posicao livre
    else:
        raise ValueError('escolher_posicao_manual(tab): algum dos argumentos e invalido')
    
def escolher_posicao_auto(tab, j, e):
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError ('escolher_posicao_auto:o argumento e invalido')
    if j != -1 and j != 1:# varificar se foi selecionado um dos jogadores
        raise ValueError('algum dos argumentos e invalido')
    cantos_das_linhas = (1,3, 7, 9)
    leterais = (2, 4, 6, 8)
    def vitoria(tab, j):
        x = obter_posicoes_livres(tab)
        for i in x:
            tab_alt = marcar_posicao(tab, j, i)
            if jogador_ganhador(tab_alt) != 0:
                return i
        return None
    def bloqueio(tab, j):
        x = obter_posicoes_livres(tab)
        for i in x:
            tab_alt = marcar_posicao(tab, -j, i)
            if jogador_ganhador(tab_alt) != 0:
                return i
        return None
    def centro(tab):
        tab1 = []
        for i in range(len(tab)):
            tab1 += tab[i]
        if tab1[4] == 0:
            return 5
        return None
    def canto_vazio(tab):
        for i in range(len(tab)):
            tab1 += tab[i]        
        for c in cantos_das_linhas:
            if tab1[c] == 0:
                return c
            return None
    def lateral_vazio(tab):
        for i in range(len(tab)):
            tab1 += tab[i]        
        for l in laterais:
            if tab1[l] == 0:
                return l
            return None
    if e == 'Basico':
        if centro(tab) != None:
            return 5
        if canto_vazio(tab) != None:
            return c
        if lateral_vazio(tab) != None:
            return l
        
        
        
    
    