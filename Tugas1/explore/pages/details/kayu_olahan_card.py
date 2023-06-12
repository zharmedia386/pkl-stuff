import pandas as pd

KAYU_OLAHAN = "../produksi_kayu_olahan.csv"

produksi_kayu_olahan_df = pd.read_csv(KAYU_OLAHAN)

sum_of_volume = int(produksi_kayu_olahan_df["volume"].sum())

sum_of_volume = "{:,}".format(sum_of_volume)

sum_of_volume = f'{sum_of_volume} m\u00b3'