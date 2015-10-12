import numpy as np
import matplotlib.pyplot as plt 
class BrownianPaths:
	def BMs(self, M,N): 
		dt = self.T/np.float(self.N)	#h Resolucion
		self.Dt = self.R * self.dt;		#h multiplo
		self.L = self.N / self.R;
		#Calcula incrementos
		self.DistNormal=np.random.randn(M,N)
		self.dBs = np.sqrt(self.dt)*self.DistNormal
		self.Bs = np.cumsum(self.dBs,1)
		Bzero=np.zeros((M,1))
		self.Bs = np.concatenate((Bzero, self.Bs),axis=1)
	def InitializeMesh(self,k,p,r,T0,T):
		self.r=r		#potencia de escala
		self.k=k		#potencia de resoluci\'on
		self.T0=T0		#[T_0,T]
		self.T=T
		self.N=2**self.k	#N\'umero de particiones
		self.R=2**self.r	#Proporci\'on
		self.dt = self.T/np.float(self.N)	# h
		self.t=np.linspace(0,self.T,self.N+1)
		self.Dt = self.R * self.dt	#R*h
		self.L = self.N / self.R
		#Trayectoria de Resoluci\'on
		self.DistNormal=np.random.randn(np.int(self.N)) #Calcula incrementeos 
		self.dW = np.sqrt(self.dt)*self.DistNormal
		self.W = np.cumsum(self.dW)	#Trayectoria
		self.W = np.concatenate(([0], self.W))	
	def RBM(self):
		self.DeltaW=np.zeros(self.L)
		self.WDt=np.zeros(self.L)
		#Genera trayectoria de operaci\'on (Suma Telesc\'opica)
		for j in np.arange(self.L):
			self.Winc = np.sum(self.dW[self.R*(j):self.R*(j+1)])
			self.DeltaW[j]=self.Winc
		self.RW = np.cumsum(self.DeltaW)
		self.RW = np.concatenate(([0], self.RW))
		for j in np.arange(self.L):
			self.WDt[j] = np.sqrt(self.Dt) * self.DistNormal[j]
		self.RW2 = np.cumsum(self.WDt)
		self.RW2 = np.concatenate(([0], self.RW2))
	def PlotBM(self):
		plt.figure()
		plt.plot(self.t,self.W,'b-',alpha=1,label=r'$B_t$') 
		plt.plot(self.t[0:np.int(self.N+1):self.R], self.RW,'-o',color='orange',alpha=0.5, lw=2, label=r'$B_t^{(R\delta t)}$',ms=6, mfc='yellow')
		plt.plot(self.t[0:np.int(self.N+1):self.R], self.RW2,'r-s',alpha=1,label=r'$B_t^{(\Delta t)}$',ms=6, mfc='none', mec='red')
		plt.grid(True)
		plt.title(r'Movimiento Browniano')
		plt.legend(shadow=True,loc=0)
		#plt.figure()
		#plt.semilogy(self.t[0:np.int(self.N+1):self.R],self.W[0:np.int(self.N+1):self.R]-self.RW,'s-',alpha=1,label=r'$|B_t^{(h)}-B_t^{(Rh)}|$') 
		#plt.grid(True)
		#plt.title(r'diferencia')
		plt.legend(shadow=True,loc=0)
		plt.show()
	def PlotBMs(self):
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
		print'\t#Resolucion: {} \t #operacion: {}'.format(self.W.shape[0],self.RW.shape[0])
		print''
		print '\t E[W^(dt)]= {}\t E[W^(Rdt)]= {}\t E[W^(Dt)]={}'.format(self.W.mean(), self.RW.mean(), self.RW2.mean())
		print '\t E[W^(dt)^2]= {}\t E[W^(Rdt)^2]= {}\t E[W^(Dt)^2]={}'.format(self.W.var(), self.RW.var(),self.RW2.var())
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
##############################################################################
##########################Class Implementation################################
k=16
r=12
T = 2.0**(0)#time in  [T0,T]
T0=0.0
BPS=BrownianPaths()
BPS.InitializeMesh(k,r,r,T0,T)
BPS.RBM()
BPS.PlotBM()
BPS.Resumen()
'''
BPS.BMs(100,100000)
BPS.PlotBMs()
'''