
import modelo 
import copy
from PIL import Image, ImageDraw

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

    return no

#--Verificar se há estado repetido
def estadoRepetido(listaDeNos, no):
    for no_ in listaDeNos:
        if (modelo.estadosIguais(no_.estado, no.estado)):
            return True
        
    return False

#--Busca uma solução para o problema
def busca(Einicial, Eobjetivo, metodo):

    #Remove a soluçao anterior
    Nos.clear()

    #A principio, inicia somente com o estado inicial, ou seja, o nó raiz
    noInicial = No(None, [], modelo.E0)

    Nos.append(noInicial)

    #A memória guarda os estados para fins de algoritmo
    memoria = [noInicial]


    possuiSolucao = False
    iteracoes = 0
    profundidade = 1
    largura = 1

    #Processa a memória até obter a solução
    while ((len(memoria) > 0 and possuiSolucao == False) and iteracoes < 10000):
        #Recupera um nó da memória de acordo com o algoritmo
        no = recuperarNo(memoria, metodo)
        #A partir do nó, obter estado
        estado = no.estado
        
        #Obtém todas as ações possíveis do estado atual
        acoes = modelo.listarAcoes(estado)

        #Atualiza os parametros da solução
        if len(acoes) > 0:
            profundidade = profundidade + 1
            largura = max(largura, len(acoes))

        for acao in acoes:
            #Obtém o novo estado aplicando a ação possível            
            novoEstado = copy.deepcopy(estado)
            modelo.executarAcao(novoEstado, acao)

            #Cria o novo nó atribuindo "no" como nó-pai e "novoEstado" como estado atual para esse nó
            novoNo = No(no, [], novoEstado)
            #Atribui "novoNo" como nó-filho 
            no.nosFilho.append(novoNo)

            #Se o estado for repetido, não coloque novamente na memória (Evita loops)
            if (estadoRepetido(Nos, novoNo) == False):
                guardarNo(memoria, novoNo)
                
            #Registra o nó mesmo se for repetido    
            Nos.append(novoNo)

            if (modelo.estadosIguais(novoEstado, Eobjetivo)):
                possuiSolucao = True
                break

            iteracoes = iteracoes + 1

    return possuiSolucao

def solucao(tabelaDeNos):
    solucao = []

    no = tabelaDeNos[len(tabelaDeNos) - 1]
    while (no != None):
        solucao.insert(0, no.estado)
        no = no.noPai
       
    return solucao

#def desenharEstado(E, imagem, xy, wh):
#    dr = ImageDraw.Draw(imagem)
#
#    # Parâmetros para o desenho
#    x,y = xy
#    w, h = wh
#    dx, dy = w/3, h/3
#
#    # Desenha elemento a elemento do estado E
#    for lin in E:
#        for value in lin:
#            dr.text((x + dx/2, y + dy/2), str(value), fill=(0, 0, 255))
#            dr.rectangle((x, y, x + dx, y + dy), outline=(0, 0, 0))
#            x = x + dx
#
#        x = xy[0]
#        y = y + dy
            

def gerarImagemSolucao(solucao):
    imagem = Image.new("RGB", (len(solucao) * 100, 100), color="white")
    
    x = 0
    for estado in solucao:
        modelo.desenharEstado(estado, imagem, (x + 5, 5), (90, 90))
        x = x + 100

    imagem.save("solucao.png")

#resultado = busca(modelo.E0, modelo.Eobj, "largura")

#print(resultado)

#gerarImagemSolucao(solucao(Nos))

#if (resultado):
#    for no in Nos:
#        print(no.estado)