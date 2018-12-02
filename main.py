import pandas as pd 
import numpy as np

# Import data
data = pd.read_csv("asty.csv", sep=";", low_memory=False)

# print(data.shape) # 425,458 rows, 136 columns

# Columns
# for i in data.columns.values:
    # print(i)

for i in data.T5C.values:
    print(i)

# print(data.describe())