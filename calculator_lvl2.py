import sys
default=True
mode=sys.argv[1]
if mode=="-h" or "-help" or "--help" or "--h":
    print("order of arguments: $ python filename mode num1 num2")
if mode == "-i":
    default=False
class main():
    if default!=False:
        if mode=="+" or "-" or "/" or "*" or "**" or "%":
            x=sys.argv[2]
            y=sys.argv[3]
    else:
        mode=input("Introduce el modo en simbolo: + es suma; - es resta; * es multiplicacion; / es division; '%' sin las comillas es porcentaje; ** es potencia:")
        if mode=="+" or "-" or "/" or "*":
            if mode!="**":
                x=input("Introduce el primer numero")
                y=input("Introduce el segundo numero:")
        if mode=="%":
            x=input("Introduce la cantidad total:")
            y=input("Introduce la cantidad especifica:")
        if mode=="**":
            x=input("Introduce numero:")
            y=input("Introduce el indice de potencia:")
p=main()
def sum(x,y):
    result=x+y
    return result
def sub(x,y):
    result=x-y
    return result
def mul(x,y):
    result=x*y
    return result
def divide(x,y):
    result=x/y
    return result
def perc(x,y):
    total= (y*100/x) ##regla de 3 simples
    return f"{total}%"
def pot(x,y):
    x1=x
    for i in range(y):
        result=x*x1
        x=result
    return result
match mode:
    case "+":
        print(sum(float(p.x),float(p.y)))
    case "-":
        print(sub(float(p.x),float(p.y)))
    case "*":
        print(mul(float(p.x),float(p.y)))
    case "/":
        print(divide(float(p.x),float(p.y)))
    case "%":
        print(perc(float(p.x),float(p.y)))
    case "**":
        print(pot(float(p.x),float(p.y)))