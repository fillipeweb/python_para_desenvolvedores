# -*- encoding: utf-8 -*-
# 4. Implementar um módulo com duas funções:
# ▪ split(fn, n), que quebra o arquivo fn em partes de n bytes e salva com nomes
# seqüenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
# ▪ join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.
import os

def split(fn, n):
    temp = file(fn)
    size = os.stat(fn).st_size
    qtd_files = size / n    
    for i in range(0,qtd_files):
        file_ = file('file%04d.txt' % (i,), 'w')
        file_.write(temp.read(n))

    if temp.read(1):
        file_ = file('file%04d.txt' % (i + 1,), 'w')
        file_.write(temp.read(n))

def join(fn, *fnList):
    file_out = file(fn, 'w')
    for file_ in fnList:
        file_out.write(file(file_).read())
        

if __name__ == '__main__':
    split('file.e1',500)
    join('fileall.txt','file0000.txt','file0001.txt','file0002.txt','file0003.txt')