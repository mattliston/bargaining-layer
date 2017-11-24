import numpy as np
import matplotlib.pyplot as plt


def bargain(w,n,stochastic_utility): #w is the weight vector, n is the number of weights bargaining over each prize
    b_w=np.zeros(w.shape[0])
    if stochastic_utility==True:
        u=np.random.rand(w.shape[0])
        for i in range(0,w.shape[0],n):
            init=i #keeps track of the initial i, could be cleaner
            for j in range(0,n):
                b_w[i]=(w[i]*u[i])/(np.sum(np.multiply(w[init:n+init],u[init:n+init]))) #w[init]*u[init]+w[init+1]*u[init+1] 
    #            print w[i],np.sum(w[init:n+init])
                i+=1 #makes bargaining sets exclusive, -ex. n=2 ((0,1),(2,3)...(i-1,i)) vs ((0,1),(1,2)...)
        return b_w

    else:
        for i in range(0,w.shape[0],n):
            init=i #keeps track of the initial i, could be cleaner
            for j in range(0,n):
                b_w[i]=(w[i]/(np.sum(w[init:n+init]))) 
    #            print w[i],np.sum(w[init:n+init])
                i+=1 #makes bargaining sets exclusive, -ex. n=2 ((0,1),(2,3)...(i-1,i)) vs ((0,1),(1,2)...)
        return b_w

def plot(w,n):
    plt.plot(w)
    for i in range(1,n):
        print i, n, n%i
        if n%i==0:
            plt.plot(bargain(w,i,True))
        else:
            continue

    plt.show()

x=np.random.rand(100)
plot(x,x.shape[0])

