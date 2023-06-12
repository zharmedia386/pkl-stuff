import pandas as pd

EKSPOR_FILE = "../ekspor.csv"

ekspor_df = pd.read_csv(EKSPOR_FILE)

sum_of_value_usd = int(ekspor_df["value usd"].sum())

sum_of_value_usd = "{:,}".format(sum_of_value_usd)

sum_of_value_usd = f'${sum_of_value_usd}'