# Luis Marques numero: 199265


# TAD posicao -  Usado para representar uma posicao do tabuleiro de jogo

# construtor
# representacao interna -> c -> coluna e l -> linha 
#R[(c,l)] = { 'coluna':c, 'linha':l}
def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    """ recebe duas cadeias de carateres correspondentes a coluna c
e a linha l de uma posicao e devolve a posicao correspondente."""
    # usando funcoes auxiliares verificar se o que e introduzido na funcao e 
    #uma coluna e um linha 
    if verif_coluna(c) and verif_linha(l):
        return { 'coluna' : c, 'linha': l}
    else:
        raise ValueError('cria_posicao: argumentos invalidos')
    
def verif_coluna(x):
    # verif_coluna: str -> booleano
    """ Recebe uma cadeia de caracteres e verifica se corresponde 
    a uma coluna.""" 
    return x in ('a', 'b', 'c')
def verif_linha(x):
    # verif_linha: str -> booleano
    """ Recebe uma cadeia de caracteres e verifica se corresponde 
    a uma linha.""" 
    return x in ('1', '2', '3')
def cria_copia_posicao(p):
    # cria_copia_posicao: posicao -> posicao
    """ Recebe uma posicao e cria uma outra posicao com igual 
    coordenadas a posicao copiada."""
    #verificar se o que foi introduzido na funcao e uma posicao
    if eh_posicao(p) == True:
        return { 'coluna': p['coluna'], 'linha': p['linha']}
    else:
        raise ValueError('cria_copia_posicao: argumento invalido')

# seletores 

def obter_pos_c(p):
    # obter_pos_c: posicao -> str
    """ Devolve a componente coluna c da posicao p. """
    return p['coluna']
def obter_pos_l(p):
    # obter_pos_l: posicao -> str
    """ Devolve a componente linha l da posicao p."""
    return p['linha']

# Reconhecedores

def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    """ Devolve True caso o seu argumento seja um TAD posicao 
    e False caso contrario"""
    if isinstance(arg, (dict)):
        # condicoes para que o argumento seja uma posicao e necessario que 
        # para alem de ser um dicinario, tem de possuir duas chaves chamadas
        # coluna e linha e nessas chaves tem de estar  respetivamente 
        #associada uma coluna e uma linha
        if len(arg) == 2 and 'coluna' in arg and 'linha' in arg:
            if verif_coluna(arg['coluna']) and verif_linha(arg['linha']):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Teste

def posicoes_iguais(p1, p2):
    # posicoes iguais: posicao x posicao -> booleano
    """Devolve True apenas se p1 e p2 sao posicoes e sao
iguais."""
    return eh_posicao(p1) and eh_posicao(p2) and \
           obter_pos_c(p1) == obter_pos_c(p2) and \
           obter_pos_l(p1) == obter_pos_l(p2)

# Transformador

def posicao_para_str(p):
    # posicao_para_str: posicao -> str
    """  Devolve a cadeia de caracteres 'cl' que representa o seu
argumento, sendo os valores c e l as componentes coluna e linha de p. """
    # somar a componente coluna da posicao com a componete linha da posicao
    # ja que esse compontes sao representados por strigs e estas sao capazes
    #de serem somadas
    return obter_pos_c(p) + obter_pos_l(p)
# funcao de alto nivel
def obter_posicoes_adjacentes(p):
    # obter posicoes adjacentes: posicao -> tuplo de posicoes
    """  devolve um tuplo com as posicoes adjacentes a posicao
p de acordo com a ordem de leitura do tabuleiro."""
     # verificar para cada posicao existente no tabuleiro as suas respetivas
     # posicoes adjacentes
    if posicao_para_str(p) == 'a1':
        return ( cria_posicao('b','1'), cria_posicao('a', '2') , \
                 cria_posicao('b', '2'))
    if posicao_para_str(p) == 'a2':
        return (cria_posicao('a', '1'), cria_posicao('b','2'), \
                cria_posicao('a','3'))
    if posicao_para_str(p) == 'a3':
        return (cria_posicao('a','2'), cria_posicao('b','2'), \
                cria_posicao('b','3'))
    if posicao_para_str(p) == 'b1':
        return (cria_posicao('a','1'), cria_posicao('c','1'), \
                cria_posicao('b','2'))
    if posicao_para_str(p) == 'b2':
        return (cria_posicao('a','1'), cria_posicao('b','1'), \
                cria_posicao('c','1') , cria_posicao('a','2'), \
                cria_posicao('c','2'), cria_posicao('a','3')\
                , cria_posicao('b','3'), cria_posicao('c','3'))
    if posicao_para_str(p) == 'b3':
        return (cria_posicao('b','2'), cria_posicao('a','3'), \
                cria_posicao('c','3'))
    if posicao_para_str(p) == 'c1':
        return (cria_posicao('b','1'), cria_posicao('b','2'), \
                cria_posicao('c','2'))
    if posicao_para_str(p) == 'c2':
        return (cria_posicao('c','1'), cria_posicao('b','2'), \
                cria_posicao('c','3'))
    if posicao_para_str(p) == 'c3':
        return (cria_posicao('b','2'), cria_posicao('c','2'), \
                cria_posicao('b','3'))
    
# TAD peca -> usado para representar as pecas do jogo.
#representacao interna : 'X' -> pecaX , 'O' -> pecaO e '' -> pecalivre
#R[(s)] = { 'peca':s}
# construtor

