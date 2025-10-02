import pandas as pd

df = pd.read_csv("./data/spotify_dataset.csv")

input_album = "sanam"
album_url = df.loc[df["Album"].str.lower().str.contains(input_album)]["Cover Image"].head(1).squeeze()
print(album_url)
print(len(album_url))

suggestion = df.loc[df["Album"].str.lower().str.contains(input_album)]["Album"].unique()
print(suggestion)


