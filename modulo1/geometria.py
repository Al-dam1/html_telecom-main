pi = 3.1416


def area_circulo(radio):
    return pi * radio**2


def perimetro_circulo(radio):
    return 2 * pi * radio


if __name__ == "__main__":
    print("pruebas del modulo geometria: ")
    print(f"Area circulo r=3:{area_circulo(3)}")
    print(f"perimetro rectangulo 4x5:{perimetro_circulo}")
