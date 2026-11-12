import pandas as pd
import plotly.express as px

dontok_adatai = pd.read_csv("UCL_Finals_1955-2023.csv")

egyedi_dontok = dontok_adatai.drop_duplicates(subset=["Season"], keep="last")

klub_gyozelmek = egyedi_dontok["Winners"].value_counts().reset_index()
klub_gyozelmek.columns = ["Csapat", "Győzelmek_száma"]

top10_klub = klub_gyozelmek.head(10)

diagram4 = px.bar(
    top10_klub,
    x="Csapat",
    y="Győzelmek_száma",
    title="<b>4. Feladat: A legsikeresebb BL/BEK klubok (trófeák száma)</b>",
    color="Győzelmek_száma",
    color_continuous_scale="Sunset",
)

diagram4.show()