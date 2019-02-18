#%%
import numpy as np
import os

print("Numpy Version is ", np.__version__)

#%%
# Saving NumPy array as a csv file
array_rain_fall = np.loadtxt(fname="rain-fall.csv", delimiter=",")
np.savetxt(fname="saved-rain-fall-row-col-names.csv", delimiter=",", X=array_rain_fall)

# Check generated csv file after loading it

array_rain_fall_csv_saved = np.loadtxt(
    fname="saved-rain-fall-row-col-names.csv", delimiter=","
)

print("NumPy array: \n", array_rain_fall_csv_saved)
print("Shape: ", array_rain_fall_csv_saved.shape)
print("Data Type: ", array_rain_fall_csv_saved.dtype.name)

# We can change our delimeter and save file in tsv or other text format

#%%

# Saving array as binary file and reading it

array_rain_fall.tofile("saved-rain-fall-binary")

array_rain_fall_binary = np.fromfile("saved-rain-fall-binary")

print("NumPy array: \n", array_rain_fall_binary)
print("Shape: ", array_rain_fall_binary.shape)
print("Data Type: ", array_rain_fall_binary.dtype.name)

#%%

# Saving array as .npy and reading it

np.save("saved-rain-fall-binary.npy", array_rain_fall)

array_rain_fall_npy = np.load("saved-rain-fall-binary.npy")

print("NumPy array: \n", array_rain_fall_npy)
print("Shape: ", array_rain_fall_npy.shape)
print("Data Type: ", array_rain_fall_npy.dtype.name)

#%%

# Saving multiple arrays in compressed npz format. Loading and reading the array.

np.savez("saved-rain-fall-binary.npz", array_rain_fall, np.array([1, 2, 3, 4, 5]))

array_rain_fall_npz = np.load("saved-rain-fall-binary.npz")

print("NumPy array 1: \n", array_rain_fall_npz["arr_0"])
print("Shape of Array 1: ", array_rain_fall_npz["arr_0"].shape)
print("Data Type of Array 1: ", array_rain_fall_npz["arr_0"].dtype.name)

print("NumPy array 2: \n", array_rain_fall_npz["arr_1"])
print("Shape of Array 2: ", array_rain_fall_npz["arr_1"].shape)
print("Data Type of Array 2: ", array_rain_fall_npz["arr_1"].dtype.name)
