# UEFA Bajnokok Ligája (UCL) – Adatvizualizációs Projekt

Ez a projekt az UEFA Bajnokok Ligája (és elődje, a BEK) történelmi teljesítményeit és döntőit elemzi, illetve vizualizálja Python és Plotly Express segítségével.

## Felhasznált adatforrások
* `UCL_AllTime_Performance_Table.csv`: Örökranglista és összesített csapatstatisztikák (`Team`, `M.`, `W`, `D`, `L`, `Dif`, `Pt.`).
* `UCL_Finals_1955-2023.csv`: A döntők eredményei és adatai 1955-től 2023-ig.

## Vizualizációk (Feladatok)
1. **Győzelmek országonként:** Az egyes nemzetek klubjainak összesített BL/BEK-győzelmei.
2. **Top 10 klub az örökranglistán:** A legtöbb összesített pontot (`Pt.`) gyűjtő csapatok rangsora.
3. **Top 10 döntős klub:** A legtöbb fináléba jutott együttesek (az 1974-es megismételt döntő duplikációjának kiszűrésével).
4. **Nyeretlen csapatok gólkülönbsége:** Azon együttesek listája, amelyek minden lejátszott mérkőzésüket elveszítették (`W == 0` és `D == 0`), a legrosszabb gólkülönbség (`Dif`) alapján sorba rendezve.
5. **A legsikeresebb klubok:** A sorozat legtöbb trófeáját elhódító csapatok összefoglalója.

## Követelmények és futtatás
A szkriptek futtatásához Python 3, valamint a `pandas` és `plotly` könyvtárak telepítése szükséges:

```bash
pip install pandas plotly