def cria_peca(s):
    # cria peca: str -> peca
    """  recebe uma cadeia de carateres correspondente ao identificador
de um dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ') e devolve a
peca correspondente. """
    # usando funcoes auxiliares para verificar se o que e introduzido 
    # corresponde a um indentificador de um dos jogadores ou uma peca livre
    if verif_pecaX(s) or verif_pecaO(s) or verif_peca_livre(s): 
        return {'peca':s}
    else:
        raise ValueError('cria_peca: argumento invalido')

def verif_pecaX(x):
    # verif_pecaX: str -> booleano
    """ Verificar se foi escolhida a peca X """
    return x == 'X' 
def verif_pecaO(x):
    # verif_pecaO: str -> booleano
    """ Verificar se foi escolhida a peca O """
    return x == 'O'
def verif_peca_livre(x):
     # verif_peca_livre: str -> booleano
    """ Verificar se foi escolhida a peca livre """
    return x == ' '
def cria_copia_peca(j):
    #cria_copia_posicao: posicao -> posicao
    """Recebe uma posicao e devolve uma copia nova da posicao.""" 
    # verificar se o que foi introduzido na funcao e uma peca, verificado se e
    # a peca 'X' ou a peca 'O' ou a peca livre
    if (verif_pecaX(j['peca']) or verif_pecaO(j['peca']) or \
       verif_peca_livre(j['peca'])) and eh_peca(j) == True:
        return {'peca':j['peca']}
    else:
        raise ValueError('cria_copia_peca: argumento invalido')
    
# Reconhecedor

def eh_peca(arg):
    #  eh peca: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD peca e False
caso contrario."""
    if isinstance(arg, (dict)):
        # Para o argumento ser uma peca e preciso que para alem de ser um 
        # dicionario seja constituinda por uma so chave denominada peca 
        if len(arg) == 1 and 'peca' in arg:
            # verificar se na chave peca existe um indentificador de um dos dois
            #jogadores ou se e uma peca livre
            if verif_pecaX(arg['peca']) or verif_pecaO(arg['peca']) or \
               verif_peca_livre(arg['peca']):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# Teste

def pecas_iguais(j1, j2):
    #pecas_iguais: peca x peca -> booleano
    """Devolve True apenas se j1 e j2 sao pecas e sao iguais."""
    # eh_peca para verificar se ambas os argumentos sao pecas e se chave peca
    # de ambas tem como elemento um indentificador de um dos dois 
    #jogadores ou se e uma peca livre
    return eh_peca(j1) and eh_peca(j2) and j1['peca'] == j2['peca']
# Transformador
def peca_para_str(j):
    # peca para str : peca -> str
    """ Devolve a cadeia de caracteres que representa o jogador dono
da peca, isto e, '[X]', '[O]' ou '[ ]'."""
    return '[' + j['peca'] + ']'

# Funcao de alto nivel
def peca_para_inteiro(j):
    # peca_para_inteiro: peca -> N
    """ Devolve um inteiro valor 1, -1 ou 0, dependendo se a peca e do
jogador 'X', 'O' ou livre, respetivamente."""
    if peca_para_str(j) == '[X]':
        return 1
    if peca_para_str(j) == '[O]':
        return -1
    if peca_para_str(j) == '[ ]':
        return 0
    
#TAD tabuleiro -> e usado para representar um tabuleiro do jogo do moinho de 3x3
#as posicoes e as pecas dos jogadores que nele sao colocadas.

# Representacao interna: o tabuleiro e constituindo por uma lista onde dentro
# desta existem tres sublistas que correspondem a cada linha do tabuleiro\
# contendo nelas tres posicoes onde se vai colocar pecas 

# Construtor

def cria_tabuleiro():
    # cria tabuleiro: {} -> tabuleiro
    """ Devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes
ocupadas por pecas de jogador."""
    return [['[ ]','[ ]','[ ]'], ['[ ]','[ ]','[ ]'],\
                ['[ ]', '[ ]', '[ ]']]
    

def cria_copia_tabuleiro(t):
    #cria_copia _tabuleiro: tabuleiro -> tabuleiro
    """Recebe um tabuleiro e devolve uma copia nova do tabuleiro."""
    # Como a copia do tabuleiro nao pode ser o tabuleiro e defenido um 
    #acumulador onde se vai colocar sublistas indenticas a do tabuleiro
    copia = []
    # verificar se o argumento introduzido e um tabuleiro
    if eh_tabuleiro(t):
        # Por cada sublista no tabuleiro
        for l in t:
            # colocar as sublistas no tabuleiro
            copia = copia + [l[:]]
        return copia
    else:
        raise ValueError('cria_copia_tabuleiro: argumento invalido')
# seletores

def posicoes_tab(t,p):
    #obter peca: tabuleiro x posicao -> str
    """Devolve a peca_para_str que esta na posicao p do 
    tabuleiro."""
    # usando os indices das listas correspondi a cada um dos elementos das
    # sublistas a respetiva posicao
    if posicao_para_str(p) == 'a1':
        return t[0][0]
    if posicao_para_str(p) == 'a2':
        return t[1][0]
    if posicao_para_str(p) == 'a3':
        return t[2][0]
    if posicao_para_str(p) == 'b1':
        return t[0][1]
    if posicao_para_str(p) == 'b2':
        return t[1][1]
    if posicao_para_str(p) == 'b3':
        return t[2][1]
    if posicao_para_str(p) == 'c1':
        return t[0][2]
    if posicao_para_str(p) == 'c2':
        return t[1][2]
    if posicao_para_str(p) == 'c3':
        return t[2][2]
    
def obter_peca(t,p):
    #obter peca: tabuleiro x posicao -> peca
    """Devolve a peca na posicao p do tabuleiro. Se a posicao nao
