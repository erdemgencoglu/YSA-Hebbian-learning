import numpy

s_y_67=numpy.array([        #Sifir %67 kayip patterni
    [-1,  1,  1,  1, -1],
    [ 1, -1, -1, -1,  1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]])

s_y_70=numpy.array([        #Sifir %70 civari kayip patterni
    [-1,  1,  1,  1, -1],
    [-1, -1, -1, -1,  1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]])

s_g=numpy.array([           #Sifir gurultulu patterni
    [-1,  -1,  1,  1, -1],
    [ 1,  -1, -1,  1, -1],
    [ 1,  -1, -1, -1,  1],
    [-1,  -1, -1, -1, -1],
    [ 1,  -1,  1, -1,  1],
    [-1,   1, -1,  1, -1]])



b_y_67=numpy.array([        #Bir %67 civari kayip patterni
    [-1,  1,  1,  -1,  -1],
    [-1, -1,  1,  -1,  -1],
    [-1, -1, -1,  -1,  -1],
    [-1, -1, -1,  -1,  -1],
    [-1, -1, -1,  -1,  -1],
    [-1, -1, -1,  -1,  -1]])

b_y_90=numpy.array([        #Bir  %85 civari kayip patterni
    [-1,  1,  1,  -1, -1],
    [-1, -1, -1, -1,  1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1]])

b_y_70=numpy.array([        #Bir gurultulu pattern
    [-1,  1,  1, -1, -1],
    [-1, -1,  1,  1, -1],
    [ 1, -1,  1, -1, -1],
    [-1, -1, -1, -1,  1],
    [-1, -1,  1, -1, -1],
    [ 1,  1,  1,  1, -1]])


p0=(-1, 1, 1, 1, 1,-1,1,-1,-1,-1,-1, 1,1,-1,-1,-1,-1,1, 1,-1,-1,-1,-1, 1,-1, 1, 1, 1, 1,-1)
p1=numpy.array([-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,-1,1, 1, 1, 1, 1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
p2=numpy.array([ 1,-1,-1,-1,-1,-1,1,-1,-1, 1, 1, 1,1,-1,-1, 1,-1,1,-1, 1, 1,-1,-1, 1,-1,-1,-1,-1,-1, 1])