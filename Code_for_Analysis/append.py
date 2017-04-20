import pandas as pd

values = ["%.2d" %i for i in range(49)]

edges = pd.read_csv("empty.csv")

for i in range (49):
    df = pd.read_csv("part-000"+values[i])
    edges = edges.append(df, ignore_index=True)
    #pd.merge(df,  edges, how='outer')

edges.to_csv("edges.csv", index=False)
print ("done")
    