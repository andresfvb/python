import string
import random

def generate():
    random.seed()
    GLOBAL_NAME_CACHE = set()
    LETRAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    DIGITOS = '1234567890'
    return ''.join((random.choice(LETRAS),
                random.choice(LETRAS),
                random.choice(DIGITOS),
                random.choice(DIGITOS),
                random.choice(DIGITOS)))
            
class Robot:
    

    def __init__(self):
        self.reset()
        
    def reset(self):
        self.name = generate()
   