estiver ocupada, devolve uma peca livre."""
    # De acordo com a posicao selecionada e a representacao de um dos jogadores
    # ou peca livre existente nessa posicao e devolvida a respetiva peca
    if posicoes_tab(t,p) == '[ ]':
        return cria_peca(' ')
    if posicoes_tab(t,p) == '[X]':
        return (cria_peca('X'))
    if posicoes_tab(t,p) == '[O]':
        return (cria_peca('O'))
    
# Considerei exteriomente as representacao das colunas e das linhas em tuplos
# que me auxiliaram em funcoes cruciais para o funcionamento do jogo
colunas = ('a', 'b', 'c')
linhas = ('1', '2', '3')

def obter_vetor(t,s):
    # obter_vetor : tabuleiro x str -> tuplo de pecas
    """Devolve todas as pecas da linha ou coluna 
    especificada pelo seu argumento."""
     # cria-se um acumulador onde se vao colocar as pecas de uma das linhas ou
     # colunas de acordo com o que e introduzido no s.
    tuplo_pecas = ()
    # se a string introduzida e uma das linhas
    if s in linhas:
        # coloca-se tuplo acumulador as pecas dessa linha ou seja
        # coloca-se a primeira peca de cada coluna.
        for i in colunas:
            tuplo_pecas = tuplo_pecas + (obter_peca(t,cria_posicao(i,s)),)
        return tuplo_pecas
    #se o string introduzida e uma das colunas
    if s in colunas:
        # coloca-se o tuplo acumulador as pecas dessa coluna ou seja 
        # coloca-se a primeira peca de cada linha 
        for i in linhas:
            tuplo_pecas = tuplo_pecas + (obter_peca(t,cria_posicao(s,i)),)
        return tuplo_pecas

# Modificadores

def coloca_peca(t,j,p):
    # coloca peca: tabuleiro x peca x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t colocando a peca j
na posicao p, e devolve o proprio tabuleiro."""
    # Para cada linha
    for l in linhas:
        # Verificar se a peca introduzida e uma das apresentadas abaixo e se 
        # esta se encontra na coluna 'a'
        if (j==cria_peca('X') or j==cria_peca('O') or j==cria_peca(' '))\
           and p == cria_posicao('a',l):
            # coloca-se a peca no tabuleiro , usei o int na linha ja 
            #que estas sao representadas por numeros no formato string e 
            # devido as condicoes dos indices subtrai um para colocar a peca
            # na posicao certa pois caso nao o fizesse existiria 4 linhas
            # o que nao esta correto e o zero do indice seguinte refere-se a
            # coluna 'a'
            t[int(l)-1][0] = peca_para_str(j)
    # Ocorre o mesmo mas so para a coluna 'b' sendo ai a origem do 1 usado
    # no indice do tabuleiro
    for l in linhas:
        if (j==cria_peca('X') or j==cria_peca('O') or j==cria_peca(' '))\
           and p == cria_posicao('b',l):
            t[int(l)-1][1] = peca_para_str(j)
        # Ocorre o mesmo mas so para a coluna 'c' sendo ai a origem do 2 usado
        # no indice do tabuleiro    
    for l in linhas:
        if (j==cria_peca('X') or j==cria_peca('O') or j==cria_peca(' '))\
           and p == cria_posicao('c',l):
            t[int(l)-1][2] = peca_para_str(j)
    return t 

