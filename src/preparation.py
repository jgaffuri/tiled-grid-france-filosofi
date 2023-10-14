#!/home/juju/pythonvenvgridDE/bin python

# /home/juju/pythonvenvgridDE/bin/python ./src/preparation.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/preparation.py

import pandas as pd
import numpy as np


print("Load data")
df = pd.read_csv("2019_reun.csv") #, nrows=10000)

print(df)




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

