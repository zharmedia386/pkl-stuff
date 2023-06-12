import pandas as pd
import plotly.express as px

DATA_PRODUKSI_KAYU_OLAHAN = "../produksi_kayu_olahan.csv"

### Read Data
produksi_kayu_olahan_df = pd.read_csv(DATA_PRODUKSI_KAYU_OLAHAN)

### Data Cleaning
# Filter only 'tahun', 'bulan', 'jenis', 'value usd' columns
new_df = produksi_kayu_olahan_df.copy()

# Change 'bulan' to its corresponding month number
new_df["bulan"] = new_df["bulan"].replace(
    [
        "Januari",
        "Februari",
        "Maret",
        "April",
        "Mei",
        "Juni",
        "Juli",
        "Agustus",
        "September",
        "Oktober",
        "November",
        "Desember",
    ],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
)

# Combine 'bulan' and 'tahun' columns
new_df["waktu"] = new_df["bulan"].astype(str) + "-" + new_df["tahun"].astype(str)

# Format 'waktu' column to datetime, but don't include the day
new_df["waktu"] = pd.to_datetime(new_df["waktu"], format="%m-%Y")

# Drop 'bulan' and 'tahun' columns
new_df = new_df.drop(["bulan", "tahun"], axis=1)

# Change 'jenis' column to category
new_df["jenis"] = new_df["jenis"].astype("category")

# Sort 'waktu' column
new_df = new_df.sort_values(by="waktu")

# Remove row where volume is 0
new_df = new_df[new_df["volume"] != 0]

"""
DATA VISUALIZATION

Tujuan  : Mendapatkan informasi jumlah produksi kayu olahan per produk dari tahun 2018 sampai dengan 2023
Catatan :
    1. Data yang digunakan adalah data produksi kayu olahan dari tahun 2018 sampai dengan 2023
"""
fig = px.line(
    new_df.filter(["jenis", "volume", "waktu"])
    .groupby(["jenis", "waktu"])
    .sum()
    .reset_index(),
    x="waktu",
    y="volume",
    color="jenis",
    title="Produksi Kayu Olahan Indonesia",
    labels={"waktu": "Waktu", "volume": "Volume (m3)"},
    height=600,
    markers=True,
)
