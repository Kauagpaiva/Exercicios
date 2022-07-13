
#olhei um bocado de coisa desse codigo aqui, o problema que eu achei é que na
#hora de retornar a soma ou subtração, eu sempre retorno um valor x*10**expoente
#só que ai o próprio python arredonda o resultado, oq é justamente oq tenho q evitar


#Input1: 0.1-1000000000000000.999999999999999999
#Output_esperado1: -1000000000000000,899999999999999999
#Meu_outpup: -1000000000000000,9

#Input: 0.1-1000000000000000.999999999999999999
#output esperado: -1000000000000000,899999999999999999
#Meu output:-1000000000000000,9


#input3: -99999990000000000000000000000+0.0000000000000000099999999978
#output esperado: -99999989999999999999999999999,9999999999999999900000000022
#nesse o meu código dá erro :(





#a ideia que o professor nos deu nesse laboratório foi de ler um valor como
#o computador lê, tipo, se o valor de entrada for 0,123 era para a gente 
# salvar o velor como 123*10**-3
#ele também sugeriu que a gente fizesse as manipulações com string

class NumeroDecimal:
    
    #nessa parte aqui foi para salvar o valor da forma que o professor sugeriu
    def __init__(self, n):
        n = str(n)
        #separei o valor antes e depois da virgula
        self.lista = n.split('.')
        if len(self.lista)>1:
            #esse self.e é como eu salvei o expoente que eu vou usar na base 10
            #dai ele é a quantidade de digitos que tinham depois da virgula
            #ex: se o valor foi 0,123, o self.e tem que ser -3, já que eu quero
            #salvar como 123*10**-3
            self.e = len(self.lista[1]) * -1
            #esse self.n é a representação do valor sem a virgula
            #ex: se o input for 12,35, eu quero salvar ele como
            # 1235*10**-2
            self.n = int((self.lista[0] + self.lista[1]))
        if len(self.lista)==1: 
            self.e = 0
            self.n = int(self.lista[0])
        
    def __add__(self, other):
        #para fazer a soma/subtração, nós tinhamos que igualar o expoente dos depois
        #valores, ex: 1235*10**-2 + 123*10**-3 = 12350*10**-3 + 123*10**-3
        
        #ai quando os expoentes fossem iguais, era só somar os dois números
        if self.e > other.e:
            d = self.e - other.e
            a = self.n*10**d + other.n
            c = str(a)[:-other.e-2]+","+str(a)[-other.e-2:]
            return c
            
        if other.e > self.e:
            d = other.e - self.e
            a = other.n*10**d + self.n
            c = str(a)[:-self.e-2]+","+str(a)[-self.e-2:]
            return c
            
        if self.e == other.e:
            a = self.n + other.n
            return str(a)[:-self.e-2]+","+str(a)[-self.e-2:]
            
    def  __sub__(self, other):
        if self.e > other.e:
            d = self.e - other.e
            a = self.n*10**d - other.n
            c = str(a)[:-other.e-2]+","+str(a)[-other.e-2:]
            #essa c ai de cima ja é uma mudança q eu tinha feito quando
            #vi q nn tava saindo o resultado que eu queria, 
            # mas o return original é esse dai de baixo, a msm coisa pra soma
            #return ((self.n*10**d) - other.n) * 10 ** other.e
            return c
            
        if other.e > self.e:
            d = other.e - self.e
            a = other.n*10**d - self.n
            c = str(a)[:-self.e-2]+","+str(a)[-self.e-2:]
            return c
            
        if self.e == other.e:
            a = self.n - other.n
            return str(a)[:-self.e-2]+","+str(a)[-self.e-2:]
            
            
    def __repr__(self):
        return self.n*10**self.e
        
        
#aqui é só pra ler o input mesmo
num = input() # num = operação, ex: 1.1+0.3
for i in range(1, len(num)):
    if num[i] == '+' or num[i] == '-' or num[i] == '/' or num[i] == '*':
        X = num[:i]
        Y = num[i+1:]
        Z = num[i]
        r = 'NumeroDecimal('+str(X)+')'
        s = 'NumeroDecimal('+str(Y)+')'
        z = r+num[i]+s
        break
    else: 
        z = 'NumeroDecimal('+num+')'


print(eval(z))
