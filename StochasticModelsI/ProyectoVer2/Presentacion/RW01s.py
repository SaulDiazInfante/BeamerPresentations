import numpy as np
import matplotlib.pyplot as plt 

def RWs(M, N, h):
    delta = T/np.float(N)
    b=np.zeros((M,N), h)
    b= np.random.binomial(1,.5, (M, N))
    omega=2.0*b-1
    Xn=h*(omega.cumsum(axis=1))
    X0=np.zeros(omega.shape[0])
    X0=X0.reshape(M,1)
    Xn = np.concatenate((X0, Xn),axis=1)
    return Xn

T=1.0
M=100
N=1000
h=1.0/np.sqrt(np.float(N))
RWs01=RWs(M, N, h)
t=np.linspace(0,T,N+1)
M = np.abs(RWs01).max()+h
mu=RWs01.mean(axis=0)
#
for i in np.arange(RWs01.shape[0]):
  plt.plot(t,RWs01[i],'g-',alpha=0.5,lw=1,ms=9,mfc='green')
plt.plot(t,mu,'r-',label=r'$E[X_n]$')
plt.xlabel(r'$transiciones$')
plt.ylabel(r'$X_n$')
plt.title(r'Caminatas aleatorias en [0,1]')
plt.grid(True)
plt.legend(shadow=True,loc=0)
plt.show()
