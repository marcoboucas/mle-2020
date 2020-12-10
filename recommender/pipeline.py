"""Pipeline for recommender system."""

from typing import List

from .database import Database


class Pipeline:
    """Pipeline for recommender system."""

    def __init__(
        self,
        database: Database
    ):
        """Init."""
        self.database = database

    def train_model(
        self,
        similarity_items,
        items_features_columns: List[str]
    ):
        """Train the model.

        Args:
            similarity_items: Function that takes the matrix of items features and return the similarity matrix
        """
        # Compute the similarity between different items
        self.database.compute_similarity_items(
            similarity_function=similarity_items,
            items_features_columns=items_features_columns
        )
