import numpy as np
import matplotlib.pyplot as plt
__c0__=299792458

class DSP:
	"""dispersion class """
	
	
	def __init__(self):
		self.name=""
	def getnName(self):
		return self.name
		
	def setname(self,name):
		self.name=name
		
	def e2index(self,e):
		return (((e.real+((e.real)**2+(e.imag)**2)**0.5))/2)**0.5+((((-1)*e.real+((e.real)**2+(e.imag)**2)**0.5)/2)**0.5)*1j
		
	def index2e(self,nki):
		return ((nki.real)**2-(nki.imag)**2)-(2*nki.real*nki.imag)*1j	
		
	def l2w(self,l):
		return ((2*np.pi)*__c0__/(l*10**(-6)))
		
	def setcauchy(self,A,B,sl,el,step):
		self.lamda=np.arange(float(sl),float(el)+step,float(step))
		
		self.w=self.l2w(self.lamda)
		self.n=A*(1.0+B/((self.lamda)**2))+1.0
		self.k=0*self.lamda
		self.nk=self.n+(1j)*(self.k)
		
		
	def setsellmier(self,A1,A2,A3,B1,B2,B3,sl,el,step):
		self.lamda=np.arange(float(sl),float(el)+step,float(step))
		self.w=self.l2w(self.lamda)
		self.n=((A1*(self.lamda**2)/(self.lamda**2-B1))+(A2*(self.lamda**2)/(self.lamda**2-B2))+(A3*(self.lamda**2)/(self.lamda**2-B3)+1.0))**0.5
		self.k=0*self.lamda
		self.nk=self.n+(1j)*(self.k)
		
		
	def setdrude(self,wp,t,sl,el,step):
		self.lamda=np.arange(float(sl),float(el)+step,float(step))
		self.w=(2*np.pi)*__c0__/(self.lamda*10**(-6))
		self.ep=1-(wp**2/(self.w*((self.w+1j)/t)))
		self.nk=(self.e2index(self.ep))
		
	def setdata(self,n,k,sl,el,step):
		self.lamda=np.arange(float(sl),float(el)+step,float(step))
		self.w=(2*np.pi)*__c0__/(self.lamda*10**(-6))
		self.nk=np.array([n+k*1j])
		
		
'''
t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
'''

dp=DSP()

dp.setname("a")
dp.setcauchy(0.5,10000.0,100,200,2)
print(dp.nk)

plt.plot(dp.lamda, dp.nk.real)
plt.plot(dp.lamda, dp.nk.imag)
plt.grid(True)
plt.xlabel('t')
plt.ylabel('G')
plt.gca().set_ylim([-1.0, 5.0])
plt.legend()
plt.show()
