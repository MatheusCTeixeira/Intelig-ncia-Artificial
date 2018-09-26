from appJar import gui 
import math
import copy 
import modelo
import busca
import sys
import re


app = gui("Example",handleArgs=False)

map = [[(1, "map/1.gif"), (2, "map/2.gif"),(3, "map/3.gif")],[(4, "map/4.gif"),(5, "map/5.gif"), (6, "map/6.gif")],[(7, "map/7.gif"), (8, "map/8.gif"), (9, "map/9.gif")]]
mapInit = copy.deepcopy(map)

#Encontrar em qual bloco esta a lacuna do tabuleiro
def encontrarLacuna():
    lin, col = 0, 0

    for l in map:
        for ele in l:
            val, img = ele
            if (val == 9):
                return (lin, col)
            col = col + 1
        lin = lin + 1
        col = 0

    return (lin, col)

#Encontra as coordenadas de uma peça baseada no seu nome/código. Ex nome = 9 ==> (1, 1), centro do tabuleiro 
def encontrarPosicaoPorNome(nome):
    val = int(nome) - 1
    col = val % 3
    lin = math.floor(val / 3)
    return (lin, col)

#Troca duas peças de posição
def inverterElementosDoMapa(coord0, coord1):
    lin0, col0 = coord0
    lin1, col1 = coord1
    map[lin0][col0], map[lin1][col1] = map[lin1][col1], map[lin0][col0]    

#Troca a imagem que esta na peça
def changeImage(imgname):
    lin0, col0 = encontrarPosicaoPorNome(imgname)
    lin1, col1 = encontrarLacuna()
    
    hor = abs(lin0-lin1) == 1 and (abs(col0-col1) == 0)
    ver = abs(lin0-lin1) == 0 and (abs(col0-col1) == 1)

    #print(str(hor) +" " + str(ver))
    
    #Verifica se as pessas realmente podem ser movidas
    #é necessario possuir a distacia == 1 e ser ou vertical ou horizontal (mutualmente exclusivo)
    if ((hor and not ver) or (ver and not hor)):
        inverterElementosDoMapa((lin0, col0), (lin1, col1))
                        

        val0 = lin0 * 3 + col0 + 1
        val1 = lin1 * 3 + col1 + 1
        #print(str(val0) + " " + str(val1))
        app.setImage(str(val0), map[lin0][col0][1])
        app.setImage(str(val1), map[lin1][col1][1])


#Cria a GUI
def criarJanela():
    app.startLabelFrame("Game")
    app.setSticky("news")
    app.setExpand("both")

    #Carrega as imagens do tabuleiro
    def carregarImagens(imagens = map):        
        l, c = 0, 0
        for lin in imagens:
            for ele in lin:
                val, img = ele
                app.addImage(str(val),img, l, c)
                app.setImageSubmitFunction(str(val), changeImage)
                c = c + 1
            l = l + 1 
            c = 0

    carregarImagens()

    app.stopLabelFrame()

    #Lógica de execução do botão.
    #Desde a obtenção do modelo até a geração do resultado
    #O método de busca é determinado pelo botão selecionado
    def processa(metodo):
        E0 = []
        for line in map:
            L = []
            for element in line:
                v = element[0]
                if (v == 9):
                    v = 'x'
                L.append(v)
            E0.append(L)
        modelo.E0 = E0
        
        resultado = busca.busca(modelo.E0, modelo.Eobj, metodo)
        if resultado != None:
            solucao = busca.solucao(busca.Nos)
            print("Solucao encontrada [largura = " + str(resultado) + ", profundidade = " + str(len(solucao)) + "]" )
            #print(solucao)
            busca.gerarImagemSolucao(solucao)
    

    app.startLabelFrame("Controle")
    app.addButtons(["largura", "profundidade"], processa)
    
    
    app.stopLabelFrame()
    app.go()


if sys.argv.count("GUI") > 0:
    criarJanela()
elif sys.argv.count("largura") > 0:
    metodo = "largura"
elif sys.argv.count("profundidade") > 0:
    metodo = "profundidade"

resultado = busca.busca(modelo.E0, modelo.Eobj, metodo)
if resultado != None:
    solucao = busca.solucao(busca.Nos)
    print("Solucao encontrada [largura = " + str(resultado) + ", profundidade = " + str(len(solucao)) + "]" )
    print("\n\nSolucao:\n")
    print(solucao)
    print("\n---------------------------------------------\n")
    busca.gerarImagemSolucao(solucao)

       

    