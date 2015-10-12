#
#Calcula m caminatas aleatorias de N pasos
#
#
import numpy as np 
import matplotlib.pyplot as plt
def randwalk(M,N):
     
    delta=np.zeros((M,N))
    delta=2.0*((np.random.rand(M,N)>0.5))-1.0 #sucesion de v.a. Bernulli
    delta=np.cumsum(delta,axis=1)
    X0=np.zeros(delta.shape[0])
    #
    X0=X0.reshape(M,1)
    X = np.concatenate((X0, delta),axis=1)
    return X
M=100
N=1000
t = np.arange(N+1)
RW=randwalk(M,N)
mu=RW.mean(axis=0)
for i in np.arange(RW.shape[0]):
  plt.plot(t,RW[i],'b-',alpha=0.5,lw=1,ms=9,mfc='blue')
plt.plot(t,mu,'r-',label=r'$E[X_n]$')
plt.plot(t,np.sqrt(t),'y-',lw=3,label=r'$\sigma$')
plt.plot(t,2.0*np.sqrt(t),'y-',lw=3,label=r'$2\sigma$')
plt.plot(t,3.0*np.sqrt(t),'y-',lw=3,label=r'$3\sigma$')
plt.plot(t,-3.0*np.sqrt(t),'y-',lw=3)
plt.plot(t,-2.0*np.sqrt(t),'y-',lw=3)
plt.plot(t,-np.sqrt(t),'y-',lw=3)
plt.xlabel(r'$transiciones$')
plt.ylabel(r'$X_n$')
plt.title(r'Caminatas aleatorias')
plt.grid(True)
plt.legend(shadow=True,loc=0)
plt.show()
