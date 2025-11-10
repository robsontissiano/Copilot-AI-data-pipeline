from faker import Faker
import pandas as pd

fake = Faker()
data = [
    {
        "customerID": i,
        "Name": fake.name(),
        "Email": fake.email(),
        "City": fake.city(),
        "Spend": fake.random_int(50, 1000),
        "Interactions": fake.random_init(1, 20)
    }
    for i in range(1000)
]

df = pd.DataFrame(data)
df.to_csv("01_data_generation/sample_datasets/synthetic_customers.csv", index=False)
print("Synthetic dataset created.")
