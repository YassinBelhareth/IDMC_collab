import numpy as np
import pandas as pd

df = pd.read_csv('dataset.csv',sep=';')

df = df.replace("?", np.nan)
df.to_csv('cleaned_dataset.csv',index=False)
