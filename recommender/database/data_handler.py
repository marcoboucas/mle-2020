"""Database class."""

import os
import logging
from time import time
from typing import Optional, List

import numpy as np

from .items import Items
from .users import Users
from .interactions import Interactions
from ..settings import settings


class Database():
    """Database.

    Contains all the Users and Items, alongside useful methods to manipulate them.
    """

    users: Users
    items: Items
    interactions: Optional[Interactions]

    items_similarity: Optional[np.ndarray]

    def __init__(
        self,
        users_path: str = os.path.join(settings.DATA_FOLDER, "users.csv"),
        items_path: str = os.path.join(settings.DATA_FOLDER, "movies.csv"),
        interactions_path: Optional[str] = None
    ) -> None:
        """Init."""

        self.users = Users(users_path)
        self.items = Items(items_path)
        if interactions_path is not None:
            self.interactions = Interactions(interactions_path)
        else:
            self.interactions = None

    def compute_similarity_items(self, similarity_function, items_features_columns: List[str]):
        """Compute the similarity between all the items."""
        t = time()
        self.items.compute_similarity(similarity_function, items)
        logging.info("Similarity computed ! (%s)", time() - t)


if __name__ == "__main__":
    db = Database()
