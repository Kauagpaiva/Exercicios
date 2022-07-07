#Faça um algoritmo em Python que receba um vetor V com n inteiros e um inteiro m>0 e m≤n, retorne um vetor com m valores: os m menores valores de V. Não é permitido ordenar o vetor ou usar qualquer tipo de função similar. Deve fazer só usando comparação entre os elementos, sem mudar o vetor ou usar um outro vetor auxiliar. 
#Input: Uma tupla onde o primeiro elemento é o vetor V de inteiros e o segundo elemento é m.
#Output: Um vetor como menor valor de V até o m-íssimo menor elemento de V.

#Exemplos:
#Input1: ([4,1,2,3],1)
#Output1: [1]
#Input2: ([-1,-3,0,0,10,-1,6,5,6],4)
#Output2: [-3,-1,-1,0]

vetor, n = [x for x in eval(input())]

def menor(vetor, n):
    resultado= []
    while len(resultado) < n:
        for indice in range(len(vetor)):
            if vetor[indice] not in resultado:
                menor = vetor[indice]
        #encontro um elemento do vetor que ainda não esteja na lista de resultados

        for elemento in vetor:
            if elemento not in resultado:
                if elemento < menor:
                    menor = elemento
        #encontro o menor elemento do vetor que ainda não esteja no resultado

        if menor not in resultado:            
            for elemento in vetor:
                if elemento == menor: 
                    if len(resultado)<n: resultado.append(menor)
        #adiciono esse elemento no resultado (se o vetor possuir mais de um elemento com o mesmo valor, eles serão adicionados ao resultado até que atinja o limite)

    return resultado
    
print(menor(vetor, n))
