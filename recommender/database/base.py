"""Base class for a database."""

from typing import List
import os

import numpy as np
import pandas as pd


class BaseDB():
    """Base DB

    handle very general things on the database.
    """

    def __init__(self, db_name: str, file_path: str, needed_columns: List[str]):
        """Init."""
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found (%s): %s" % (db_name, file_path))

        # Load the data
        self.data = pd.read_csv(file_path)

        # Check if the data is correct
        for needed_column in needed_columns:
            if needed_column not in self.data.columns:
                raise KeyError(
                    'This column does not appear in the dataset (%s): %s' % (db_name, needed_column)
                )

    def get_features(self, features_names: List[str]) -> np.ndarray:
        """Retrieve the features."""
        return self.data[features_names].to_numpy()
