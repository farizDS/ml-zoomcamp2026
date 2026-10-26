import numpy as np
from scipy import sparse

def convert_indices_to_int32(X):
    X = X.copy()

    if sparse.issparse(X):
        X.indices = X.indices.astype(np.int32)
        X.indptr = X.indptr.astype(np.int32)

    return X