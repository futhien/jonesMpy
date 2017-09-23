import numpy	as np

_sizeOf_=2
X=np.arange(_sizeOf_)
Y=np.arange(_sizeOf_)
Ax=1*np.random.random((_sizeOf_,_sizeOf_))
Ay=1*np.random.random((_sizeOf_,_sizeOf_))
fai=np.pi*2*np.random.random((_sizeOf_,_sizeOf_))
delta=np.pi*2*np.random.random((_sizeOf_,_sizeOf_))

'''
Ex=1*np.ones((_sizeOf_,_sizeOf_))
Ey=2*np.ones((_sizeOf_,_sizeOf_))
fai=np.pi*2*np.random.random((_sizeOf_,_sizeOf_))
delta=0*np.ones((_sizeOf_,_sizeOf_))'''
'''位相板 fai位相がずれる。sitaだけ板が回転'''
def JwaveP(fai,sita):
	return np.array([[np.cos(fai/2)+(np.sin(fai/2)*np.cos(2*sita))*1j,(np.sin(fai/2)*np.sin(2*sita))*1j],[(np.sin(fai/2)*np.sin(2*sita))*1j,np.cos(fai/2)-(np.sin(fai/2)*np.cos(2*sita))*1j]])
	
'''偏光子sitaだけ板が回転'''
def JLinerP(sita):
	return [[np.cos(sita)**2,np.sin(sita)*np.cos(sita)],[np.sin(sita)*np.cos(sita),np.sin(sita)**2]]
	
'''各種特殊偏光子'''
_JLVP_= [[0,0],[0,1]]
_JLHP_= [[1,0],[0,0]]
_JLP45_= [[1,1],[1,1]]
_JLPm45_= [[1,-1],[-1,1]]


'''厚みと屈折率差から位相遅れを計算・・・rad'''	
def reterdation(ne,no,d,lam):
	return (ne-no)*d*2*np.pi/lam
'''進行波 電界強度、位相(x基準)、位相差、で規定
   進行波、I、s1、s2、s2、s4を返す'''

'''
def wave(Ex,Ey,fai,delta):
	return [[Ex*np.e**(fai*1j),Ey*np.e**((fai+delta)*1j)],[Ex*np.e**(fai*1j)*(np.conj(Ex*np.e**(fai*1j))),Ey*np.e**((fai+delta)*1j)*np.conj(Ey*np.e**((fai+delta)*1j))],[Ex**2+Ey**2,Ex**2-Ey**2],[2*Ey*Ex*np.cos(delta),2*Ey*Ex*np.sin(delta)]]
'''
'''進行波 電界強度、位相(x基準)、位相差、で規定
   Ax,Ay,Ex(fai),Ey(fai),fai(x),delta(y-x),Ix,Iy'''
def wave(Ax,Ay,fai,delta):
	return Ax,Ay,Ax*np.e**(fai*1j),Ay*np.e**((fai+delta)*1j),fai,delta,Ax*np.e**(fai*1j)*(np.conj(Ax*np.e**(fai*1j))),Ay*np.e**((fai+delta)*1j)*np.conj(Ay*np.e**((fai+delta)*1j))
'''
print(JwaveP(1/4*np.pi,1/4*np.pi))
print(JLinerP(1/4*np.pi))
print("print wave/n")
'''
print("Ax")
print(Ax)

print("Ay")
print(Ay)

print("fai")
print(fai)

print("delta")
print(delta) 

print("wave")
result=wave(Ax,Ay,fai,delta)
print("Ax")
print(result[0])
print("Ay")
print(result[1])
print("Ex")
print(result[2])
print("Ex")
print(result[3])
print("fai")
print(result[4])
print("delta")
print(result[5])
print("Ix")
print(result[6])
print("Iy")
print(result[7])