def remove_peca(t,p):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t removendo a 
    peca da posicao p, e devolve o proprio tabuleiro."""
    # Para remover decedi que ao ser introduzido o tabuleiro e a posicao selecio
    #nada colocava-se uma peca livre nessa posicao removendo caso houvesse uma
    # peca 'X' ou peca 'O'
    return coloca_peca(t,cria_peca(' '),p)

def move_peca(t, p1, p2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    """Modifica destrutivamente o tabuleiro t movendo a 
    peca que se encontra na posicao p1 para a posicao p2, 
    e devolve o proprio tabuleiro."""
    # verificar se as posicoes selecionadas sao iguais, no caso devolve-se o 
    # tabuleiro sem qualquer alteracao
    if posicoes_iguais(p1,p2):
        return t
    else:
        # Senao coloca-se a peca que esta na posicao p1 na p2 e como se trata
        # de um movimento elimina-se a peca na posicao p1
        return coloca_peca(t,obter_peca(t,p1),p2) and remove_peca(t,p1)
# Reconhecedores

def todas_pecas_tab(t):
    # todas_pecas_tab: tabuleiro -> tuplo de pecas
    """funcao auxiliar que devolve num tuplo, todas as pecas existentes no 
    taboleiro, incluindo as pecas livres."""
    #Acumulador onde vao ser colocadas todas as pecas do tabuleiro de seguida\
    #num tuplo
    todas_as_pecas = ()
    # ciclo for que percorre as linhas e coloca as pecas de cada linha no tuplo\
    # acumulador por intermedio da funcao obter_vetor restrigida as linhas
    for l in linhas:
        todas_as_pecas = todas_as_pecas + (obter_vetor(t,l))
    return todas_as_pecas

def conta_pecas(t,j):
    # conta_pecas(t,j): tabuleiro x peca -> numero de pecas
    """funcao auxiliar que devolve o numeoro de um determinado tipo de peca
    existente no tabuleiro."""
    # Acumulador do numero de um determinado tipo de peca
    n_peca = 0
    # Por intermedio do ciclo for percorres-se todo o tuplo formado pela \
    # funcao auxiliar anterior contendo as pecas
    for i in range(9):
        # caso umas das pecas correspende a peca introduzida soma-se 1 ao\
        #acumulador
        if todas_pecas_tab(t)[i] == j:
            n_peca = n_peca + len(todas_pecas_tab(t)[i])
    return n_peca

def contar_vencedores(tab):
    #contar_vencedores(tab): tabuleiro -> numero de vencedores
    """funcao auxiliar que recebe um tabuleiro e devolve o numero de vezes 
    que os jogadores estao na condicao de vencer, ou seja se as pecas de um dos 
    jogadores aparecem de seguida numa linha ou numa coluna"""
    # inicialmente nao existem vencedores
    vencedores = 0
    # ciclo for para percorre as pecas das linhas e colunas
    for i in range(3):
        # caso se verifique uma destas condicoes de vitoria no tabuleiro introduzido\
        #ou seja uma linha ou uma coluna so com pecas de um determinado jogador\
        # adiciona-se ao acumulador vencedor um valor. 
        linha = obter_vetor(tab, linhas[i])
        if linha == (cria_peca('X'),cria_peca('X'),cria_peca('X')):
            vencedores = vencedores + 1 
        if linha == (cria_peca('O'),cria_peca('O'),cria_peca('O')):
            vencedores = vencedores + 1
        coluna = obter_vetor(tab, colunas[i])
        if coluna == (cria_peca('X'),cria_peca('X'),cria_peca('X')):
            vencedores = vencedores + 1
        if coluna == (cria_peca('O'),cria_peca('O'),cria_peca('O')):
            vencedores = vencedores + 1
    # No fim de se verificar todo o tabuleiro devolve-se o numero de vencedores
    return vencedores


def ganhador_nao_simultaneo(t):
    # ganhador_nao_simultaneo(t): tabuleiro -> booleano
    """funcao auxiliar que devolve True caso o argumento seja 
    um TAD tabuleiro, mais especificamente devolve True caso nao haja dois
    ganhadores no mesmo tabuleiro"""
    if contar_vencedores(t) == 2:
        return False
    else:
        return True  
            
def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    """Devolve True caso o seu argumento seja um TAD 
tabuleiro e False caso contrario. Um tabuleiro valido pode ter um maximo de 3 
pecas de cada jogador, nao pode conter mais de 1 peca mais de um jogador que do
contrario, e apenas pode haver um ganhador em simultaneo."""
    # As 3 linhas asseguir servem para verificar a estrutura do tabuleiro
    # que ja foi descrita anteriormente
    if isinstance(arg, list) and len(arg) == 3:
        if isinstance(arg[0], list) and isinstance(arg[1],list) and \
           isinstance(arg[2],list) and len(arg[0]) == 3 and len(arg[1]) == 3\
           and len(arg[2]) == 3:
            # verificar se os elementos das sublistas sao pecas
            if eh_peca(obter_peca(arg,cria_posicao('a','1'))) and\
               eh_peca(obter_peca(arg,cria_posicao('a','2'))) and\
               eh_peca(obter_peca(arg,cria_posicao('a','3'))) and\
               eh_peca(obter_peca(arg,cria_posicao('b','1'))) and\
               eh_peca(obter_peca(arg,cria_posicao('b','2'))) and\
               eh_peca(obter_peca(arg,cria_posicao('b','3'))) and\
               eh_peca(obter_peca(arg,cria_posicao('c','1'))) and\
               eh_peca(obter_peca(arg,cria_posicao('c','2'))) and\
               eh_peca(obter_peca(arg,cria_posicao('c','3'))):
                # Verificar o numero maximo de pecas 'X' e 'O' que e 3 e\
                # e se existe um so vencedor
                if conta_pecas(arg, cria_peca('X')) <= 3 and\
                   conta_pecas(arg, cria_peca('O')) <= 3 and \
                   ganhador_nao_simultaneo(arg):
                    if (conta_pecas(arg, cria_peca('X')) - \
                        conta_pecas(arg, cria_peca('O')) in [0,1]) or \
                       (conta_pecas(arg, cria_peca('O')) - \
                        conta_pecas(arg, cria_peca('X')) in [0,1]):                       
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
def eh_posicao_livre(t,p):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    """Devolve True apenas no caso da posicao p do 
    tabuleiro corresponder a uma posicao livre."""
    return obter_peca(t,p) == cria_peca(' ')
# Teste
def tabuleiros_iguais(t1,t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    """Devolve True apenas se t1 e t2 sao tabuleiros 
    e sao iguais."""
    return ((eh_tabuleiro(t1) == True and eh_tabuleiro(t2) == True) and\
            (t1 == t2))

# Transformador

def tabuleiro_para_str(t):
    #  tabuleiro_para_str : tabuleiro -> str 
    """Devolve a cadeia de caracteres que representa o 
    tabuleiro."""
    
    return ('   a   b   c\n')\
           +('1 '+ t[0][0] + '-' + t[0][1] + '-' + t[0][2] + '\n')\
           + ('   | \\ | / |\n')\
           +('2 ' + t[1][0] + '-' + t[1][1] + '-' + t[1][2] + '\n')\
           + ('   | / | \\ |\n')\
           + ('3 ' + t[2][0] + '-' + t[2][1] + '-' + t[2][2])

def inteiro_para_peca_str(n):
    # inteiro_para_peca: N -> peca_para_str
    """ funcao auxiliar que devolve uma cadeia de caracteres que representa o 
    jogador dono da peca, isto e, '[X]', '[O]' ou '[ ]' 
    dependendo se o inteiro digitado for de valor 1, -1 ou 0, respetivamente."""    
    if n == 1:
        return '[X]'
    if n == -1:
        return '[O]'
    if n == 0:
        return '[ ]'


def tuplo_para_tabuleiro(t):
    # tuplo para tabuleiro: tuplo -> tabuleiro
    """Devolve o tabuleiro que e representado 
    pelo tuplo t com 3 tuplos, cada um deles contendo 
    3 valores inteiros iguais a 1, -1 ou 0."""
    # acumulador onde vai ser colocadas as sublistas com as respetivas\
    # pecas_para_str
    tabuleiro = []
    # Percorre-se todas as linhas do tabuleiro e coloca por intermedio das colu\
    #nas  todas as pecas numa lista
    for l in linhas:
        tabuleiro = tabuleiro\
            +[inteiro_para_peca_str(posicoes_tab(t,cria_posicao('a',l))),]\
            +[inteiro_para_peca_str(posicoes_tab(t,cria_posicao('b',l))),]\
            +[inteiro_para_peca_str(posicoes_tab(t,cria_posicao('c',l))),]
        # organizar lista de acordo com um tabuleiro
    return [tabuleiro[0:3],tabuleiro[3:6],tabuleiro[6:9]]
      
    
                    
# Alto nivel        
def obter_ganhador(t):
    # obter_ganhador : tabuleiro -> peca
    """Devolve uma peca do jogador que tenha as suas 3 pecas em linha
