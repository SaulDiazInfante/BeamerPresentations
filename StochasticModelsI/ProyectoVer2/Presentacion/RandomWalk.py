import numpy as np
import matplotlib.pyplot as plt

def randwalk(N):
     #%t=[0,1,2,..., N]
    delta=np.zeros(N)
    delta=2.0*((np.random.rand(N)>0.5))-1.0 #sucesion de v.a. Bernulli
    X = np.cumsum(delta)                    #Calcula la suma de las v.a Bernulli
    X = np.concatenate(([0], X))
    return X
N=10
t = np.arange(N+1)
RW=randwalk(N)
M = np.abs(RW).max()+5
mu=RW.mean()*np.ones(RW.shape)
plt.plot(t,RW,'k-*',alpha=0.8,lw=1,ms=9,mfc='yellow',label=r'$RW$')
#plt.plot(t,mu,'r-',label=r'$E[X_n]$')
plt.xlabel(r'$transiciones$')
plt.ylabel(r'$X_n$')
plt.title(r'n')
plt.grid(True)
plt.legend(shadow=True,loc=0)
plt.show()
