import json
import pandas as pd

data = json.load(open("response.json"))
data["users"]

users = pd.json_normalize(data, "users")
companies = pd.json_normalize(data, "companies")

df = pd.concat([users, companies], keys=["users", "companies"],)
df.to_csv("res.csv")
