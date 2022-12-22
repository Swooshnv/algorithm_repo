import numpy as np

def knapSack(v, w, k, W):
    cnt = len(w)
    for i in range(cnt):
        for j in range(W - 1):
            if i==0 or j==0:
                k[i][j] = 0
            elif j < w[i]:
                k[i][j] = k[i - 1][j]
            else:
                if k[i - 1][j] > k[i - 1][j - w[i]] + v[i]:
                    k[i][j] = k[i - 1][j]
                else:
                    k[i][j] = k[i - 1][j - w[i]] + v[i]
    for i in range(cnt):
        for j in range(W - 1):
            print(f"  {int(k[i][j])}", end = "")
        print("\n")

counts = 0
value = np.array([0], dtype = np.int32)
weight = np.array([0], dtype = np.int32)
print(weight.shape)
while(True):    
    try:    
        print(value, weight)
        value = np.insert(value, [1], [int(input(f"Press enter with no input for next step\n<value> of item No.{counts + 1}: "))])
        weight = np.insert(weight, [1], [int(input(f"<weight> of item No.{counts + 1}: "))])
        counts += 1
        print(value, weight)
    except:
        value = np.delete(value, np.s_[0])
        weight = np.delete(weight, np.s_[0])
        print(value, weight)
        W = int(input("Enter sack limit: "))
        break
print(f"Item Count: {counts}, values: {value}, weight: {weight}")
k = np.ndarray(shape = (counts, W))
knapSack(value, weight, k, W)