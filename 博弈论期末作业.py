#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
#对列表中的数据求和
def sumx(x):
    r=0
    for i in x:
        r=r+i
    return r

#最优奖励
def max_R(n,s,t,c,u):
    temp=(n-1)/sumx(c)
    tt=[]
    for i in c:
        tt.append((1-i*temp)**2)
    r=(u*s*temp-1)/(2*u*t*temp**2*sumx(tt))
    return r

#最优有效数据载荷
def max_x(r,n,c,i):
    x=r*(n-1)/sumx(c)-c[i]*r*((n-1)**2/sumx(c)**2)
    return x

#感知用户收益
def u_R(r,x,c,i):
    return r*x[i]/sumx(x)-c*x[i]

#平台收益
def mcs(r,c,x,s,t,u):
    temp=[]
    for i in x:
        temp.append(s*i-t*i**2)
    return u*sumx(temp)-r-c


# In[2]:


s=80
t=0.01
n=3
u=100
C=[15,13,11]#用户成本集合

#最优奖励
r=max_R(n,s,t,C,u)

#最优有效数据载荷
cx=[]
for i in range(3):
    cx.append(max_x(r,n,C,i))

#用户2，用户3，平台执行最优策略，用户1上传不同量的有效数据集荷载
cx_=[]
for i in range(-2,3):
    temp=cx[0]+i*500
    cx_.append([temp,cx[1],cx[2]])

#感知用户收益
u_x=[[]for i in range(3)]
for j in range(3):
    for i in range(5):
        u_x[j].append(u_R(r,cx_[i],C[j],j))

fig=plt.figure()
x=["x*-1000","x*-500","x*","x*+500","x*+1000"]
cplt=fig.add_subplot() 
cplt.bar([i*1.5 for i in range(5)],u_x[0],fc="b",width=0.4)
cplt.bar([i*1.5+0.4 for i in range(5)],u_x[1],fc="r",width=0.4)
cplt.bar([i*1.5+0.8 for i in range(5)],u_x[2],fc="y",width=0.4)
cplt.set_xticks([i*1.5+0.4 for i in range(5)],x)
cplt.legend(labels=["感知用户1","感知用户2","感知用户3"])
plt.xlabel("感知用户1的有效数据载荷")
plt.ylabel("感知用户的收益")
plt.title("感知用户的收益条形图")


# In[3]:


#平台收益
mcsu=[]
for i in range(5):
    mcsu.append(mcs(r,10000,cx_[i],s,t,u))
        
plt.plot(x,mcsu,c="b")
plt.xlabel("感知用户1的有效数据载荷")
plt.ylabel("平台收益")
plt.title("平台收益折线图")


# In[4]:


#用户执行最优策略
mcs_r=[]
for i in range(-2,3):
    mcs_r.append(r+i*10000)
    
#不同奖励下用户提供的有效数据载荷
rx=[[]for i in range(3)]
for i in range(5):
    for j in range(3):
        rx[j].append(max_x(mcs_r[i],n,C,j))

fig=plt.figure()
x=["r*-20000","r*-10000","r*","r*+10000","r*+20000"]
rxplt=fig.add_subplot() 
rxplt.bar([i*1.5 for i in range(5)],rx[0],fc="b",width=0.4)
rxplt.bar([i*1.5+0.4 for i in range(5)],rx[1],fc="r",width=0.4)
rxplt.bar([i*1.5+0.8 for i in range(5)],rx[2],fc="y",width=0.4)
rxplt.set_xticks([i*1.5+0.4 for i in range(5)],x)
rxplt.legend(labels=["感知用户1","感知用户2","感知用户3"])
plt.xlabel("奖励")
plt.ylabel("感知用户的有效数据载荷")
plt.title("感知用户的有效数据载荷条形图")


# In[5]:


#感知用户收益
u_r=[[]for i in range(3)]
for j in range(3):
    for i in range(5):
        u_r[j].append(u_R(r,[rx[0][i],rx[1][i],rx[2][i]],C[j],j))

fig=plt.figure()
urplt=fig.add_subplot() 
urplt.bar([i*1.5 for i in range(5)],u_r[0],fc="b",width=0.4)
urplt.bar([i*1.5+0.4 for i in range(5)],u_r[1],fc="r",width=0.4)
urplt.bar([i*1.5+0.8 for i in range(5)],u_r[2],fc="y",width=0.4)
urplt.set_xticks([i*1.5+0.4 for i in range(5)],x)
urplt.legend(labels=["感知用户1","感知用户2","感知用户3"])
plt.xlabel("奖励")
plt.ylabel("感知用户的收益")
plt.title("感知用户的收益条形图")


# In[6]:


#不同奖励下的平台收益
mcsu_r=[]
for i in range(5):
    mcsu_r.append(mcs(mcs_r[i],10000,[rx[0][i],rx[1][i],rx[2][i]],s,t,u))
        
plt.plot(x,mcsu_r,c="b")
plt.xlabel("奖励")
plt.ylabel("平台收益")
plt.title("平台收益折线图")


# In[ ]:




