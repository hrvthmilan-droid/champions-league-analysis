import pandas as pd
import plotly.express as px

fajlnev = "UCL_AllTime_Performance_Table.csv"
adatok = pd.read_csv(fajlnev)

rendezett_adatok = adatok.sort_values(by="Pt.", ascending=False)

top10_csapat = rendezett_adatok.head(10)

diagram2 = px.bar(
    top10_csapat,
    x="Team",
    y="Pt.",
    title="<b>2. Feladat: Top 10 klub összesített BL-pontszám alapján</b>",
    color="Pt.",
    color_continuous_scale="Sunset",
)

diagram2.show()