#Paula Natalia Paez Vega
#Escuela Colombiana de ingeniería Julio Garavito
import math

def suma(a,b):
    #Esta función, suma vectores
    return (a[0]+b[0],a[1]+b[1])
def multiplicacion(a,b):
    # Esta función, multiplica vectores
    d = round(a[0]*b[0]-a[1]*b[1])
    c = round(a[1]*b[0]+b[1]*a[0])
    return d, c
def resta(a,b):
    # Esta función, resta vectores
    return (a[0] - b[0], a[1] - b[1]) ##(1,2)(1,2)
def division(a,b):
    # Esta función, divide vectores
    c = (((a[0]*a[1]) + (b[0]*b[1])) / (((a[1])**2) + ((b[1])**2)))
    d = (((a[1]*b[0]) - (a[0]*b[1])) / (((a[1])**2) + ((b[1])**2)))
    return round(c), round(d)
def modulo(a):
    # Esta función, saca el modulo del vector sumando ambos elementos y elevandolos al cuadrado, esto dentro del radical
    return round(+((((a[0])**2)+((a[1])**2))**(1/2)),2)
def conjugado(a):
    # Esta función, cambia de signo el segundo elemento
    return a[0],(-a[1])
def fase(a):
    # Esta función, saca la fase del vector
    c = math.atan(a[1]/a[0])
    p = c * (180 / math.pi)
    return round(p)
def cartesiano_polar(a):
    #Esta funcion cambia de cartesiano a polar
    c = round((a[0]*math.cos(a[1])))
    d = round((a[0]*math.sin(a[1])))
    return c,d
def polar_cartesiano(d):
    # Esta funcion cambia de polar a cartesiano
    f = round(d[0]*math.cos(d[1])), round(d[0]*math.sin(d[1]))
    return f
def main():
    print(suma((3.5,7),(4.2,9)))
    print(multiplicacion((3.5,7),(4.2,9)))
    print(division((-2,1),(1,2)))
    print(resta((3.5,7),(4.2,9)))
    print(modulo((1,-1)))
    print(conjugado((6,5)))
    print(fase((1,1)))
    print(cartesiano_polar((1.41,45)))
    print(polar_cartesiano((2,math.pi)))
main()