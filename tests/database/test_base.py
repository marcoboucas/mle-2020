"""Test the base Database."""
import os
from unittest import TestCase

from recommender.settings import settings
from recommender.database.base import BaseDB

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


class TestBaseDB(TestCase):
    """Test the baseDB."""

    def test_loading(self):
        """Test the loading."""
        # Test not exists
        file_path = os.path.join(CURRENT_FOLDER, "notExistingFile.csv")
        self.assertRaises(
            FileNotFoundError, BaseDB,
            "test", file_path, []
        )

        # Test columns
        file_path = os.path.join(settings.DATA_FOLDER, "movies.csv")
        self.assertRaises(
            KeyError, BaseDB,
            "test", file_path, ["sdljgsd"]
        )
