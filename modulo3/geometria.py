# geometria.py

""" PI = 3.1416

def area_circulo(radio):
    return PI * radio**2

def perimetro_circulo(radio):
    return 2 * PI * radio

if __name__ == "__main__":
    print("Pruebas del módulo geometría:")
    print(f"Área círculo r=3: {area_circulo(3)}")
    print(f"Perímetro círculo r=3: {perimetro_circulo(3)}") """

def area_circulo(base,altura):
    return base * altura
def perimetro_cuadrado(lado):
    return lado * 4
def area_trinagulo(base,altura):
    return (base * altura) / 2
def area_rectangulo(a,b):
    return a *b

print(area_circulo(4,12))
print(perimetro_cuadrado(6))
print(int(area_trinagulo(6,12)))