import pandas as pd
pd.set_option('display.mpl_style', 'default')

path = 'C:/Users/friedhop/Desktop/other_scripts/inventory.xlsx'
columns1 = "G:J,K,L,AQ,AV"
raw1 = pd.read_excel(path, sheetname = 'Sheet 2', header = 0, na_values = ['NA'], parse_cols = columns1)
columns2 = "C:D,L"
raw2 = pd.read_excel(path, sheetname = 'Sheet 3', header = 0, na_values = ['NA'], parse_cols = columns2)

# Filtering
"""
raw[raw["Proj Id"]=="J008"]

raw[raw["Part No"].map(lambda x: x.startswith("E001010"))]

raw[raw["Part No"].map(lambda x: x.startswith("E001010")) & (raw["Proj Id"]=="J007")]

"""

# Row & Colum selection
"""
Select rows with:
raw[:3] or raw[1:7]

Select colums with their name, then select specific rows:
raw[['Proj Id', 'Part No']][:5]
"""