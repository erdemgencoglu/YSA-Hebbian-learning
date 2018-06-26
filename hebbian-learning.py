import pattern_bilgileri
import numpy
import math
import hardlims

p1=numpy.array([     #0 sayisinin pattern bilgisi
    [-1,  1,  1,  1, -1],
    [ 1, -1, -1, -1,  1],
    [ 1, -1, -1, -1,  1],
    [ 1, -1, -1, -1,  1],
    [ 1, -1, -1, -1,  1],
    [-1,  1,  1,  1, -1]])

p2=numpy.array([     #1 sayisinin pattern bilgisi
    [-1,  1, 1, -1, -1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, -1],
    [-1, -1, 1, -1, -1]])

p3=numpy.array(     #2 sayisinin pattern bilgisi
    [[1,1,1,-1,-1],
    [-1,-1,-1,1,-1],
    [-1,-1,-1,1,-1],
    [-1,1,1,-1,-1],
    [-1,1,-1,-1,-1],
    [-1,1,1,1,1]])

# Beklenen ciktilar
T1=p1
T2=p2
T3=p3

Wnew=[]  #Yeni agirlik matrisi
Wold=[]  #Eski agirlik matrisi
alpha=1  #Ogrenme hizi sabit verdik
a=[]


#Transpoz aldirma metodu
def transpose(matris):
    return numpy.matrix.transpose(matris)

# Ortonormal olup olmadigini kontrol eder
def is_ortonormal(p,t):

    transposeMatris=transpose(p)
    sonuc=numpy.dot(transposeMatris,p)

    if numpy.array_equal(numpy.identity(5),sonuc):#Birim matrise esit mi?
        print "Birim matrise esit"
        W=numpy.dot(t,transpose(p))
        test(W,p,t)
    else:
        b=make_ortonormal(transposeMatris[0])  #matrisin satirlari bizim ortonormal yapacagimiz kisim yatay gelio!
        c=make_ortonormal(transposeMatris[1])
        d=make_ortonormal(transposeMatris[2])
        e=make_ortonormal(transposeMatris[3])
        f=make_ortonormal(transposeMatris[4])
        olustur=numpy.array([b,c,d,e,f])
        W=numpy.dot(t,olustur) #Agirlik matrisini bulmus olduk 6x6
        test(W,p,t)

# Ortonormal yapma metodu
def make_ortonormal(p):

    carpim=numpy.dot(transpose(p),p)
    karekok=math.sqrt(carpim)
    bolum=numpy.divide(p,karekok)
    return bolum


def test(W,p,t):
    global Wold
    global Wnew
    global a

    a=hardlims.hardlims(numpy.dot(W,p))
    Wold=W #ilk deger gelen agirlik matrisene esittir

    print("Test sonucu")
    print("a=hardlims(W*P)\n"),a
    # print("p"),p
    if numpy.array_equal(a,t):
        print("Beklenen cikti ile esit")

    else:
        print ("Beklenen cikti ile esit degil Wnew hesapla\n")
        Wnew=Wold+(alpha*(numpy.dot(t,transpose(p))))
        a2=hardlims.hardlims(numpy.dot(Wnew,p))



# print is_ortonormal(pattern_bilgileri.b_y_67,T2)
print is_ortonormal(p2,T2)
