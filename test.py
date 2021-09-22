import numpy as np
a=np.array([1,2,3])
print(a)
with open('output.txt', 'w') as f:
    print(a, file=f)