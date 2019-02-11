#%%
import numpy as np

print("Numpy Version is ", np.__version__)

#%%
# Creating 1 dimensional numpy array with Python list (int type)
one_d_list = [1, 2, 3, 4, 5]
array_one_dim_list = np.array(one_d_list)
print("NumPy array: ", array_one_dim_list)
print("Shape: ", array_one_dim_list.shape)
print("Data Type: ", array_one_dim_list.dtype.name)

#%%

# Creating 2 dimensional numpy array with Python list (float type)
two_d_list = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
array_two_d_py_list = np.array(two_d_list)
print("NumPy array: \n", array_two_d_py_list)
print("Shape: ", array_two_d_py_list.shape)
print("Data Type: ", array_two_d_py_list.dtype.name)

#%%

# Creating 3 dimensional numpy array with Python 3d list (String)
three_d_list = [
    [["aa", "bb", "cc"], ["dd", "ee", "ff"], ["gg", "hh", "kk"]],
    [["ll", "mm", "nn"], ["oo", "pp", "qq"], ["rr", "ss", "tt"]],
]
three_d_array = np.array(three_d_list)
print("NumPy array: \n", three_d_array)
print("Shape: ", three_d_array.shape)
print("Data Type: ", three_d_array.dtype.name)

#%%
# Creating 3 dimensional numpy array with Python 3d list (String)
three_d_list = [
    [["aa", "bb", "cc"], ["dd", "ee", "ff"], ["gg", "hh", "kk"]],
    [["ll", "mm", "nn"], ["oo", "pp", "qq"], ["rr", "ss", "tt"]],
]
three_d_array = np.array(three_d_list)
print("NumPy array: \n", three_d_array)
print("Shape: ", three_d_array.shape)
print("Data Type: ", three_d_array.dtype.name)

#%%
# Creating NumPy array with Python list with mix data type elements
mix_data_type_list = [1.0, 2, 3.5, 4.75, 5.0]
mix_data_type_array = np.array(mix_data_type_list)
print("NumPy array: \n", mix_data_type_array)
print("Shape: ", mix_data_type_array.shape)
print("Data Type: ", mix_data_type_array.dtype.name)

#%%
# Creating NumPy array with Pythong list and specifying data type
fix_data_type_array = np.array(mix_data_type_list, np.int)
print("NumPy array: \n", fix_data_type_array)
print("Shape: ", fix_data_type_array.shape)
print("Data Type: ", fix_data_type_array.dtype.name)


#%%

# Creating NumPy array with mix of List and Tuples upgraded

a_list = [1, 2.5, 3]
a_tuple = (1.5, 2.3, 3)

two_d_list_tuple_array = np.array([a_list, a_tuple])
print("NumPy array: \n", two_d_list_tuple_array)
print("Shape: ", two_d_list_tuple_array.shape)
print("Data Type: ", two_d_list_tuple_array.dtype.name)

#%%

# Creating NumPy array with jagged 2 d Python list

jagged_two_d_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

jagged_two_d_array = np.array(jagged_two_d_list)
print("NumPy array: \n", jagged_two_d_array)
print("Shape: ", jagged_two_d_array.shape)
print("Data Type: ", jagged_two_d_array.dtype.name)

#%%
# Create NumPy array with Python List and enforce minimum dimension

# We are using an already create one dimensional array one_d_list
array_enforced_three_dim_list = np.array(object=two_d_list, ndmin=3)
print("NumPy array: ", array_enforced_three_dim_list)
print("Shape: ", array_enforced_three_dim_list.shape)
print("Data Type: ", array_enforced_three_dim_list.dtype.name)

#%%
# Use asarray to create NumPy array

one_dim_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
one_dim_array_use_asarray = np.asarray(one_dim_list)
print("NumPy array: \n", one_dim_array_use_asarray)
print("Shape: ", one_dim_array_use_asarray.shape)
print("Data Type: ", one_dim_array_use_asarray.dtype.name)

# For above operation NumPy copy as object used to create array is Python list

#%%
# array method by default make copy and hence change applied to copy
np.array(one_dim_array_use_asarray)[1]=1
print("NumPy array: \n", one_dim_array_use_asarray)

# asarray method don't make copy and hence change applied to one_dim_array_use_asarray
np.asarray(one_dim_array_use_asarray)[1]=1
print("NumPy array: \n", one_dim_array_use_asarray)


