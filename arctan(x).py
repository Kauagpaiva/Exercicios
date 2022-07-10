#A série descoberta por Leibniz para computar o arco tangente é 
#arctanx = x − (x^3)/3 + (x^5)/5 − (x^7)/7 + (x^9)/9−...
#Se usarmos x=1, podemos computar uma aproximação para π/4.
#Faça uma função que receba x e n, onde n é o numero de termos da serie e retorna o valor da serie.
#Input: são dois inputs. O primeiro recebe um float e o segundo recebe um inteiro positivo
#Output: saída da função


x, n = float(input()), int(input())

def Arctan(x, n):
    lista = [x for x in range(n) if x%2 != 0]
    lista_positiva = lista[::2]
    lista_negativa = lista[1:][::2]
    resultado1, resultado2 = 0, 0
    
    for elemento in lista_positiva:
        resultado1 += (x**elemento)/elemento
    for elemento in lista_negativa:
        resultado2 += -((x**elemento)/elemento)
        
    return resultado1 + resultado2
    
print(Arctan(x, n))
