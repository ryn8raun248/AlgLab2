
import numpy as np
from pca import PCA
import sklearn
from sklearn.decomposition import PCA as sk_PCA


def main():
    num_components = 2

    data = np.random.random((4,4))

    p = PCA(num_components)

    pca2 = sk_PCA(n_components=num_components).fit(data)

    control = pca2.fit_transform(data)

    x = p.get_components(data)

    print(x)
    print(control)
    print()

if __name__ == "__main__":
    main()
