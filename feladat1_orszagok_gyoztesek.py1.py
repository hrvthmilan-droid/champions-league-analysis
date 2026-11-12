import pandas as pd
import plotly.express as px

dontok_adatai = pd.read_csv("UCL_Finals_1955-2023.csv")

gyoztesek = dontok_adatai["Country"].value_counts().reset_index()
gyoztesek.columns = ["Ország", "Győzelmek_száma"]

diagram1 = px.bar(
    gyoztesek,
    x="Ország",
    y="Győzelmek_száma",
    title="<b>1. Feladat: BL/BEK győztesek száma országonként</b>",
    color="Győzelmek_száma",
    color_continuous_scale="Sunset",
)

diagram1.show()