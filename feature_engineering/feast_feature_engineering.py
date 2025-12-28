from feast import FeatureStore
from datetime import datetime, timedelta

store = FeatureStore(repo_path="feature_repo")

store.apply()  # Registers entities and views

# Materialize to online store (file-based for local)
end = datetime.now()
start = end - timedelta(days=365)
store.materialize(start, end)

print("Features materialized!")