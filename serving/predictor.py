import joblib
from feast import FeatureStore
import pandas as pd

class Predictor:
    def __init__(self):
        self.model = joblib.load("/artifacts/model.joblib")
        self.store = FeatureStore(repo_path="/feature_repo")

    def predict(self, transaction_ids):
        features = self.store.get_online_features(
            features=["transaction_features:amount", "transaction_features:distance_from_home",
                      "transaction_features:ratio_to_median", "transaction_features:used_chip",
                      "transaction_features:online_order"],
            entity_rows=[{"transaction_id": tid} for tid in transaction_ids]
        ).to_df()
        X = features.drop(columns=["transaction_id"])
        return self.model.predict_proba(X)[:, 1].tolist()