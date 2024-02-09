import pandas as pd

df = pd.read_csv("data/unigram_freq.csv", usecols=["word"])
df = df.head(5000)
df = df[df['word'].str.len() > 2]
df.to_csv("data/data_preprocessed.csv", index=False)
# further preprocessing is in Google Sheets, using GOOGLETRANSLATE built-in function
