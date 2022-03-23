import pandas as pd

data = pd.read_csv("data.tsv", sep="\t")
# print(data)
for note in data["note"]:
  print(note)










