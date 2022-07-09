#Faça duas duas funções: uma codificar uma mensagem e outra para descodificar uma mensagem.
#Deve receber uma mensagem (string), essa mensagem só tem as letras padrões e espaço (não tem acento, símbolo, maiúscula e número). A ordem deste alfabeto começa com "a" e termina com espaço, ou seja espaço fica depois da letra "z".
#Além da mensagem, receba um número que é a senha para codificar ou descodificar a mensagem.
#Para codificar, cada letra deve ser movida pelo alfabeto o número de letras. Exemplo: letra "a" e senha 1 retorna "b";  letra "a" e senha 3 retorna "d"; letra "b" e senha 2 retorna "d".
#Exemplo de codificação: "abc", senha 1, retorna "bcd".
#Para descodificar o processo é inverso. A mensagem recebida já está codificada e a senha serve para reconstruir a mensagem original. Exemplo: "bcd", senha 1, retorna "abc".
#Se a operação de shift passa o final do alfabeto, deve retorna para o início do alfabeto. Exemplo: codificar "xyz", senha 5, retorna "bcd". descodificar "a" senha 5 retorna "w".
#Leia uma tupla (x, m, s):
#x: booleano (True, False) - True se é para codificar a mensagem m e False para descodificar a mensagem m.
#m: String - mensagem
#s: inteiro - senha usada para codificar ou descodificar.


codificar, codigo, senha = eval(input())

import string
alfabeto = list(string.ascii_lowercase) + [' ']

def codificar(codigo, senha):
    resultado = ""
    for indice in range(len(codigo)):
        for indice2 in range(len(alfabeto)):
            if codigo[indice] == alfabeto[indice2]:
                indice3 = indice2 + senha
                while indice3 > 26:
                    indice3 = indice3 - 27
                resultado += alfabeto[indice3]
    return resultado

def decodificar(codigo, senha):
    resultado = ""
    for indice in range(len(codigo)):
        for indice2 in range(len(alfabeto)):
            if codigo[indice] == alfabeto[indice2]:
                indice3 = indice2 - senha
                while indice3 < 0:
                    indice3 += 27
                resultado += alfabeto[indice3]
    return resultado

if codificar == True: print(codificar(codigo,senha))
else: print(decodificar(codigo,senha))
