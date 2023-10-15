#!/home/juju/pythonvenvgridDE/bin python

# /home/juju/pythonvenvgridDE/bin/python ./src/preparation.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/preparation.py

import pandas as pd
import numpy as np
import os  


def prepare(year, geo, printfinal):

    print("Charge "+year+" " + geo)
    df = pd.read_csv("input/"+year+"_"+geo+".csv") #, nrows=10000)

    print("Supprime colonnes inutilisées")
    colSup = ["Idcar_1km", "Idcar_nat", "I_est_1km", "lcog_geo", "Groupe"] if year == "2017" else ["idcar_1km", "idcar_nat", "i_est_1km", "lcog_geo"] if year == "2019" else []
    df = df.drop(colsSup, axis=1)

    print("Renomme colonne id")
    colId = "Idcar_200m" if year == "2017" else "idcar_200m" if year == "2019" else ""
    df = df.rename(columns={colId: "id"})

    print("Change noms colonnes en lettres minuscules")
    df.columns = df.columns.str.lower()

    print("Classe colonnes par ordre alphabétique")
    df = df.reindex(sorted(df.columns), axis=1)

    if(printfinal): print(df)

    print("Sauvegarde")
    if not os.path.exists('tmp'): os.makedirs('tmp')
    df.to_csv("tmp/"+year+"_"+geo+".csv", index=False)

    print("Fait - "+year+" " + geo)



prepare("2017", "reun", False)
prepare("2017", "mart", False)
prepare("2017", "met", False)
prepare("2019", "reun", False)
prepare("2019", "mart", False)
prepare("2019", "met", False)


