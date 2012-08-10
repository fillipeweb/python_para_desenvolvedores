# -*- encoding: utf-8 -*-
# 3. Implementar um gerador que produza tuplas com as cores do padrão RGB (R, G e B
# variam de 0 a 255) usando xrange() e uma função que produza uma lista com as tuplas
# RGB usando range(). Compare a performance.

def gen_rgb():
    for i in xrange(0, 255):
        for j in xrange(0, 255):
            for k in xrange(0, 255):
                yield (i, j, k)
                
def func_rgb():
    for i in range(0, 255):
        for j in range(0, 255):
            for k in range(0, 255):
                print (i, j, k)
                

if __name__ == "__main__":
    # func_rgb()
    for i in gen_rgb():
        print i 