from sklearn.datasets import fetch_california_housing
import pandas as pd

# Load the California housing dataset
housing = fetch_california_housing(as_frame=True)

# Convert to pandas DataFrame
df = housing.frame

# Save to CSV
df.to_csv("california_house_prices.csv", index=False)

print("California housing dataset saved as 'california_house_prices.csv'")
