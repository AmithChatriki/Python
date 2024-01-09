import numpy as np 
 
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float) 
y = np.array(([92], [86], [89]), dtype=float) 
X = X/np.amax(X) # max of array 
y = y/100 
 
def sigmoid (x): 
    return 1/(1 + np.exp(-x)) 
 
def derivatives_sigmoid(x): 
    return x * (1 - x) 
 
epoch=5000 
lr=0.1 
 
wh = np.random.uniform(size=(2,3))  
bh = np.random.uniform(size=(1,3)) 
wout = np.random.uniform(size=(3,1)) 
bout = np.random.uniform(size=(1,1)) 
 
for i in range(epoch): 
    # forward prop 
    hinp=np.dot(X,wh) + bh 
    hlayer_act = sigmoid(hinp) 
    outinp=np.dot(hlayer_act,wout) + bout 
    output = sigmoid(outinp) 
 
    hiddengrad = derivatives_sigmoid(hlayer_act) 
    outgrad = derivatives_sigmoid(output) 
     
    EO = y-output 
    d_output = EO* outgrad 
     
    EH = d_output.dot(wout.T) 
    d_hiddenlayer = EH * hiddengrad 
 
    wout += hlayer_act.T.dot(d_output) *lr 
    wh += X.T.dot(d_hiddenlayer) *lr 
 
print("Input: \n" + str(X))  
print("Actual Output: \n" + str(y)) 
print("Predicted Output: \n" ,output) 
