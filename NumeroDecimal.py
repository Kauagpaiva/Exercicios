#Objetivo: Implementar uma classe de número em ponto flutuante usando número inteiro, desta forma essa classe terá precisão "infinita".

class NumeroDecimal:
    
    def __init__(self, n):
        #Quero guardar um número como n*10**e. Ex: 1,25 = 125*10**-2
        self.lista = n.split('.')
        if len(self.lista)>1: #verifico se o len for maior que 1, significa que é um número com virgula, se for igual a 1 é um inteiro
            self.e = -len(self.lista[1]) #conto os números depois da virgula e salvo como expoente, x*10**self.e
            if self.lista[0][0] == "-": #verifico se o número é negativo, para deixar o resultado negativo também
                self.n = -int((self.lista[0] + self.lista[1]))
            else: 
                self.n = int((self.lista[0] + self.lista[1]))
        if len(self.lista)==1: 
            self.e = 0
            if self.lista[0][0] == "-":
                self.n = -int(self.lista[0])
            else:
                self.n = int(self.lista[0])

    def __add__(self, other):
        #Para fazer a soma, preciso igualar o expoente dos dois valores, ex: 123*10**1 + 321*10**-2 = 123000*10**-2 + 321*10**-2
        #depois que os expoentes forem iguais, basta somar os dois números e multiplicar por 10**expoente_utilizado
        if self.e > other.e:
            diferença = self.e - other.e #calculo a diferença dos expoentes
            soma = self.n*10**diferença + other.n #faço a soma dos valores
            if str(soma)[0] == "-":
                resultado = str(soma)[:-other.e-1]+","+str(soma)[-other.e-1:]
            else: 
                resultado = str(soma)[:-other.e-2]+","+str(soma)[-other.e-2:]
            return resultado
            
        if other.e > self.e:
            diferença = other.e - self.e
            soma = other.n*10**diferença + self.n
            if str(soma)[0] == "-":
                resultado = str(soma)[:-self.e-1]+","+str(soma)[-self.e-1:]
            else:
                resultado = str(soma)[:-self.e-2]+","+str(soma)[-self.e-2:]
            return resultado
            
        if self.e == other.e:
            soma = self.n + other.n
            return str(soma)[:-self.e]+","+str(soma)[-self.e:]
            
    def  __sub__(self, other):
        #Para fazer a subtração, preciso igualar o expoente dos dois valores, ex: 9999*10**4 - 55*10**-2 = 9999000000*10**-2 + 55*10**-2
        #depois que os expoentes forem iguais, basta subtrair os dois valores e multiplicar por 10**expoente_utilizado
        if self.e > other.e:
            diferença = self.e - other.e
            sub = self.n*10**diferença - other.n
            if str(sub)[0] == "-":
                resultado = str(sub)[:-other.e-1]+","+str(sub)[-other.e-1:]
            else: 
                resultado = str(sub)[:-other.e-2]+","+str(sub)[-other.e-2:]
            return resultado
            
        if other.e > self.e:
            diferença = other.e - self.e
            sub = other.n*10**diferença - self.n
            if str(sub)[0] == "-":
                resultado = str(sub)[:-self.e-1]+","+str(sub)[-self.e-1:]
            else: resultado = str(sub)[:-self.e-2]+","+str(sub)[-self.e-2:]
            return resultado
            
        if self.e == other.e:
            sub = self.n - other.n
            return str(sub)[:-self.e]+","+str(sub)[-self.e:]
            
            
    def __repr__(self):
        return self.n*10**self.e
        
numero = input() # num = operação, ex: 1.1+0.3
for i in range(1, len(numero)):
    if numero[i] == "+" :
        print(NumeroDecimal(numero[:i]) + NumeroDecimal(numero[i+1:]))
    if numero[i] == "-":
        print(NumeroDecimal(numero[:i]) - NumeroDecimal(numero[i+1:]))
