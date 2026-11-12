import pandas as pd
import plotly.express as px

alltime_adatok = pd.read_csv("UCL_AllTime_Performance_Table.csv")

mindig_kikap = alltime_adatok[
    (alltime_adatok["W"] == 0) & 
    (alltime_adatok["D"] == 0) & 
    (alltime_adatok["M."] > 0)
]

top_remenytelen = mindig_kikap.sort_values(by="Dif", ascending=True).head(10)

diagram4 = px.bar(
    top_remenytelen,
    x="Team",
    y="Dif",
    title="<b>4. Feladat: Nyeretlen és pontnélküli csapatok a legrosszabb gólkülönbség alapján</b>",
    color="Dif",
    color_continuous_scale="Sunset",
    hover_data=["Dif"]
)

diagram4.show()