import numpy as np

inputs = open("inputs.txt")

coords = np.array([list(map(int, line[:-1].split(','))) for line in inputs.readlines()])
# x
x = coords[:,0].copy()
squared = x**2
x.resize(1,x.shape[0])
matrix = np.matmul(x.T, x)
dists = (np.sqrt(squared.reshape(-1, 1) - 2*matrix + squared) + np.ones((x.shape[0]))).astype(np.int64)
# y
y = coords[:,1].copy()
y_squared = y**2
y.resize(1,y.shape[0])
y_matrix = np.matmul(y.T, y)
dists *= (np.sqrt(y_squared.reshape(-1, 1) - 2*y_matrix + y_squared) + np.ones((y.shape[0]))).astype(np.int64)

print(np.max(dists))

inputs.close()