na vertical ou na horizontal no tabuleiro. Se nao existir nenhum ganhador, 
devolve uma peca livre."""
    # Percorre por intermedio do ciclo for todas as linhas e colunas \
    # de forma a verificar se existe um ganhador
    for l in linhas:
        if (obter_vetor(t,l) == \
            (cria_peca('X'),cria_peca('X'),cria_peca('X'))):
            return cria_peca('X')
        if (obter_vetor(t,l) == \
            (cria_peca('O'),cria_peca('O'),cria_peca('O'))):
            return cria_peca('O')        
    for c in colunas:
        if (obter_vetor(t,c) == \
            (cria_peca('X'),cria_peca('X'),cria_peca('X'))):
            return cria_peca('X')
        if (obter_vetor(t,c) == \
            (cria_peca('O'),cria_peca('O'),cria_peca('O'))):
            return cria_peca('O')                
    else:
        return cria_peca(' ')

def obter_posicoes_livres(t):
    # obter posicoes livres: tabuleiro -> tuplo de posicoes
    """Devolve um tuplo com as posicoes nao ocupadas pelas pecas
de qualquer um dos dois jogadores na ordem de leitura do tabuleiro."""
    # Acumulador de pecas livres
    pos_livres = ()
    # Percorrer por intermedio do ciclo for as linhas e as colunas de forma
    for l in linhas:
        for c in colunas:
            # verificar se a posicao e livre
            if eh_posicao_livre(t,cria_posicao(c,l)):
                pos_livres = pos_livres + (cria_posicao(c,l),)
    # Retornar todas as posicoes livres
    return pos_livres

def obter_posicoes_jogador(t,j):
    # obter posicoes jogador : tabuleiro x peca -> tuplo de posicoes
    """Devolve um tuplo com as posicoes ocupadas pelas pecas
