
#import modelo 
import copy
import math
from PIL import Image, ImageDraw

def genericLstAction(State):
    pass

def genericExeAction(State, Action):
    pass

def genericCmpState(StateA, StateB):
    pass

#Estes callbacks tornam os algorimos de busca independentes dos modelos
funcLstAction = genericLstAction
funcExeAction = genericExeAction
funcCmpState  = genericCmpState


#--Representa um nó
class No:
    def __init__(self, noPai, nosFilho, E):
        self.noPai = noPai
        self.nosFilho = nosFilho
        self.estado = copy.deepcopy(E)


#--Tabela de estados
Nos = []

#--Guardar estado
def guardarNo(memoria, estado):
    memoria.append(estado)

#--Recuperar no
def recuperarNo(memoria, metodo):
    no = None
    if (metodo == "largura"):
        no = memoria.pop(0)
    elif (metodo == "profundidade"):
        no = memoria.pop()
    elif (metodo == "custo"):
        #Ordena os nós pelo menor custo
        memoria.sort(key = lambda No: No.estado[1])
        no = memoria.pop(0)

    return no

#--Verificar se há estado repetido
def estadoRepetido(listaDeNos, no):
    for no_ in listaDeNos:
        if (funcCmpState(no_.estado, no.estado)):
        #if (modelo.estadosIguais(no_.estado, no.estado)):
            return True
        
    return False

def strMemoria(memoria):
    txt = ""

    for no in memoria:
        txt = txt + str(no.estado)

    return txt

#--Busca uma solução para o problema
def busca(Einicial, Eobjetivo, metodo, maxiteracoes = 100):
    #Remove a soluçao anterior
    Nos.clear()

    #A principio, inicia somente com o estado inicial, ou seja, o nó raiz
    noInicial = No(None, [], Einicial)

    Nos.append(noInicial)

    #A memória guarda os estados para fins de algoritmo
    memoria = [noInicial]

    possuiSolucao = False
    iteracoes = 0
    
    #Teste inicial...
    if (funcCmpState(Einicial, Eobjetivo)):
    #if (modelo.estadosIguais(Einicial, Eobjetivo)):
        possuiSolucao = True
        #possuiSolucao = largura

    #Processa a memória até obter a solução
    while ((len(memoria) > 0 and possuiSolucao == False) and iteracoes < maxiteracoes):
        #txt = strMemoria(memoria) ##Remover depois

        #Recupera um nó da memória de acordo com o algoritmo
        no = recuperarNo(memoria, metodo)

        #txt = txt + "->" + str(no.estado) ##Remover depois
        #print(txt) ##Remover depois

        #A partir do nó, obter estado
        estado = no.estado        
        
        #Obtém todas as ações possíveis do estado atual
        acoes = funcLstAction(estado)
        #acoes = modelo.listarAcoes(estado)

        #Verifica se encontrou a solução utilizando o método de redução do custo         
        if (funcCmpState(estado, Eobjetivo)):
        #if (modelo.estadosIguais(estado, Eobjetivo)):
            possuiSolucao = True
            Nos.append(no)  
            break        
                
        for acao in acoes:
            #Obtém o novo estado aplicando a ação possível            
            novoEstado = copy.deepcopy(estado)
            
            novoEstado = funcExeAction(novoEstado, acao)
            #novoEstado = modelo.executarAcao(novoEstado, acao)

            #print(novoEstado)
            
            #Cria o novo nó atribuindo "no" como nó-pai e "novoEstado" como estado atual para esse nó
            novoNo = No(no, [], novoEstado)

            #Atribui "novoNo" como nó-filho 
            no.nosFilho.append(novoNo)

            #Se o estado for repetido, não coloque novamente na memória (Evita loops)
            #if (estadoRepetido(Nos, novoNo) == False):
            guardarNo(memoria, novoNo)
                
            #Registra o nó mesmo se for repetido    
            Nos.append(novoNo)

            
            iteracoes = iteracoes + 1

    return possuiSolucao

#Obter os passos que levam a solução
def solucao():
    solucao = []

    no = Nos[len(Nos) - 1]
    while (no != None):
        solucao.insert(0, no.estado)
        no = no.noPai
       
    return solucao
            
#Gera uma imagem para facilitar a visualização da solução
#def gerarImagemSolucao(solucao):
#    imagem = Image.new("RGB", (len(solucao) * 100, 100), color="white")
#    
#    x = 0
#    for estado in solucao:
#        modelo.desenharEstado(estado, imagem, (x + 5, 5), (90, 90))
#        x = x + 100
#
#    imagem.save("solucao.png")
