"""Pipeline for recommender system."""

from typing import List, Dict, Union
import pandas as pd


from .database import Database
from .database.items import Item


class Pipeline:
    """Pipeline for recommender system."""

    def __init__(
        self,
        database: Database
    ):
        """Init."""
        self.database = database

    def train_model(
        self,
        similarity_items,
        items_features_columns: List[str]
    ):
        """Train the model.

        Args:
            similarity_items: Function that takes the matrix of items features and return the similarity matrix
        """
        # Compute the similarity between different items
        self.database.compute_similarity_items(
            similarity_function=similarity_items,
            items_features_columns=items_features_columns
        )

    def recommend_one_user(self, user_id: int) -> List[Item]:
        """Recommend one user using our algorithm."""
        # Retrieve all the movies for this author
        already_seen_movies = self.database.interactions.get_user_interactions(user_id)
        return self.recommend_from_list(already_seen_movies)

    def recommend_from_list(self, item_list: List[int], n: int = 3) -> List[Item]:
        """Recommend from a list of items."""
        # Find the most similar
        to_see_movies = set()
        for movie in item_list:
            to_see_movies.update(
                list(map(
                    lambda x: x.item_id,
                    self.database.items.get_most_similar(movie, n)
                ))

            )
        return [
            x for x in to_see_movies
            if x not in item_list
        ]

    def evaluate_one_user(self, user_id, val_size: float = 0.2, n: int = 3) -> Dict[str, int]:
        """Evalute the results for one user."""
        # Get the movies already seen
        already_seen_movies = self.database.interactions.get_user_interactions(user_id)

        # Take a part of them
        index = int(len(already_seen_movies) * val_size)
        x_train = already_seen_movies[:index]
        x_val = set(already_seen_movies[index:])

        # Generate the prediction
        recommendations = set(self.recommend_from_list(x_train))

        results: Dict[str, int] = {}
        results['nbr_predicted'] = len(recommendations)
        results['nbr_train'] = len(x_train)
        results['correct'] = len([x for x in x_val if x in recommendations])
        return results

    def evaluate_all_results(self, nbr_items: int = -1, val_size: float = 0.2, n: int = 3) -> pd.DataFrame:
        """Evaluate all the users."""
        results = list(map(
            lambda x: self.evaluate_one_user(x, val_size, n),
            self.database.users.data['user_id'].tolist()[:nbr_items]
        ))
        return pd.DataFrame.from_records(results)
