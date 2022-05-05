import numpy as np


class PCA():
    """
    Class that is responsible for conducting PCA on a matrix
    """
    def __init__(self, num_components):
        """
        Initializes the PCA class
        :param num_components: The number of components to extract from the matrix
        """
        self.num_components = num_components
        self.components = None
        self.centered_data = None

    def fit(self, data):
        """
        Method responsible for computing the principle components
        of the input matrix
        :param data: The matrix that will have its principle components
        determined
        """
        # Ensure there are less components than there are features
        assert self.num_components < data.shape[1]

        # Center the data
        self.centered_data = data - np.mean(data, axis=0)

        # Compute the covariance matrix
        covariance_matrix = self.get_covariance_matrix(self.centered_data)

        # Use numpy to calculate eigen values
        eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)

        # Sort by the largest eigen values
        sorted_indices = np.argsort(eigen_values)[::-1]

        sorted_eigen_vectors = eigen_vectors[:, sorted_indices]

        # Save only the top n components
        self.components = np.array(sorted_eigen_vectors[:, 0:self.num_components])

    def transform(self):
        """
        Method responsible for returning the reduced matrix according to
        the number of principle components
        :return: The reduced matrix
        """
        reduced_data = self.centered_data @ self.components

        return reduced_data

    def get_covariance_matrix(self, data):

        # Get height and width of the matrix
        N, M = data.shape

        # Create a square matrix with a side length equal to the
        # number of features
        cov = np.zeros((M, M))

        for i in range(M):
            # Compute the center of one of the features
            i_mean = np.sum(data[:, i]) / N
            centered_i = data[:, i] - i_mean
            for j in range(M):
                # Center a secondary feature
                j_mean = np.sum(data[:, j]) / N
                centered_j = data[:, j] - j_mean

                # Compute the covariance of those two features and
                # save it into the covariance matrix
                cov[i, j] = np.sum(centered_i * centered_j) / (N - 1)

        return cov
