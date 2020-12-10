"""Default similarity between items."""

import numpy as np


def similarity_score(items_matrix: np.ndarray):
    """Compute the basic similarity score between items."""
    return items_matrix @ items_matrix.T


if __name__ == "__main__":
    matrix = np.random.random((2, 2))
    print(matrix)
    print(similarity_score(matrix))
