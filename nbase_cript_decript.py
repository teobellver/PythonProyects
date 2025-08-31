import random, time
import unicodedata

utf_8_chars = "".join([chr(i) for i in range(0, 0x10FFFF) if unicodedata.category(chr(i)).startswith('L') or unicodedata.category(chr(i)).startswith('N')])

funcion = input("Que funcion queres usar? (Para convertir escribi C) (Para de-convertir escribi D):")
base = int(input("Inserta la base del sistema de enumeracion al que quieras convertir:"))
valor= input("Inserta el valor que quieras convertir:")
num=[]
result=[]
binary=[]
chars_availables=[]
for char in valor:
    num.insert(0, int(char))
        ## print(num) ##array building
num.append(int("2"))
totalchars=len(num)-1
resultado=0
    
def de_convertir(base, totalchars, num, resultado):

    contador=0
    for i in range(totalchars):
        resultado+=(num[i]*pow(base,i))
        print(num[i], "X", base, "**", i ,"==>",resultado) ###procedimientos
        
        
    print(resultado)
def enable_custom_chars(base, chars, chars_availables):
    chars_len=len(chars)
    for i in range(chars_len):
        if i < base:
            chars_availables.append(chars[i])
    print(chars_availables)
    print("length de new_chars: "+ str(len(chars_availables)))

def convertir(base, valor, totalchars, result, binary, chars_availables):
    enable_custom_chars(base, utf_8_chars, chars_availables)
    while valor>0.001:
        time.sleep(0.1)
 #       print("Valor inicial= " + str(valor))
        
        valorI=valor/base ## 192 -> 64 -> 21.3
        valorF=int(valorI)
#        print("Valor float= "+ str(valorI)+" Valor int="+ str(valorF) )
        if valorF == valorI: ## si no es integer // si no tiene resto
            result.append(0)
        resto=int(((valorI-valorF)+0.1)*base)
#        print("resto= "+str(resto))
        if valorF != valorI: ## si si es integer // si tiene resto
            result.append(chars_availables[resto])
        valor=int(valorI)
        print(result)
        print("Next Step")
    print(result)
    result_len=len(result)
    binary = result[::-1]
    for element in binary:
        print(element, end="")
    return binary

if funcion=="D" or "d":
    de_convertir(base, totalchars, num, resultado)    
if funcion=="C" or "c":
    convertir(base, int(valor), totalchars, result, binary, chars_availables)