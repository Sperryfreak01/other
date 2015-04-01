import pandas as pd

columns = "G:J"
data = pd.read_excel('C:/Users/friedhop/AppData/Local/Continuum/Anaconda3/envs/trypandas/src/inventory.xlsx', sheet_name = 'Sheet2', header = 0, na_values = ['NA'], parse_cols = columns)

# Filtering
x = data[data["Proj Id"]=="J008"]

y = data[data["Part No"].map(lambda x: x.startswith("E001010"))].head()

z = data[data["Part No"].map(lambda x: x.startswith("E001010")) & (data["Proj Id"]=="J007")]