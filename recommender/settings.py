"""Settings file."""

import os


# pylint: disable=invalid-name,too-few-public-methods
class settings:
    """All the needed constants for the model."""

    PACKAGE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(PACKAGE_FOLDER, "..", "data")

    # User DB
    USER_COLUMNS = ["user_id", "gender", "age", "occupation", "zip_code"]

    # Item DB
    ITEM_COLUMNS = ['item_id', 'name']
    ITEM_FEATURES = [
        'Animation', "Children's", 'Comedy', 'Adventure',
        'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
        'Thriller', 'Horror', 'Sci-Fi', 'Documentary', 'War',
        'Musical', 'Mystery', 'Film-Noir', 'Western'
    ]

    # Interaction DB
    INTERACTION_COLUMNS = ['user_id', 'item_id', 'score']
