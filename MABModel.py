import numpy as np
import random

class MABModel(object):
    q = np.zeros(1) # bernoulli correlation probabilities
    p = np.zeros(1) # bernoulli arm probabilities
    curState = 0 # previous arm pulled
    
    def __init__(self, K):
        self.q = np.zeros(K)
        self.p =np.zeros([K,K])
        for i in range(K):
            self.q[i] = random.uniform(0, 1)
            for j in range(K):
                self.p[i,j] = random.uniform(0, 1)
        self.curState = random.randint(0,2)
    def getArm(self, state):
        temp = 0
        if(random.uniform(0,1) < self.q[state]):
            temp += 1
        if(random.uniform(0,1) < self.p[self.curState,state]):
            temp += 1
        self.curState = state
        return temp/2
    def getq(self):
        return self.q
    def getp(self):
        return self.p


class AdversarialMABModel(object):
    q = np.zeros(1) # bernoulli correlation probabilities
    p = np.zeros(1) # bernoulli arm probabilities
    curState = 0 # previous arm pulled
    
    def __init__(self, K):
        self.q = np.zeros(K)
        self.p =np.zeros([K,K])
        for i in range(K):
            self.q[i] = random.uniform(0, 1)
            for j in range(K):
                self.p[i,j] = random.uniform(0, 1)
        self.curState = random.randint(0,2)
    def getArm(self, state):
        temp = 0
        if(random.uniform(0,1) < self.q[state]):
            temp += 1
        if(random.uniform(0,1) < self.p[self.curState,state]):
            temp += 1
        self.curState = state
        return temp/2
    def getq(self):
        return self.q
    def getp(self):
        return self.p