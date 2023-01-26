import pandas as pd


df1 = pd.read_csv("response.csv")
df2 = pd.read_csv("api.csv")


df = pd.concat([df1, df2])


df.replace("", float("NaN"), inplace=True)


df.dropna(inplace=True)


df.drop(columns=["Open Price", "High Price", "Low Price", "Close Price"], inplace=True)

df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d").dt.strftime("%Y-%m-%d")

df.to_csv("cleaned_data.csv", index=False)