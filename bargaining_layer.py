
import numpy as np
import matplotlib.pyplot as plt


def bargain(w,n): #w is the weight vector, n is the number of weights bargaining over each prize
    b_w=np.zeros(w.shape[0])
    for i in range(0,w.shape[0],n):
        print i
        init=i #keeps track of the initial i, could be cleaner
        for j in range(0,n):
            b_w[i]=(w[i]/(np.sum(w[init:n+init]))) 
#            print w[i],np.sum(w[init:n+init])
            i+=1 #makes bargaining sets exclusive, -ex. n=2 ((0,1),(2,3)...(n-1,n)) vs ((0,1),(1,2)...)
            print i
    return b_w

def plot(w,n):
    plt.plot(w)
    for i in range(1,n):
        print i, n, n%i
        if n%i==0:
            plt.plot(bargain(w,i))
        else:
            continue

    plt.show()

x=np.random.rand(100000)
plot(x,x.shape[0])
