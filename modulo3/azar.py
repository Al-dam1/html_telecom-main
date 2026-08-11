import random

def tirar_dado():
    return random.randint(1, 6)

def tirar_moneda():
    return random.choice(["cara", "cruz"])
