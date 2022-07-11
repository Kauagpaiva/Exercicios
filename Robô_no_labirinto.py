#Deseja-se um algoritmo para ajudar um robô a navegar um labirinto composto de salas que podem estar vazias ou cheias. O labirinto é codificado por uma matriz contendo apenas os valores 0, 1 conforme a sala correspondente esteja aberta ou fechada. O robô deve começar na sala correspondente ao canto superior esquerdo da matriz e sair pela sala correspondente ao canto inferior direito da matriz. Mais ainda: o robô só pode andar uma casa por vez em uma de duas direções: para a direita ou para baixo, ocupando apenas salas vazias. Escreva a função caminho_diagonal(m) que recebe uma matriz m contendo o labirinto e retorna uma lista com tuplas da forma (i,j), onde i e j são os índices de linha e coluna da matriz ocupadas sucessivamente pelo robô desde a entrada até a saída. Caso não haja nenhum caminho até a saída, a função deve retornar False.


# começo: 20h15
# termino: 21h15

matriz = eval(input())

def avalia_direita(m, linha, coluna):
    if m[linha][coluna+1] == 1: return False
    return True
    
def avalia_baixo(m,linha,coluna):
    if m[linha+1][coluna] == 1: return False
    return True

def caminho_diagonal(m, linha, coluna, resultado, erro):
    if m[0][0] == 1: return False
    
    if [linha, coluna] == [len(m)-1, len(m[0])-1]: return resultado
    
    if coluna+1 < len(m):
        if avalia_direita(m, linha, coluna):
            resultado += [(linha, coluna+1)]
            return caminho_diagonal(m, linha, coluna+1, resultado, erro)
        erro += [[linha, coluna+1]]
        
        
    if linha+1 < len(m[0]):
        if [linha+1, coluna] not in erro:
            if avalia_baixo(m,linha,coluna):
                resultado += [(linha+1, coluna)]
                return caminho_diagonal(m, linha+1, coluna, resultado, erro)
            erro += [[linha+1, coluna]]
    
    m[linha][coluna] = 1
    erro += [[linha, coluna]]
    
    return caminho_diagonal(m,0,0, [[0,0]], erro)
    
print(caminho_diagonal(matriz, 0, 0, [[0,0]], []))


