import numpy as np
import Constants as cte
def zero(x):
    return 0;

def g_ij(x):
    g = np.zeros((4,4))

    g[0,0] = -1/(1-2*cte.Rs/x[0])
    g[1,1] = -x[0]**2.0
    g[2,2] = -(x[0]*np.sin(x[1]))**2.0
    g[3,3] = (1-2*cte.Rs/x[0])

    return g

def gij_(x):
    g = np.zeros((4,4))

    g[0,0] = -(1-2*cte.Rs/x[0])
    g[1,1] = -x[0]**(-2.0)
    g[2,2] = -(x[0]*np.sin(x[1]))**(-2.0)
    g[3,3] = 1/(1-2*cte.Rs/x[0])

    return g
    

#def g_00(x):
#    return -1/(1-2*cte.Rs/x[0])
#def g_11(x):
#    return -x[0]**2.0
#def g_22(x):
#    return -(x[0]*np.sin(x[1]))**2.0
#def g_33(x):
#    return (1-2*cte.Rs/x[0])

#def g00_(x):
#    return -(1-2*cte.Rs/x[0])
#def g11_(x):
#    return -x[0]**(-2.0)
#def g22_(x):
#    return -(x[0]*np.sin(x[1]))**(-2.0)
#def g33_(x):
#    return 1/(1-2*cte.Rs/x[0])

#def InitMetric():
#    g_ij = np.array([[g_00,zero,zero,zero],
#                     [zero,g_11,zero,zero],
#                     [zero,zero,g_22,zero],
#                     [zero,zero,zero,g_33]]);
#    gij_ = np.array([[g00_,zero,zero,zero],
#                     [zero,g11_,zero,zero],
#                     [zero,zero,g22_,zero],
#                     [zero,zero,zero,g33_]])

#    return g_ij, gij_
