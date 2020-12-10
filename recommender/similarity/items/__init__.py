"""Similarity between items.


All similarity functions take as input a matrix of shape (n,m) with :
- n: Number of items
- m: Number of features
"""

from .default import similarity_score as default_item_score
