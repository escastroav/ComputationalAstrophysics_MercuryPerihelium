import numpy as np

dx = 1.3e-8
dt = 1.3e-8

def DPartial(i,g,x):
    x[i] -= 2*dx
    d1 = g(x)
    x[i] += dx
    d2 = g(x)
    x[i] += 2*dx
    d3 = g(x)
    x[i] += dx
    d4 = g(x)
    x[i] -= 2*dx

    return (d1-8*d2+8*d3-d4)/(12*dx)

def RK4(f2, C, x0, x1, x2, t):
    dx01=np.zeros(4); dx02=np.zeros(4); dx03=np.zeros(4); dx04=np.zeros(4)  
    dx11=np.zeros(4); dx12=np.zeros(4); dx13=np.zeros(4); dx14=np.zeros(4)    
    dx21=np.zeros(4); dx22=np.zeros(4); dx23=np.zeros(4); dx24=np.zeros(4)

    dx01=x2*dt
    dx11=x2*dt
    for i in range(4): dx21[i]=f2[i](C,x0,x1,x2,t)*dt

    x0 += 0.5*dx01
    x1 += 0.5*dx11
    x2 += 0.5*dx21

    dx02=x2*dt
    dx12=x2*dt
    for i in range(4): dx22[i]=f2[i](C,x0,x1,x2,t+0.5*dt)*dt

    x0 += 0.5*dx02 
    x1 += 0.5*dx12 
    x2 += 0.5*dx22 

    dx03=x2*dt
    dx13=x2*dt
    for i in range(4): dx23[i]=f2[i](C,x0,x1,x2,t+0.5*dt)*dt

    x0 += dx03 
    x1 += dx13 
    x2 += dx23

    dx04=x2*dt
    dx14=x2*dt
    for i in range(4): dx24[i]=f2[i](C,x0,x1,x2,t+dt)*dt

    x0 += (dx01+2*(dx02+dx03)+dx04)/6.0
    x1 += (dx11+2*(dx12+dx13)+dx14)/6.0
    x0 += (dx21+2*(dx22+dx23)+dx24)/6.0

    return x0, x1, x2

    
    
    