j de um dos dois jogadores na ordem de leitura do tabuleiro."""
    # Mesmo formato da funcao anterior mas em vez de acumular pecas livres\
    # acumula o tipo de peca introduzido:
    pos_jogador = ()
    for l in linhas:
        for c in colunas:
            if obter_peca(t,cria_posicao(c,l)) == j:
                pos_jogador = pos_jogador + (cria_posicao(c,l),)
    return pos_jogador

# Funcoes adicionais

def obter_movimento_manual(tab,j):
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    """ Funcao auxiliar que recebe um tabuleiro e uma peca de um jogador, 
    e devolve um tuplo com uma ou duas posicoes que representam uma posicao 
    ou um movimento introduzido manualmente pelo jogador."""
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError('obter_movimento_manual:algum \
        dos argumentos e invalido')
    if eh_peca(j) == False:# varificar se foi selecionado um dos jogadores
        raise ValueError('obter_movimento_manual: \
        algum dos argumentos e invalido')
    # Verificar se esta nas condicoes para colocar
    if ((len(obter_posicoes_jogador(tab,cria_peca('X')))) <= 3 and \
        (len(obter_posicoes_jogador(tab,cria_peca('O')))) < 3) or \
        ((len(obter_posicoes_jogador(tab,cria_peca('X')))) < 3 and \
        (len(obter_posicoes_jogador(tab,cria_peca('O')))) <= 3):
        # Os input e transformado em uma string sendo depois manipulado
        p1 = (str(input('Turno do jogador. Escolha uma posicao: '),))
        # verificar se o que foi introduzido e uma peca_para_str contem dois elementos\
        # e se e uma posicao_livre
        if len(p1) == 2:
            if (verif_coluna(p1[0]) and verif_linha(p1[1])) == True and \
               cria_posicao(p1[0],p1[1]) in obter_posicoes_livres(tab):
                return (cria_posicao(p1[0],p1[1]),)
            else:
                raise ValueError ('obter_movimento_manual: escolha invalida') 
        else:
            raise ValueError ('obter_movimento_manual: escolha invalida')
    # Verificar as condicoes de movimentacao
    if (tab != cria_tabuleiro() and eh_tabuleiro(tab)) == True and \
       obter_ganhador(tab) == cria_peca(' ') and \
       len(obter_posicoes_jogador(tab,cria_peca('X'))) == 3 and\
       len(obter_posicoes_jogador(tab,cria_peca('O'))) == 3:
        p2 = (str(input('Turno do jogador. Escolha um movimento: ')))
        # verificar se o input e um movimento  
        if len(p2) == 4:
            if (verif_coluna(p2[0]) and verif_linha(p2[1])) == True and \
               (verif_coluna(p2[2]) and verif_linha(p2[3])) == True:
                # Verificar se pode haver movimento das peca do jogador \
                #entre posicoes
                if ((cria_posicao(p2[0],p2[1]) \
                     in obter_posicoes_jogador(tab,j)) 
                    and (cria_posicao(p2[2],p2[3]) in \
                         obter_posicoes_livres(tab)) 
                    and (cria_posicao(p2[2],p2[3]) in \
                         obter_posicoes_adjacentes(cria_posicao(p2[0],p2[1]))))\
                   == True  :
                    # Apresenar o movimento
                    return (cria_posicao(p2[0],p2[1]),) +\
                           (cria_posicao(p2[2],p2[3]),)
                # Senao verificar se todas as pecas do jogador estao bloqueadas
                elif esta_bloqueada(tab,j): 
                    if (cria_posicao(p2[0],p2[1]) in \
                        obter_posicoes_jogador(tab,j)) and\
                       posicoes_iguais(cria_posicao(p2[0],p2[1]),\
                                       cria_posicao(p2[2],p2[3])):
                        return (cria_posicao(p2[0],p2[1]),) +\
                               (cria_posicao(p2[2],p2[3]),)
                    else:
                        raise ValueError('obter_movimento_manual: escolha \
                        invalida')
                else:
                    raise ValueError('obter_movimento_manual: escolha invalida')                    
            else:
                raise ValueError ('obter_movimento_manual: escolha invalida')
        else:
            raise ValueError ('obter_movimento_manual: escolha invalida')
    else:
        raise ValueError ('obter_movimento_manual: escolha invalida')
    
# Considerei exteriomente as representacao das cantos e das laterais em tuplos
# que me auxiliaram em funcoes cruciais para o funcionamento do jogo    
cantos = (cria_posicao('a','1'),cria_posicao('c','1'),cria_posicao('a','3'),\
          cria_posicao('c','3'))
laterais =  (cria_posicao('b','1'),cria_posicao('a','2'),cria_posicao('c','2'),\
          cria_posicao('b','3'))
def inteiro_para_peca(n):
    # inteiro_para_peca: N -> peca
    """ funcao auxiliar que devolve uma peca, isto e, 'X', 'O' ou ' ' 
    dependendo se o inteiro digitado for de valor 1, -1 ou 0, respetivamente."""    
    if n == 1:
        return cria_peca('X')
    if n == -1:
        return cria_peca('O')
    if n == 0:
        return cria_peca(' ')
    
def valor_tabuleiro(tab):
    # valor_tabuleiro: tabuleiro -> N
    """ funcao auxiliar que devolve um numero correspondente ao jogador que
    ganhou ou devolve o numero correspondente ao empate"""
    if obter_ganhador(tab) == cria_peca('X'):
        return +1
    if obter_ganhador(tab) == cria_peca('O'):
        return -1
    if obter_ganhador(tab) == cria_peca(' '):
        return 0   
def jogador_adversario(j):
    # jogador_adversario: peca -> peca do adversario
    """ funcao auxiliar que recebe a peca de um dos jogadores e devolve a peca 
    jogador adversario"""
    if j == cria_peca('X'):
        return cria_peca('O')
    if j == cria_peca('O'):
        return cria_peca('X')
            
def minimax(tab,jgdr,pronf,seq_movimentos):
    # minimax: tabuleiro x peca x pronfundidade x sequencia_de_movimentos -> 
    # valor_tabuleiro x sequencia_de_movimentos
    """ O minimax e um algoritmo recursivo que pode 
    sumarizar-se como a escolha do melhor movimento para um
