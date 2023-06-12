import pandas as pd

BAHAN_BAKU = "../pemenuhan_bahan_baku.csv"

pemenuhan_bahan_baku_df = pd.read_csv(BAHAN_BAKU)

sum_of_value = int(pemenuhan_bahan_baku_df["value"].sum())

sum_of_value = "{:,}".format(sum_of_value)

sum_of_value = f'{sum_of_value} m\u00b3'

latest_month = pemenuhan_bahan_baku_df["tahun"]

latest_month = latest_month.sort_values(ascending=False)

latest_month = latest_year = latest_month.iloc[0]

latest_month = pemenuhan_bahan_baku_df.query(f'tahun == {latest_month}')

latest_month = latest_month.query('value > 0')

latest_month = latest_month.tail(1)

latest_month = latest_month["bulan"].loc[latest_month.index[0]]
