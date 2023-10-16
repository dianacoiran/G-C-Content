import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("MyGC_genome.csv",sep="\t")
tabla = df[["Length","GC"]]
print(tabla)

temp_tsv = ("bac_GC.tsv")
tabla.to_csv(temp_tsv, sep='\t', index=False)