proprio assumindo que o adversario ira a escolher o pior possivel."""
    # A funcao esta descrita no enunciado e e importante dizer que associei a\
    # a melhor sequencia com None
    melhor_seq_movimentos = None
    if obter_ganhador(tab) == jgdr or obter_ganhador(tab) == \
       jogador_adversario(jgdr) or (pronf == 0):
        return (valor_tabuleiro(tab),seq_movimentos)
    else:
        best_result = peca_para_inteiro(jogador_adversario(jgdr))
        for p_j in obter_posicoes_jogador(tab,jgdr):
            for p_a in obter_posicoes_adjacentes(p_j):
                if p_a in obter_posicoes_livres(tab):
                    jogada1 = move_peca(cria_copia_tabuleiro(tab),p_j,p_a)
                    new_result,new_seq_mov = \
                        minimax(jogada1,jogador_adversario(jgdr),pronf - 1, \
                                seq_movimentos + ((p_j,p_a)))
                    if melhor_seq_movimentos == None or (jgdr == cria_peca('X')\
                        and new_result > best_result) or\
                       (jgdr == cria_peca('O') and new_result < best_result):
                        best_result,melhor_seq_movimentos = \
                            new_result,new_seq_mov
        return best_result,melhor_seq_movimentos
     
def vitoria(tab,j):
    # vitoria: tabuleiro x peca -> posicao
    """ funcao auxiliar em que se o jogador tiver duas das suas pecas 
    em linha e uma posicao livre entao deve marcar na posicao 
    livre  que e devolvida(ganhando o jogo)""" 
    x = obter_posicoes_livres(tab)
    # Percorre as posicoes livres e coloca_peca nessas posicoes que caso \
    # resultem em vitoria devolve a posicao e remove a peca da possicao\
    # para a funcao fase_colocao nao tenha o tabuleiro alterado caso nao \
    # resulte numa vitoria
    for i in x:
        tab_alt = coloca_peca(tab, j, i)
        if eh_tabuleiro(tab_alt):
            if obter_ganhador(tab_alt) != cria_peca(' '):
                remove_peca(tab_alt,i)
                return i
            else:
                remove_peca(tab_alt,i)
                
        else:
            remove_peca(tab_alt,i)
            return None

   

def bloqueio(tab, j):
    # bloqueio: tabuleiro x peca -> posicao
    """funcao auxiliar em que se o adversario tiver duas das suas pecas em linha 
    e uma posicao livre entao deve marcar na posicao livre  que e devolvida
    (para bloquear o adversario)"""
    # Usei a funcao peca_para_inteiro para ajudar no colocar a peca do\
    #adversario 
    j_n = peca_para_inteiro(j)
    x = obter_posicoes_livres(tab)
    for i in x:
        tab_alt = coloca_peca(tab,inteiro_para_peca(-(j_n)),i)
        if obter_ganhador(tab_alt) != cria_peca(' '):
            remove_peca(tab_alt,i)
            return i
        else:
            remove_peca(tab_alt,i)
            
                

def centro(tab):
    # centro: tabuleiro -> posicao
    """ funcao auxiliar em que se a posicao central estiver livre
    entao devolve a posicao central onde se vai jogar"""
    if cria_posicao('b','2') in obter_posicoes_livres(tab):
        return (cria_posicao('b','2'),)
    else:
        return None
def canto_vazio(tab):
    # canto_vazio: tabuleiro -> posicao 
    """ funcao auxiliar em que se um canto for uma posicao livre
