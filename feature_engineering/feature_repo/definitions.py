from datetime import timedelta
from feast import Entity, FeatureView, Field, FileSource
from feast.types import Float64, Int64, String

transaction = Entity(name="transaction_id", join_keys=["transaction_id"])

transaction_source = FileSource(
    path="data/transactions.parquet",
    timestamp_field="event_timestamp",
)

transaction_fv = FeatureView(
    name="transaction_features",
    entities=[transaction],
    ttl=timedelta(days=365),
    schema=[
        Field(name="user_id", dtype=String),
        Field(name="amount", dtype=Float64),
        Field(name="distance_from_home", dtype=Float64),
        Field(name="ratio_to_median", dtype=Float64),
        Field(name="used_chip", dtype=Int64),
        Field(name="online_order", dtype=Int64),
        Field(name="fraud", dtype=Int64),
    ],
    source=transaction_source,
)