import pandas as pd
import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/series_temporelles.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/series_temporelles.py


# Charge fichier par année et extrait les données pour la séries temporelle
def extraction(year, geo, printfinal=False):
    print("charge " + year + " " + geo)
    d = pd.read_csv("./tmp/" + year + "_" + geo + ".csv")
    d = d[["id", "ind", "imputed"]]
    d = d.rename(columns={"ind": "ind" + year, "imputed": "imp" + year})
    if printfinal:
        print(d)
    return d


# construction des séries temporelles par jointure des données annuelles
def jointure(geo, printfinal=False):
    d = extraction("2015", geo)
    d = pd.merge(d, extraction("2017", geo), on="id", how="outer")
    d = pd.merge(d, extraction("2019", geo), on="id", how="outer")
    if printfinal:
        print(d)
    return d








# Préparation des données des séries temporelles, par région
for geo in ["reun", "mart", "met"]:
    print("*** Jointure " + geo)
    d = jointure(geo)
    # Sauvegarde
    d.to_csv("./tmp/ts_pop_" + geo + ".csv", index=False)








# Tuilage, via gridtiler
for geo in ["reun", "mart", "met"]:
    theme = "ts_pop"
    t = 128
    rounding = 2

    # défini les paramètres du tuilage en fonction du territoire géographique
    if geo == "met":
        crs = "3035"
        x = 3200000
        y = 2000000
    elif geo == "reun":
        crs = "2975"
        x = 300000
        y = 7600000
    elif geo == "mart":
        crs = "5490"
        x = 600000
        y = 1500000

    for a in [1, 2, 3, 5, 10, 25, 50, 100, 250, 500]:
        print("*** " + geo + " " + str(a * 200) + "m")

        subprocess.run(
            [
                "gridtiler",
                "-i",
                "./tmp/" + theme + "_" + geo + ".csv",
                "-r",
                "200",
                "-c",
                crs,
                "-x",
                str(x),
                "-y",
                str(y),
                "-p",
                "const a = c.id.split('N')[1].split('E'); return { x:a[1],y:a[0] };",
                "-m",
                "delete c.id",
                "-a",
                str(a),
                "-o",
                "./out/csv/" + geo + "/" + theme + "/" + str(a * 200) + "m/",
                "-t",
                str(t),
                "-R",
                str(rounding),
                "-e",
                "csv",
            ]
        )
