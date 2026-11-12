import pandas as pd
import plotly.express as px

dontok_adatai = pd.read_csv("UCL_Finals_1955-2023.csv")

gyoztesek = dontok_adatai["Winners"]
masodikak = dontok_adatai["Runners-up"]
minden_dontos = pd.concat([gyoztesek, masodikak])

dontok_szama = minden_dontos.value_counts().reset_index()
dontok_szama.columns = ["Csapat", "Döntők_száma"]

top10_dontos = dontok_szama.head(10)

diagram3 = px.bar(
    top10_dontos,
    x="Csapat",
    y="Döntők_száma",
    title="<b>4. Feladat: Top 10 klub a BL/BEK döntős szereplések száma alapján</b>",
    color="Döntők_száma",
    color_continuous_scale="Sunset",
)

diagram3.show()