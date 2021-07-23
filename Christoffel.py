import numpy as np
import Calculus as calc
import Metric as mt

def InitC(C):
    C = np.zeros((4,4,4))
    return C

def SqrBrakets(g, x, i, j, k):
    DiGkj = calc.DPartial(i,g[k,j],x)
    DjGki = calc.DPartial(j,g[k,i],x)
    DkGij = calc.DPartial(k,g[i,j],x)

    return 0.5*(DiGkj + DjGki - DkGij)

def Gamma(g_ij, gij_, x, l, i, j):
    ckGamma = 0
    ckGamma += gij_[l,0](x)*SqrBrakets(g_ij,x,i,j,0)
    ckGamma += gij_[l,1](x)*SqrBrakets(g_ij,x,i,j,1)
    ckGamma += gij_[l,2](x)*SqrBrakets(g_ij,x,i,j,2)
    ckGamma += gij_[l,3](x)*SqrBrakets(g_ij,x,i,j,3)

    return ckGamma

def ChristoffelSymbol(C, g_ij, gij_, x):
    for l in range(4):
        for i in range(4):
            for j in range(4):
                C[l,i,j] = Gamma(g_ij,gij_,x,l,i,j)
    return C

