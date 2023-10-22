import pandas as pd

# /home/juju/pythonvenvgridDE/bin/python ./src/join.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/join.py


def extract(year, geo, printfinal=False):
    print("load " + year + " " + geo)
    d = pd.read_csv("./tmp/" + year + "_" + geo + ".csv")
    #print("select columns")
    d = d[["id", "ind", "imputed"]]
    #print("rename columns")
    d = d.rename(columns={"ind": "ind" + year, "imputed": "imp" + year})
    if printfinal:
        print(d)
    return d


def prepareJoin(geo, printfinal=False):
    d = extract("2019", geo)
    d = pd.merge(d, extract("2017", geo), on="id", how="outer")
    d = pd.merge(d, extract("2015", geo), on="id", how="outer")
    if printfinal:
        print(d)
    return d


# for geo in ["reun", "mart", "met"]:
geo = "met"
d = prepareJoin(geo, True)
d.to_csv("./tmp/ts_pop_" + geo + ".csv", index=False)
