import numpy as np


class PCA():
    def __init__(self, num_components):
        self.num_components = num_components

    def get_components(self, data):
        centered_data = data - np.mean(data, axis=0)

        covariance_matrix = self.get_covariance_matrix(centered_data)

        eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

        sorted_indices = np.argsort(eigen_values)[::-1]

        sorted_eigen_vectors = eigen_vectors[:, sorted_indices]

        final_eigen_vectors = np.array(sorted_eigen_vectors[:, 0:self.num_components])

        reduced_data = centered_data @ final_eigen_vectors

        return reduced_data

    def get_covariance_matrix(self, data):

        N, M = data.shape

        cov = np.zeros((M, M))

        for i in range(M):
            i_mean = np.sum(data[:, i]) / N
            centered_i = data[:, i] - i_mean
            for j in range(M):
                j_mean = np.sum(data[:, j]) / N
                centered_j = data[:, j] - j_mean

                cov[i, j] = np.sum(centered_i * centered_j) / (N - 1)

        return cov

    def get_largest_eigen_vector(self, data, num_simulations=1000):
        # Ideally choose a random vector
        # To decrease the chance that our vector
        # Is orthogonal to the eigenvector
        v1 = np.random.rand(data.shape[1])

        for _ in range(num_simulations):
            # calculate the matrix-by-vector product Ab
            v1_prod = np.dot(data, v1)

            # calculate the norm
            v1_prod_norm = np.linalg.norm(v1_prod)

            # re normalize the vector
            v1 = v1_prod / v1_prod_norm

        return v1

    def get_eigen_value(self, data, eigen_vector):
        return (eigen_vector.T @ (data @ eigen_vector)) / eigen_vector.T @ eigen_vector

    def get_eigen_values_and_vectors(self, data):

        eigen_vectors = []
        eigen_values = []

        matrix = data.copy()

        for i in range(self.num_components):
            eigen_vectors.append(self.get_largest_eigen_vector(matrix))
            eigen_values.append(self.get_eigen_value(matrix, eigen_vectors[i]))

            matrix = matrix - (eigen_values[i] * ((eigen_vectors[i] @ eigen_vectors[i].T) / np.abs(eigen_vectors[i])**2))

        return eigen_values, eigen_vectors
