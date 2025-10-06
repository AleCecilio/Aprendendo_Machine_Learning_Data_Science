import numpy as np

'''
arr = np.arange(0, 11)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:5])
print(arr[5:])

arr[0:5] = 100
print(arr) 
'''

'''
arr = np.arange(0, 11)
slice_of_arr = arr[0:5]
print(slice_of_arr)
slice_of_arr[:] = 99
print(slice_of_arr)
print(arr) 

arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
'''

'''
arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)
print(arr_2d.shape)
print(arr_2d[0])
print(arr_2d[2])
print(arr_2d[1][1])
print(arr_2d[1,1])
print(arr_2d[:2])
print(arr_2d[:2,1:])
'''

'''
arr = np.arange(1,11)
print(arr > 4)

bool_arr = arr > 4
print(bool_arr) 

print(arr[bool_arr])
print(arr[arr>4])
'''
