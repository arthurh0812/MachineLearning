import numpy as np

a = np.array([1, 3, 5])
b = np.array([1, 4, 9])

print(a*b)
print(a+3)
print(b-a)

c = np.array([[9.0, 8.0, 9.0], [3.5, 6.0, 5.5], [7.0, 4.5, 9.0]])
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)
print(c.itemsize)
print(c.size)
print(c.nbytes)

full = np.full(shape=(4, 2), fill_value=99, dtype='int32')
print(full)

d = np.array([[1, 3, 5]])

print(np.repeat(d, 3, axis=1))
print(d+1)

matrix1 = np.full(shape=(3, 2), fill_value=2)
matrix2 = np.ones(shape=(2, 3))
print(matrix1)
print(matrix2)

print(np.reshape(matrix2, newshape=(3, 2)))

file = np.genfromtxt("test.data", delimiter=',')
file.astype('int32')

matrix, _ = np.meshgrid(file, file)
print(matrix)

mulMatrix = np.matmul(matrix, matrix)
print(mulMatrix)

determinant = np.linalg.det(matrix)
print(determinant)

min = np.min(matrix)
print(min)

print(matrix[[2, 4, 8]])

greaterThan30 = matrix[matrix > 30]
print(greaterThan30)
print(matrix < 30)

# Law of Large Numbers
test_sizes = [10, 100, 1000, 10000, 100000]

for size in test_sizes:
    random_data = np.random.normal(loc=50, scale=100, size=(size,))
    avg = np.sum(random_data) / random_data.size
    print(f"size {size}: avg = {avg}")
