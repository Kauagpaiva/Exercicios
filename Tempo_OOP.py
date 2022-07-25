#Implemente uma classe chamada Tempo que representa um instante ou um intervalo de tempo.
#O construtor da classe deve suportar argumentos para especificar hora, minuto e segundo.
#Instância de Tempo devem poder ser somadas ou subtraídas, isto é, a classe deve implementar os métodos __add__ e __sub__.
#Sua classe também deve suportar um método __repr__ que retorna uma string indicando o tempo em horas, minutos e segundos.
#Veja um exemplo de utilização abaixo (caso de uso).

#print(Tempo(2,0,51)+Tempo(0,1,10))
#print(Tempo(2,0,1)-Tempo(2,1,0))

#Imprime:
#2h, 2m, 1s
#-0h, 0m, 59s


#inicio: 19h03
#termino: 19h45

class Tempo:
    
    def __init__(self, horas, minutos, segundos):
        self.horas = int(horas)
        self.minutos = int(minutos)
        self.segundos = int(segundos)
        
    def __add__(self,other):
        horas = 0
        minutos = 0 
        segundos = self.segundos + other.segundos
        while segundos > 60:
            segundos = segundos - 60
            minutos += 1
        minutos += self.minutos + other.minutos
        while minutos > 60:
            minutos = minutos - 60
            horas += 1
        horas += self.horas + other.horas
        return str(horas)+"h, "+ str(minutos)+"m, " + str(segundos)+"s"
        
    def __sub__(self,other):
        teste1 = self.segundos + self.minutos*60 + self.horas*60*60
        teste2 = other.segundos + other.minutos*60 + other.horas*60*60
        if other.segundos < self.segundos:
            other.minutos = other.minutos - 1
            other.segundos += 60
        segundos = other.segundos - self.segundos
        
        if other.minutos < self.minutos:
            other.horas = other.horas - 1
            other.minutos += 60
        minutos = other.minutos - self.minutos
        
        horas = other.horas - self.horas
        if teste1 < teste2:
            return "-"+str(horas)+"h, "+ str(minutos)+"m, " + str(segundos)+"s"
        else: return str(horas)+"h, "+ str(minutos)+"m, " + str(segundos)+"s"
        
    def __repr(self):
        return str(self.horas)+"h, "+ str(self.minutos)+"m, " + str(self.segundos)+"s"
        
        
x = input()
for indice in range(len(x)):
    if x[indice] == "+" or x[indice] == "-":
        a = "Tempo"+x[:indice]
        b = "Tempo"+x[indice+1:]
        r = eval(a+x[indice]+b)
        
print(r)
