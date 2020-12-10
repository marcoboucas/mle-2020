"""Interactions class."""


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


if __name__ == "__main__":
    db = Interactions(os.path.join(settings.DATA_FOLDER, "ratings.csv"))
