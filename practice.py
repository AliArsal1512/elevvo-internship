# a = "hello world !"

# aa = a.split("o")
# print (aa)

import numpy as np
# print (np.__version__)

arr = np.arange(10)

# print (arr)

bool_arr = np.ones(10, dtype=bool)

# print (bool_arr)

selective_arr = arr[arr>4]

# print (selective_arr)

arr[arr>4]  = 2
# print (arr)

arr = np.arange(10)
arr[arr%2 == 1] = -1
# print(arr)

arr = np.arange(10)
arr = arr.reshape(5, -1)
# print(arr)

a = np.arange(10).reshape(2,-1)
b = np.arange(0,20,2).reshape(2,-1)

# print (np.vstack([a,b]))
print(a)
print(b)
print(np.where(a == b))
