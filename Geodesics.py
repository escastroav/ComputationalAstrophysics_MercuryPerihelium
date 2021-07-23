import Metric as mtr
import Christoffel as ch
import Calculus as cl
import numpy as np

def f01(C, x0, x1, x2, t):
    return x2[0]
def f11(C, x0, x1, x2, t):
    return x2[1]
def f21(C, x0, x1, x2, t):
    return x2[2]
def f31(C, x0, x1, x2, t):
    return x2[3]
def f02(C, x0, x1, x2, t):
    C0 = C[0,:,:]
    x_11 = np.tensordot(x1, x1, axes=0)
    sum = np.tensordot(C0, x_11, axes=2)
    #sum = 0
    #for i in range(4):
    #    for j in range(4):
    #        sum += ch.Gamma(g_ij, gij_, x0, 0, i, j)*x1[i]*x1[j];

    return -sum;
def f12(C, x0, x1, x2, t):
    C0 = C[1,:,:]
    x_11 = np.tensordot(x1, x1, axes=0)
    sum = np.tensordot(C0, x_11, axes=2)
    #sum = 0
    #for i in range(4):
    #    for j in range(4):
    #        sum += ch.Gamma(g_ij, gij_, x0, 1, i, j)*x1[i]*x1[j];

    return -sum;
def f22(C, x0, x1, x2, t):
    C0 = C[2,:,:]
    x_11 = np.tensordot(x1, x1, axes=0)
    sum = np.tensordot(C0, x_11, axes=2)
    #sum = 0
    #for i in range(4):
    #    for j in range(4):
    #        sum += ch.Gamma(g_ij, gij_, x0, 2, i, j)*x1[i]*x1[j];

    return -sum;
def f32(C, x0, x1, x2, t):
    C0 = C[3,:,:]
    x_11 = np.tensordot(x1, x1, axes=0)
    sum = np.tensordot(C0, x_11, axes=2)
    #sum = 0
    #for i in range(4):
    #    for j in range(4):
    #        sum += ch.Gamma(g_ij, gij_, x0, 3, i, j)*x1[i]*x1[j];

    return -sum;

def SolveGeodesics(g_ij, gij_, x0, x1, x2, t, tmax):
    #f1 = np.array([f01,f11,f21,f31])
    f2 = np.array([f02,f12,f22,f32])
    t = 0
    data = np.empty((0,11),float)
    C = np.zeros((4,4,4))
    for t_n in range(tmax):
        t = cl.dt*t_n
        data = np.append(data, np.array([[t,
                                          x0[0],
                                          x0[1],
                                          x0[2],
                                          x0[3],
                                          x1[0],
                                          x1[1],
                                          x1[2],
                                          x1[3],
                                          x0[0]*np.cos(x0[2])*np.sin(x0[1]),
                                          x0[0]*np.sin(x0[2])*np.sin(x0[1])]]),
                         axis=0)
        #print(f'{t:.4f}',
        #      f'{x0[0]:.4f}',
        #      f'{x0[1]:.4f}',
        #      f'{x0[2]:.4f}',
        #      f'{x0[3]:.4f}',
        #      f'{x1[0]:.4f}',
        #      f'{x1[1]:.4f}',
        #      f'{x1[2]:.4f}',
        #      f'{x1[3]:.4f}',
        #      f'{x0[0]*np.cos(x0[2])*np.sin(x0[1]):.4f}',
        #      f'{x0[0]*np.sin(x0[2])*np.sin(x0[1]):.4f}')
        C = ch.ChristoffelSymbol(C, g_ij, gij_, x0)
        cl.RK4(f2,C,x0,x1,x2,t)
    return data
        

    

