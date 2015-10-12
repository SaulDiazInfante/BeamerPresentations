import numpy as np
import matplotlib.pyplot as plt 
class BrownianPaths:
    def BMs(self, M,N):#Stensil of the mesh
        dt = self.T/np.float(self.N)
        self.Dt = self.R * self.dt;
        self.L = self.N / self.R;
    #%  Compute the Brownian increments, and the discretized Brownian path.
        self.DistNormal=np.random.randn(M,N)
        self.dBs = np.sqrt(self.dt)*self.DistNormal
        self.Bs = np.cumsum(self.dBs,1)
        Bzero=np.zeros((M,1))
        self.Bs = np.concatenate((Bzero, self.Bs),axis=1)
        
        #self.Dw=np.sqrt(self.Dt)*self.DistNormal[0:self.L]
        #self.W2 = np.cumsum(self.Dw)
        #self.W2 = np.concatenate(([0], self.W2))
    
    
    def InitializeMesh(self,k,p,r,T0,T):#Stensil of the mesh
        self.p=p
        self.r=r
        self.k=k
        self.T0=T0
        self.N=2**self.k
        self.P=2**self.p
        self.R=2**self.r
        self.T=T
        
        self.dt = self.T/np.float(self.N)
        self.t=np.linspace(0,self.T,self.N+1)
        self.Dt = self.R * self.dt;
        self.L = self.N / self.R;
    #%  Compute the Brownian increments, and the discretized Brownian path.
        self.DistNormal=np.random.randn(np.int(self.N))
        self.dW = np.sqrt(self.dt)*self.DistNormal
        self.W = np.cumsum(self.dW)
        self.W = np.concatenate(([0], self.W))
        
        self.Dw=np.sqrt(self.Dt)*self.DistNormal[0:self.L]
        self.W2 = np.cumsum(self.Dw)
        self.W2 = np.concatenate(([0], self.W2))
    def RBM(self):
    #%  Preallocate Xem for efficiency.
        self.DeltaW=np.zeros(self.L)
        for j in np.arange(self.L):
            self.Winc = np.sum(self.dW[self.R*(j):self.R*(j+1)])
            self.DeltaW[j]=self.Winc
        self.RW = np.cumsum(self.DeltaW)
        self.RW = np.concatenate(([0], self.RW))
    def PlotBM(self):
        plt.figure()
        plt.plot(self.t,self.W,'g-o',lw=2, ms=4, mfc='black', alpha=.60,label=r'$B_t$') 
        #plt.plot(self.t[0:np.int(self.N+1):self.R], self.RW,'r-o',lw=2, alpha=.5,label=r'$B_t^{(R\delta t)}$',ms=10, mfc='orange')
        plt.grid(True)
        plt.title(r'Movimiento Browniano')
        plt.legend(shadow=True,loc=0)
        #plt.figure()
        #plt.semilogy(self.t[0:np.int(self.N+1):self.R],self.W[0:np.int(self.N+1):self.R]-self.RW,'s-',alpha=1,label=r'$|B_t^{(h)}-B_t^{(Rh)}|$') 
        #plt.grid(True)
        #plt.title(r'diferencia')
        #plt.legend(shadow=True,loc=2)
        plt.show()
    def PlotBMs(self):
        t=self.dt*np.arange(self.Bs.shape[1])
        plt.figure()
        for j in np.arange(self.Bs.shape[0]):
            plt.plot(self.dt*np.arange(self.Bs.shape[1]),self.Bs[j],'-',mfc='none',mec='blue',alpha=.1,label=r'$B_t$') 
        plt.plot(t,np.mean(self.Bs, axis=0), 'r.', ms=1,alpha=1.0,label=r'$E[B_t]$')
        plt.grid(True)
        plt.title(r'Movimiento Browniano')
        plt.show()
    def PlotBMSigma(self):
        t=self.dt*np.arange(self.Bs.shape[1])
        plt.figure()
        for j in np.arange(self.Bs.shape[0]):
            plt.plot(self.dt*np.arange(self.Bs.shape[1]),self.Bs[j],'-',mfc='none',mec='blue',alpha=.1,label=r'$B_t$') 
        plt.plot(t,np.mean(self.Bs, axis=0), 'r.', ms=1,alpha=1.0,label=r'$E[B_t]$')
        plt.plot(t,np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$\sqrt{t}$')
        plt.plot(t,2.0*np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$2\sqrt{t}$')
        plt.plot(t,3.0*np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$2\sqrt{t}$')
        plt.plot(t,-np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$\sqrt{t}$')
        plt.plot(t,-2.0*np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$2\sqrt{t}$')
        plt.plot(t,-3.0*np.sqrt(t), 'g.',ms=1.0,alpha=.5,label=r'$2\sqrt{t}$')
        plt.grid(True)
        plt.title(r'Movimiento Browniano')
        plt.show()
    def  Resumen(self):
		print'{:*^90}'.format('')
		print'{:^90}'.format('Resumen')
		print'{:*^90}'.format('')
		print'{:^90}'.format('Parametros de simulacion:')
		print'\tResolucion: {} \t operacion: {}'.format(self.dt,self.Dt)
		print'\t#Resolucion: {} \t #operacion: {}'.format(self.W.shape[0],self.W2.shape[0])
		print''
		print '\t E[W^(dt)]= {}\t E[W^(Rdt)]= {}\t E[W^(Dt)]={}'.format(self.W.mean(), self.RW.mean(), self.W2.mean())
		print '\t E[W^(dt)^2]= {}\t E[W^(Rdt)^2]= {}\t E[W^(Dt)^2]={}'.format(self.W.var(), self.RW.var(), self.W2.var())
    def IntegralBW(self, alpha):
        self.I_dB_t=0.0
        for j in np.arange( self.N):
            dW=self.W[j+1]-self.W[j]
            self.I_dB_t=self.I_dB_t+alpha*dW
        print "I=", self.I_dB_t 
     
    def IntegralBRW(self, alpha):
        self.I_dB_Rt=0.0
        for j in np.arange( self.L):
            dW=self.RW[j+1]-self.RW[j]
            self.I_dB_Rt=self.I_dB_Rt+alpha*dW
        print "Ir=", self.I_dB_Rt 
    def IntegralBRW2(self, alpha):
        self.I_dB_W2t=0.0
        for j in np.arange( self.L):
            dW=self.W2[j+1]-self.W2[j]
            self.I_dB_W2t=self.I_dB_W2t+alpha*dW
        print "I_W2=", self.I_dB_W2t 

BPS=BrownianPaths()
k=12
p=4
r=4
T = 2.0**(0)#time in  [T0,T]
T0=0.0
alpha=1.0
BPS.InitializeMesh(k,p,r,T0,T)
BPS.RBM()
BPS.BMs(1000,10000)
#BPS.PlotBMs()
BPS.PlotBM()
BPS.PlotBMSigma()
#BPS.Resumen()
#BPS.IntegralBW(alpha)
#BPS.IntegralBRW(alpha)
#BPS.IntegralBRW2(alpha)
