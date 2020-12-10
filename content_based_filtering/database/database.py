"""Database class."""

import os

from .items import Items
from .users import Users
from ..settings import settings


class Database():
    """Database.

    Contains all the Users and Items, alongside useful methods to manipulate them.
    """"

    def __init__(
        self,
        users_csv: str = os.path.join(settings.DATA_FOLDER, "users.csv"),
        items: str = os.path.join(settings.DATA_FOLDER, "movies.csv")
    ) -> None:
        """Init."""

        self.users = Users(users_csv)
        self.items = Items(items_csv)

    def
