#%%
import numpy as np
import os

print("Numpy Version is ", np.__version__)

#%%
# Create an array from rain-fall.csv, keeping rainfall data in mm

array_rain_fall = np.loadtxt(fname="rain-fall.csv", delimiter=",")

print("NumPy array: \n", array_rain_fall)
print("Shape: ", array_rain_fall.shape)
print("Data Type: ", array_rain_fall.dtype.name)

#%%
# Check error when different column counts in rows

array_rain_fall_wrong = np.loadtxt(
    fname="rain-fall-wrong.csv", delimiter=","
)

#%%
# Skip first row and first column

array_rain_fall_named = np.loadtxt(
    fname="rain-fall-row-col-names.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
)
print("NumPy array: \n", array_rain_fall_named)
print("Shape: ", array_rain_fall_named.shape)
print("Data Type: ", array_rain_fall_named.dtype.name)

#%%
# Create array from gzipped csv

array_rain_fall_zip = np.loadtxt(
    fname="rain-fall-row-col-names.csv.gz",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
)
print("NumPy array: \n", array_rain_fall_zip)
print("Shape: ", array_rain_fall_zip.shape)
print("Data Type: ", array_rain_fall_zip.dtype.name)

#%%

# Create array from tsv files

array_rain_fall_tab = np.loadtxt(
    fname="rain-fall-row-col-names.tsv",
    delimiter="\t",
    skiprows=1,
    usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
)
print("NumPy array: \n", array_rain_fall_zip)
print("Shape: ", array_rain_fall_zip.shape)
print("Data Type: ", array_rain_fall_zip.dtype.name)