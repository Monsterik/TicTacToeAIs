import numpy as np

memory_size = 20
n_features = 9

np.set_printoptions(threshold=np.inf)

memory = np.zeros((memory_size, n_features * 2 + 2))

print(memory)