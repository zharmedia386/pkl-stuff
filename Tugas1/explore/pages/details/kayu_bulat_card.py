import pandas as pd

KAYU_BULAT = "../produksi_kayu_bulat.csv"

produksi_kayu_bulat_df = pd.read_csv(KAYU_BULAT)

sum_of_volume = int(produksi_kayu_bulat_df["volume"].sum())

sum_of_volume = "{:,}".format(sum_of_volume)

sum_of_volume = f'{sum_of_volume} m\u00b3'
