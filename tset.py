# -*- coding: utf-8 -*-  
  
  
from scipy import signal  
import numpy as np  
import matplotlib.pyplot as pl  
import matplotlib  
import math  
  
N = 500  
fs = 5  
n = [2*math.pi*fs*t/N for t in range(N)]  
axis_x = np.linspace(0,1,num=N)  
#设置字体文件，否则不能显示中文  
myfont = matplotlib.font_manager.FontProperties(fname='c:\\windows\\fonts\\fzshjw_0.ttf')  
  
#频率为5Hz的正弦信号  
x = [math.sin(i) for i in n]  
pl.subplot(221)  
pl.plot(axis_x,x)  
pl.title(u'5Hz的正弦信号', fontproperties=myfont)  
pl.axis('tight')  
  
xx = []  
x1 = [math.sin(i*10) for i in n]  
for i in range(len(x)):  
    xx.append(x[i] + x1[i])  
   
pl.subplot(222)  
pl.plot(axis_x,xx)  
pl.title(u'5Hz与50Hz的正弦叠加信号', fontproperties=myfont)  
pl.axis('tight')  
  
b,a = signal.butter(3,0.08,'low')  
sf = signal.filtfilt(b,a,xx)  
  
pl.subplot(223)  
pl.plot(axis_x,sf)  
pl.title(u'低通滤波后', fontproperties=myfont)  
pl.axis('tight')  
  
b,a = signal.butter(3,0.10,'high')  
sf = signal.filtfilt(b,a,xx)  
  
pl.subplot(224)  
pl.plot(axis_x,sf)  
pl.title(u'高通滤波后', fontproperties=myfont)  
pl.axis('tight')  

pl.show()