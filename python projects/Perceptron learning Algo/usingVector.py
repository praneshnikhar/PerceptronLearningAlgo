import numpy as np
def compute_output_vector(w, x):
    z = np.dot(w, x)
    return np.sign(z)
