"""Items class."""

from typing import Dict, Union, Any
import os
from dataclasses import dataclass

import pandas as pd

from .base import BaseDB
from ..settings import settings


@dataclass
class Item(BaseDB):
    item_id: int
    name: str
    extra_features: Dict[str, Any]


class Items(BaseDB):
    """Items Handler.

    Handle all the needed methods to manipulate the items."""

    def __init__(self, file_path: str) -> None:
        """Init."""
        super().__init__("items", file_path, settings.ITEM_COLUMNS)

    def get_item(self, item_id: int) -> Item:
        """Get one user from the database."""
        item_search = self.data[self.data['item_id'] == item_id]
        if item_search.shape[0] == 0:
            raise ValueError("Item not found, id: % s" % item_id)
        item_info_all = item_search.loc[0].to_dict()

        # Put extra features into separate values
        item_info = {}
        extra_features = {}
        for key, value in item_info_all.items():
            if key in settings.ITEM_COLUMNS:
                item_info[key] = value
            else:
                extra_features[key] = value

        return Item(**{
            **item_info,
            "extra_features": extra_features
        })


if __name__ == "__main__":
    db = Items(os.path.join(settings.DATA_FOLDER, "movies.csv"))
    print(db.get_item(0))
