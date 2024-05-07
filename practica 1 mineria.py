
import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns))

df = pd.read_csv("C:/Users/ricar/OneDrive/Documentos/Mineria/dataset/climate_change_data.csv")
print_tabulate(df)