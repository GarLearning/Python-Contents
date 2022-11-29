# as -> é usado para dar um peseudônimo para um modulo que esta sendo importado exemplo:
#import random as rand
# agora em vez de usar ramdom como nome base usaria o rand
#print(rand.randint(1, 9))

#funcionalidades de modulos
from random import randint as randitt
print(randitt(1, 9))

#em abos os casos abaixo n daria ceerto pelo que testei
"""from modularização.func_115 import * as func
from modularização.func_115 as func import *"""