import pandas as pd

# /home/juju/pythonvenvgridDE/bin/python ./src/join.py /usr/bin/python3 /home/juju/workspace/tiled-grid-france-filosofi/src/join.py


# Load file for each year and extract data for time series
def extract(year, geo, printfinal=False):
    print("load " + year + " " + geo)
    d = pd.read_csv("./tmp/" + year + "_" + geo + ".csv")
    # print("select columns")
    d = d[["id", "ind", "imputed"]]
    # print("rename columns")
    d = d.rename(columns={"ind": "ind" + year, "imputed": "imp" + year})
    if printfinal:
        print(d)
    return d


# Join data per year
def join(geo, printfinal=False):
    d = extract("2015", geo)
    d = pd.merge(d, extract("2017", geo), on="id", how="outer")
    d = pd.merge(d, extract("2019", geo), on="id", how="outer")
    if printfinal:
        print(d)
    return d


# Prepare data for time series
for geo in ["reun", "mart", "met"]:
    print("*** Join " + geo)
    d = join(geo)
    # Save
    d.to_csv("./tmp/ts_pop_" + geo + ".csv", index=False)



    # execute tuilage, via gridtiler
    subprocess.run(
        [
            "gridtiler",
            "-i",
            "./tmp/" + str(year) + "_" + geo + ".csv",
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
            "./out/csv/"
            + geo
            + "/"
            + theme
            + "/"
            + str(year)
            + "/"
            + str(a * 200)
            + "m/",
            "-t",
            str(t),
            "-s",
            cols,
            "-R",
            str(rounding),
            "-e",
            "csv",
        ]
    )


