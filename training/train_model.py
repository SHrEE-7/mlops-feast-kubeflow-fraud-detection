import pandas as pd
from feast import FeatureStore
import xgboost as xgb
import joblib

store = FeatureStore(repo_path="/feature_repo")

features = ["transaction_features:amount", "transaction_features:distance_from_home",
            "transaction_features:ratio_to_median", "transaction_features:used_chip",
            "transaction_features:online_order"]

entity_df = pd.read_parquet("/feature_repo/data/transactions.parquet")[["transaction_id", "event_timestamp"]]

training_df = store.get_historical_features(
    entity_df=entity_df,
    features=features + ["transaction_features:fraud"]
).to_df()

X = training_df[features]
y = training_df["transaction_features__fraud"]

model = xgb.XGBClassifier()
model.fit(X, y)

joblib.dump(model, "/artifacts/model.joblib")
print("Model trained and saved!")