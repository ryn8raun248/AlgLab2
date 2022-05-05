import numpy as np
from pca import PCA
from sklearn.decomposition import PCA as sklearn_PCA


def main():
    num_components = 2
    data = np.random.random((4, 4))

    pca = PCA(num_components)
    pca.fit(data)
    transformed_data = pca.transform()

    sk_transformed_data = sklearn_PCA(n_components=num_components).fit_transform(data)

    print(transformed_data)
    print(sk_transformed_data)


if __name__ == "__main__":
    main()
