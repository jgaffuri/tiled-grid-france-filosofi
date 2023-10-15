#!/home/juju/pythonvenvgridDE/bin python

# /home/juju/pythonvenvgridDE/bin/python ./src/preparation.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/preparation.py

import pandas as pd
import numpy as np
import os  




def prepare2017(geo, printfinal):

    print("Charge 2017 " + geo)
    df = pd.read_csv("input/2017_"+geo+".csv") #, nrows=10000)

    print("Supprime colonnes inutilisées")
    df = df.drop(["Idcar_1km", "Idcar_nat", "I_est_1km", "lcog_geo", "Groupe"], axis=1)

    print("Renomme colonne id")
    df = df.rename(columns={"Idcar_200m": "id"})

#en capitale
#ordonne les colonnes par ordre alphabetique

    if(printfinal): print(df)

    print("Sauvegarde")
    if not os.path.exists('tmp'): os.makedirs('tmp')
    df.to_csv("tmp/2017_"+geo+".csv", index=False)

    print("Fait - 2017 " + geo)


prepare2017("reun", True)


def prepare2019(geo, printfinal):

    print("Charge 2017 " + geo)
    df = pd.read_csv("input/2019_"+geo+".csv") #, nrows=10000)

    print("Supprime colonnes inutilisées")
    df = df.drop(["idcar_1km", "idcar_nat", "i_est_1km", "lcog_geo"], axis=1)

    print("Renomme colonne id")
    df = df.rename(columns={"idcar_200m": "id"})

    if(printfinal): print(df)

    print("Sauvegarde")
    if not os.path.exists('tmp'): os.makedirs('tmp')
    df.to_csv("tmp/2019_"+geo+".csv", index=False)

    print("Fait - 2019 " + geo)


#prepare2019("reun", False)
#prepare2019("mart", False)
#prepare2019("met", False)









def prepare(csvfile, sep, code, printfinal):
    print(code)

    print("Load data")
    df = pd.read_csv(csvfile, sep=sep, encoding="iso-8859-1") #, nrows=10000)

    print("drop unecessary rows")
    df = df[df.Merkmal == code]

    print("drop unecessary columns")
    df = df.drop(["Gitter_ID_100m_neu", "Auspraegung_Text", "Anzahl_q", "Merkmal"], axis=1)

    print("Make new grd_id column")
    df["grd_id"] = df.apply(
        lambda row: row["Gitter_ID_100m"].replace("100m", ""), axis=1
    )

    print("Drop unecessary column Gitter_ID_100m")
    df = df.drop(["Gitter_ID_100m"], axis=1)

    print("Rename Anzahl column")
    df = df.rename(columns={"Anzahl": "value"})

    print("Pivot")
    df = pd.pivot_table(
        df,
        columns=["Auspraegung_Code"],
        values="value",
        index=["grd_id"],
        aggfunc=np.sum,
        fill_value=0,
    )

    if printfinal:
        print(df)

    print("Save")
    df.to_csv("input/out_" + code + ".csv")

    print("Done " + code)