entao devolve a posicao desse canto, na qual se vai jogar"""
    for i in obter_posicoes_livres(tab):
        if i in cantos:
            return i
    else:
        return None
  
def lateral_vazio(tab):
    #lateral_vazio: tabuleiro -> posicao
    """ funcao auxiliar em que se uma posicao lateral 
    (que nem e o centro, nem um canto) for livre
    entao devolve essa lateral onde se vai jogar."""
    for i in obter_posicoes_livres(tab):
        if i in laterais:
            return i
    else:
        return None
    
    
def fase_colocacao(tab,j):
    # fase_colocacao: tabuleiro x peca -> posicao
    """ funcao auxiliar que recebe um tabuleiro e um peca e devolve um tuplo
    contendo a posicao em que o jogador dessa peca vai jogar de acordo com
    os criterios defenidos em funcoes anteriores"""
    if vitoria(tab,j) != None:
        return (vitoria(tab,j),)        
    if bloqueio(tab,j) != None:
        return (bloqueio(tab,j),)        
    if centro(tab) != None:
        return centro(tab)
    if canto_vazio(tab) != None:
        return (canto_vazio(tab),)
    if lateral_vazio(tab) != None:
        return (lateral_vazio(tab),)
def esta_bloqueada(tab,j):
    # esta_bloqueada: tabuleiro x peca -> booleano
    """ Funcao auxiliar que permite ver se todas as pecas de um determinado 
    jogador estao bloqueadas caso estejam retorna True senao retorn False"""
    if j in (cria_peca('X'),cria_peca('O')):
        for p in obter_posicoes_jogador(tab,j):
            for adj in obter_posicoes_adjacentes(p):
                if eh_posicao_livre(tab, adj):
                    return False
        return True
    
   
def obter_movimento_auto(tab,j,modo):
    # obter_movimento_auto: tabuleiro x peca x modo_de_jogo -> movimento
    """Funcao auxiliar que recebe um tabuleiro, uma peca de um jogador e uma 
    cadeia de carateres representando o nivel de dificuldade do jogo, e devolve 
    um tuplo com uma ou duas posicoes que representam uma posicao 
    ou um movimento escolhido automaticamente."""
    if eh_tabuleiro(tab) == False:# Verifica se e um tabuleiro
        raise ValueError('obter_movimento_auto:algum dos argumentos e invalido')
    if eh_peca(j) == False:# varificar se foi selecionado um dos jogadores
        raise ValueError('obter_movimento_auto: \
        algum dos argumentos e invalido')
    if modo not in ('facil','normal','dificil'):# verificar se e um modo
        raise ValueError('obter_movimento_auto: algum dos argumentos\
        e invalido')

    if modo == 'facil':
        if  ((len(obter_posicoes_jogador(tab,cria_peca('X')))) <= 3 and \
            (len(obter_posicoes_jogador(tab,cria_peca('O')))) < 3) or \
            ((len(obter_posicoes_jogador(tab,cria_peca('X')))) < 3 and\
             (len(obter_posicoes_jogador(tab,cria_peca('O')))) <= 3):
            colocacao = fase_colocacao(tab,j)
            if eh_tabuleiro(coloca_peca(tab,j,colocacao[0])):
                return colocacao
        elif obter_ganhador(tab) == cria_peca(' '):
            if esta_bloqueada(tab,j):
                posicoes = obter_posicoes_jogador(tab,j)
                return (posicoes[0], posicoes[0])
            else:
                for p in obter_posicoes_jogador(tab,j):
                    for i in range(3):
                        if obter_posicoes_adjacentes(p)[i] in \
                           obter_posicoes_livres(tab):
                            return (p,obter_posicoes_adjacentes(p)[i])                   
                    
    if modo == 'normal':
        if  ((len(obter_posicoes_jogador(tab,cria_peca('X')))) <= 3 and \
            (len(obter_posicoes_jogador(tab,cria_peca('O')))) < 3) or \
            ((len(obter_posicoes_jogador(tab,cria_peca('X')))) < 3 and \
            (len(obter_posicoes_jogador(tab,cria_peca('O')))) <= 3):
            colocacao = fase_colocacao(tab,j)
            if eh_tabuleiro(coloca_peca(tab,j,colocacao[0])) == True:
                return colocacao 
        elif obter_ganhador(tab) == cria_peca(' '):
            return minimax(tab,j,1,())[1]
                
            
            
    if modo == 'dificil':
        if  ((len(obter_posicoes_jogador(tab,cria_peca('X')))) <= 3 and \
            (len(obter_posicoes_jogador(tab,cria_peca('O')))) < 3) or \
            ((len(obter_posicoes_jogador(tab,cria_peca('X')))) < 3 and \
            (len(obter_posicoes_jogador(tab,cria_peca('O')))) <= 3):
            colocacao = fase_colocacao(tab,j)
            if eh_tabuleiro(coloca_peca(tab,j,colocacao[0])) == True:
                return colocacao             
        elif obter_ganhador(tab) == cria_peca(' '):
            posicoes = minimax(tab,j,5,())[1]
            return (posicoes[0],posicoes[1])
        
def moinho(jogador,modo):
    tab = cria_tabuleiro()
    jogador_do_turno = cria_peca('X')
     # Verificar se foi introduzido um jogador e um modo de jogo
    if jogador in (peca_para_str(cria_peca('X')),peca_para_str(cria_peca('O'))):
        if modo in ('facil','normal','dificil'):
            print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + modo + '.')
            print(tabuleiro_para_str(tab))
        else:
            raise ValueError('moinho: argumentos invalidos')
    else:
        raise ValueError('moinho: argumentos invalidos')
    # Enquanto nao houver ganhador o ciclo while onde ocorre as colocacoes e\
    # movimentacoes vai ser feito
    while (obter_ganhador(tab)) == cria_peca(' '):
        # Verificar se e o utilizador
        if peca_para_str(jogador_do_turno) == jogador:
            jogada = obter_movimento_manual(tab,jogador_do_turno)
        else:
            # Verificar se e o computador
            jogada = obter_movimento_auto(tab,jogador_do_turno,modo)
            print('Turno do computador' + ' (' + modo + ')' + ':')
        # Se tratar de uma colocacao
        if len(jogada) <= 1:
            tab = coloca_peca(tab,jogador_do_turno,jogada[0])
        # Senao e um movimento
        else:
            tab = move_peca(tab,jogada[0],jogada[1])
        print(tabuleiro_para_str(tab))
        # O jogador do turno atual e trocado pelo do adversario, neste caso\
        # o pc para que este tambem jogue
        jogador_do_turno = jogador_adversario(jogador_do_turno)           
            
    ganhador = obter_ganhador(tab)
    return peca_para_str(ganhador)
    
        
    
        
         
        
            
            
            
      
                   

    
        

    
         
          
    
                    
                
            
        
        
        
        
        
        
        
        
        
    
    
        
        
    
        
    

        
    
    

    

    
          
            
             
            
                       
           
    
    

    
    
    
             
        
             
    

            
    
                            
        


  
    
    
    
    
        
            
    
           

    
                   
                   
                 
                        
                
                        

        
            
       
 
                              
                                           
                            
                     
                    
      
 
           
                  

    
        

        
        
     
    
        
   
        



   
        
    
    
    
    
     
            

    
        
  
    
        
        
        
    
    

    



    
    
    

    
    


    
    
    

    

    








    
    
    
    