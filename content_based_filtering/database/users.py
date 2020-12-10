"""Users class."""

from typing import Dict, Union
import os
from dataclasses import dataclass


import pandas as pd

from .base import BaseDB
from ..settings import settings


@dataclass
class User:
    user_id: int
    gender: str
    age: int
    occupation: int
    zip_code: int


class Users(BaseDB):
    """Users Handler.

    Handle all the needed methods to manipulate the users."""

    def __init__(self, file_path: str) -> None:
        """Init."""
        super().__init__("users", file_path, settings.USER_COLUMNS)

    def get_user(self, user_id: int) -> User:
        """Get one user from the database."""
        user_search = self.data[self.data['user_id'] == user_id]
        if user_search.shape[0] == 0:
            raise ValueError("User not found, id: % s" % user_id)
        user_info = user_search.loc[0].to_dict()
        user = User(**user_info)
        return user


if __name__ == "__main__":
    db = Users(os.path.join(settings.DATA_FOLDER, "users.csv"))
    print(db.get_user(0))
