import numpy as np
my_list = [1, 2, 3, 4, 5, 6]
my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(np.array(my_list))                # make my_list list to 1d array
# print(np.array(my_mat))                 # make my_mat list to 2d array
# print(np.arange(0, 10))                 # print 0 - 9
# print(np.arange(0, 11, 2))              # print 0- 11 but interval is 2
# print(np.zeros(3))                      # three time zero matrix
# print(np.zeros((5, 5)))                 # 5 * 5 matrix with 0
# print(np.ones(4))                       # 4 time 1 matrix
# print(np.ones((3, 4)))                  # 3 * 4 matrix with 1
# print(np.linspace(0, 5, 10))            # 0 to 5 range with 10 time value
# print(np.eye(4))                        # diagonal matrix
# print(np.random.rand(5))                # random 5 time 0.somthing
# print(np.random.rand(5, 5))             # 5 * 5 time random
# print(np.random.randint(0, 50, 10))     # random between 0-50 10 values

arr = np.arange(1, 10)
# print(arr)
arr[2:6]
print(arr)
arr[2:6] = 10
print(arr)


# arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# print(arr_2d)
# print(arr_2d[0][0])
# print(arr_2d[0])
# print(arr_2d[:2, 1:])
# print(arr_2d[:2])


# my_list = [1, 2, 3, 4, 5, 6]
# my_list = np.array(my_list)
# my_list_1 = my_list[my_list > 2]
# print(my_list_1)


my_list = [1, 2, 3, 4, 5, 6]
my_list = np.array(my_list)
# print(my_list + my_list)
# print(my_list + 100)
# print(my_list * my_list)
# print(1 / my_list)
# print(my_list / my_list)
print(np.max(my_list))
print(np.sqrt(my_list))
print(np.exp(my_list))
