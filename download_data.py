from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing(as_frame=True)
df = data.frame
df.to_csv('data/raw/boston_housing.csv', index=False)

print("✔ California housing dataset saved as boston_housing.csv")
