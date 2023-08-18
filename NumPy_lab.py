import numpy as np

# Create a 3D array
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6]],
                   [[7, 8, 9],
                    [10, 11, 12]],
                   [[13, 14, 15],
                    [16, 17, 18]]])

# Split into two new arrays along the first axis
split_arrs = np.array_split(arr_3d, 2, axis=0)
print(split_arrs)
