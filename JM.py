import numpy	as np

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
def wave(Ex,Ey,fai,delta):
	return [[Ex*np.e**(fai*1j),Ey*np.e**((fai+delta)*1j)],[Ex*np.e**(fai*1j)*(np.conj(Ex*np.e**(fai*1j))),Ey*np.e**((fai+delta)*1j)*np.conj(Ey*np.e**((fai+delta)*1j))],[Ex**2+Ey**2,Ex**2-Ey**2],[2*Ey*Ex*np.cos(delta),2*Ey*Ex*np.sin(delta)]]

'''デバッグ
print(JwaveP(1/4*np.pi,1/4*np.pi))
print(JLinerP(1/4*np.pi))
print("print wave")
print(wave(1,1,1,1/4*np.pi))"""
