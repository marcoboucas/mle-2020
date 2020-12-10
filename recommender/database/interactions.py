"""Interactions class."""

from typing import List
import os
from dataclasses import dataclass

from .base import BaseDB
from ..settings import settings


@dataclass
class Interaction(BaseDB):
    """Interaction Schema."""
    user_id: int
    item_id: str
    score: float


class Interactions(BaseDB):
    """Interactions Handler.

    Handle all the needed methods to manipulate the interactions."""

    def __init__(self, file_path: str) -> None:
        """Init."""
        super().__init__("interactions", file_path, settings.INTERACTION_COLUMNS)

    def get_user_interactions(self, user_id: int) -> List[int]:
        """Find all the interactions of one user."""
        return self.data[self.data['user_id'] == user_id]['item_id'].tolist()


if __name__ == "__main__":
    db = Interactions(os.path.join(settings.DATA_FOLDER, "ratings.csv"))
    print(db.get_user_interactions(0))
