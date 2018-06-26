#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy
import math
import hardlims
import pattern



#Transpoz aldirma metodu
def transpose(matris):
    return numpy.matrix.transpose(matris)

#Vektoru ortonormal yapma
def make_ortonormal(P):
    carpim=numpy.dot(P,transpose(P))
    karekok=math.sqrt(carpim)
    bolum=numpy.divide(P,karekok)
    return bolum


#SIFIR SAYISI
P0=numpy.array([[-1,  1,  1,  1,  1, -1,
                  1, -1, -1, -1, -1,  1,
                  1, -1, -1, -1, -1,  1,
                  1, -1, -1, -1, -1,  1,
                  1,  1,  1,  1,  1, -1]])
#BIR SAYISI
P1=numpy.array([[-1,  -1, -1, -1, -1, -1,
                  1,  -1, -1, -1, -1, -1,
                  1,   1,  1,  1,  1,  1,
                 -1,  -1, -1, -1, -1, -1,
                 -1,  -1, -1, -1, -1, -1]])


T=P0            #Beklenen cikti

alpha=1
Wnew=[]
Wold=[]
a=[]

#Girilen patternin agirligini bulan metod
def W_Hesapla(P):
    global a
    W = numpy.dot(transpose(P),T)
    a = hardlims.hardlims(numpy.dot(W, transpose(P)))  # test edilen desen
    if numpy.array_equal(transpose(a), T):
        return W
    # else:
    #     print ("İstenilen girdinin agirliği icin girdi ve cikti esit olmali")

def test(W,P):
    global Wnew
    global Wold
    global a

    a=hardlims.hardlims(numpy.dot(W,transpose(P)))
    if (numpy.array_equal(transpose(a),T)):
        print "\nGirilen deger istenilen cikti ile esit\n"
        print("a=\n"),a
    else:
        Wold=W
        while(1):
            Wnew = Wold + (alpha * (numpy.dot(T,transpose(P))))
            Wold = Wnew
            a = hardlims.hardlims(numpy.dot(Wnew,transpose(P)))
            if(numpy.array_equal(transpose(a),T)):
                break
            print "a: \n",a





sonuc=numpy.dot(transpose(P0),P0)

if numpy.array_equal(sonuc,numpy.identity(30)):
    print("Birim matrise esit")
    W=sonuc
    test(W,P0)
else:
    agirlik=W_Hesapla(make_ortonormal(P0)) #ortonormal yapilacak vektoru yaz
    test(agirlik,pattern.P0_67)
    print pattern.P0_67




