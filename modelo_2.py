
#from PIL import Image, ImageDraw
import busca

#--Estado inicial
E0 =  [ [1,'x',2] ,  [4,5,3] , [7,8,6]]

#--Estado final
Eobj = [ [1,2,3] ,  [4,5,6] , [7,8,'x']]


#-- Procura a posição atual
def posicaoAtual(Et):    
    lin, col = 0, 0    
    for lines  in Et:        
        for element in lines: 
            if (element == 'x'):
                return (lin, col)
            else:
                col = col + 1
        lin = lin + 1      
        col = 0
#------------------------------------------------


#--Lista todos as possiveis ações para determinado estado
def listarAcoes(Et):

    acoesPossiveis = []

    posicao = posicaoAtual(Et)
    
    lin, col = posicao
   
    if (lin > 0):
        acoesPossiveis.append("up")

    if (lin < 2):
        acoesPossiveis.append("down")

    if (col > 0): 
        acoesPossiveis.append("left")

    if (col < 2): 
        acoesPossiveis.append("right")

    return acoesPossiveis
#------------------------------------------------



#--Troca duas posições
def trocaPosicao(Et, p0, p1):
    l0, c0 = p0
    l1, c1 = p1

    # swap
    Et[l0][c0], Et[l1][c1] = Et[l1][c1], Et[l0][c0]
#------------------------------------------------



#--Executar ações
def executarAcao( Et, acao):
    posAt = posicaoAtual(Et)
    lin, col = posAt

    if (acao == "up"):
        trocaPosicao(Et, posAt, (lin - 1, col))

    if (acao == "down"):
        trocaPosicao(Et, posAt, (lin + 1, col))

    if (acao == "left"):
        trocaPosicao(Et, posAt, (lin, col - 1))

    if (acao == "right"):
        trocaPosicao(Et, posAt, (lin, col + 1))

    return Et
   
#------------------------------------------------

#--Compara igualdade de estados
# **** É possivel associar um inteiro a cada estado e
# **** assim a comparação seria direta
def estadosIguais(Ea, Eb):
    for lin in range(len(Ea)):
        for col in range(len(Ea[0])):
            if (Ea[lin][col] != Eb[lin][col]):
                return False
    
    return True
#------------------------------------------------

# Desenha o estado
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

           
#Necessário para utilizar os algorimos de busca
busca.funcLstAction = listarAcoes
busca.funcExeAction = executarAcao
busca.funcCmpState  = estadosIguais

busca.busca(E0, Eobj, "largura")
print(busca.solucao())