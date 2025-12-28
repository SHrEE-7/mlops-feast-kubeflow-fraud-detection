import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
num_records = 10000

data = []
for _ in range(num_records):
    data.append({
        "transaction_id": fake.uuid4(),
        "user_id": fake.uuid4(),
        "amount": round(random.uniform(5.0, 5000.0), 2),
        "distance_from_home": round(random.uniform(0.0, 5000.0), 2),
        "ratio_to_median": round(random.uniform(0.1, 10.0), 2),
        "used_chip": random.randint(0, 1),
        "online_order": random.randint(0, 1),
        "fraud": random.choices([0, 1], weights=[0.95, 0.05])[0],
        "event_timestamp": datetime.now() - timedelta(days=random.randint(0, 365)),
    })

df = pd.DataFrame(data)
df.to_parquet("feature_engineering/feature_repo/data/transactions.parquet", index=False)
print("Synthetic data generated: feature_engineering/feature_repo/data/transactions.parquet")