"""Items class."""

from typing import Dict, Any, List
import os
import logging
from dataclasses import dataclass
import numpy as np

from .base import BaseDB
from ..settings import settings


@dataclass
class Item(BaseDB):
    """Item Schema."""
    item_id: int
    name: str
    extra_features: Dict[str, Any]


class Items(BaseDB):
    """Items Handler.

    Handle all the needed methods to manipulate the items."""

    items_similarity: np.ndarray

    def __init__(self, file_path: str) -> None:
        """Init."""
        super().__init__("items", file_path, settings.ITEM_COLUMNS)

    def get_item(self, item_id: int) -> Item:
        """Get one user from the database."""
        item_search = self.data[self.data['item_id'] == item_id]
        if item_search.shape[0] == 0:
            raise ValueError("Item not found, id: % s" % item_id)
        item_info_all = item_search.reset_index().loc[0].to_dict()
        return self.convert_item(item_info_all)

    def convert_item(self, raw_item: Dict[str, Any]) -> Item:
        """Convert an item to the right dataformat."""
        # Put extra features into separate values
        item_info = {}
        extra_features = {}
        for key, value in raw_item.items():
            if key in settings.ITEM_COLUMNS:
                item_info[key] = value
            else:
                extra_features[key] = value

        return Item(**{  # type: ignore
            **item_info,
            "extra_features": extra_features
        })

    def compute_similarity(self, similarity_function, items_features_columns: List[str]):
        """Compute the similarity."""
        items_features = self.get_features(items_features_columns)
        # Compute the similarity
        self.items_similarity = similarity_function(items_features)

    def get_most_similar(self, item_id: int, n: int = 5):
        """Get the most similar items."""
        # Check if similarity computed
        if self.items_similarity is None:
            logging.warning("Similarity not computed !")
            return None

        # Get item id in the array
        try:
            item_array_id = self.data[self.data['item_id'] == item_id].index.tolist()[0]
        except IndexError:
            logging.warning('Please take id in the list %s', item_id)
            return None

        # Get all the similarity
        similarities = self.items_similarity[item_array_id]
        similarities_indexes = similarities.argsort()[::-1][:n]

        # Get the raw items
        raw_items = self.data.loc[similarities_indexes]

        return list(map(
            self.convert_item, raw_items.to_dict('records')))


if __name__ == "__main__":
    from ..similarity.items import default_item_score
    db = Items(os.path.join(settings.DATA_FOLDER, "movies.csv"))
    print(db.get_item(0))
    db.compute_similarity(
        similarity_function=default_item_score,
        items_features_columns=settings.ITEM_FEATURES
    )
    db.get_most_similar(1, n=10)
