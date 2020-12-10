"""Users class."""

from typing import Dict, Union
import os
from dataclasses import dataclass

import pandas as pd

from ..settings import settings


@dataclass
class User:
    user_id: int
    gender: str
    age: int
    occupation: int
    zip_code: int


class Users:
    """Users Handler.

    Handle all the needed methods to manipulate the users."""

    def __init__(self, csv_path: str) -> None:
        """Init."""
        # Check if the file exists
        if not os.path.isfile(csv_path):
            raise FileNotFoundError("File not found (User DB): %s" % csv_path)

        # Load the data
        self.users = pd.read_csv(csv_path)

        # Check if the data is correct
        for needed_column in settings.USER_COLUMNS:
            if needed_column not in self.users.columns:
                raise KeyError(
                    'This column does not appear in the dataset' % needed_column
                )

    def get_user(self, user_id: int) -> User:
        """Get one user from the database."""
        user_search = self.users[self.users['user_id'] == user_id]
        if user_search.shape[0] == 0:
            raise ValueError("User not found, id: % s" % user_id)
        user_info = user_search.loc[0].to_dict()
        user = User(**user_info)
        return user


if __name__ == "__main__":
    db = Users(os.path.join(settings.DATA_FOLDER, "users.csv"))
    print(db.get_user(0))
