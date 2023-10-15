#!/home/juju/pythonvenvgridDE/bin python

# /home/juju/pythonvenvgridDE/bin/python ./src/preparation.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/harmonise.py

import pandas as pd
import numpy as np
import os  


def harmonise(year, geo, printfinal):

    print("Charge "+year+" " + geo)
    df = pd.read_csv("input/"+year+"_"+geo+".csv") #, nrows=10000)

    print("Supprime colonnes inutilisées")
    colsSup = ["Id_carr1km", "Id_carr_n", "Groupe", "Depcom", "I_pauv", "Id_car2010", "I_est_1km"] if year == "2015" else ["Idcar_1km", "Idcar_nat", "I_est_1km", "lcog_geo", "Groupe"] if year == "2017" else ["idcar_1km", "idcar_nat", "i_est_1km", "lcog_geo"] if year == "2019" else []
    df = df.drop(colsSup, axis=1)

    print("Renomme colonne id")
    colId = "IdINSPIRE" if year=="2015" else "Idcar_200m" if year == "2017" else "idcar_200m" if year == "2019" else ""
    df = df.rename(columns={colId: "id"})

    print("Renomme colonne imputation")
    colImp = "I_est_cr" if year=="2015" else "I_est_200" if year == "2017" else "i_est_200" if year == "2019" else ""
    df = df.rename(columns={colImp: "imputed"})

    print("Change noms colonnes en lettres minuscules")
    df.columns = df.columns.str.lower()

    print("Classe colonnes par ordre alphabétique")
    df = df.reindex(sorted(df.columns), axis=1)

    if(printfinal): print(df)

    print("Sauvegarde")
    if not os.path.exists('tmp'): os.makedirs('tmp')
    df.to_csv("tmp/"+year+"_"+geo+".csv", index=False)

    print("Fait - "+year+" " + geo)



harmonise("2015", "reun", False)
harmonise("2015", "mart", False)
harmonise("2015", "met", False)
harmonise("2017", "reun", False)
harmonise("2017", "mart", False)
harmonise("2017", "met", False)
harmonise("2019", "reun", False)
harmonise("2019", "mart", False)
harmonise("2019", "met", False)


