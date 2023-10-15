import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tuilage.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tuilage.py

# increase javascript heap size
# export NODE_OPTIONS="--max-old-space-size=16384"
# subprocess.run(['export NODE_OPTIONS="--max-old-space-size=16384"'])


# Construit une liste de paramètres par défaut pour gridtiler
def getParams(year, geo, a, t, crs, x, y, rounding, outFolder):
    return [
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
        + outFolder
        + "/"
        + str(year)
        + "/"
        + geo
        + "/"
        + str(a * 200)
        + "m/",
        "-t",
        str(t),
        "-R",
        str(rounding),
        "-e",
        "csv",
    ]


#
def tuilage(year, geo, a, crs, x, y):
    print("*** " + str(year) + " " + geo + " " + str(a * 200) + "m")

    # population, par âge
    params = getParams(year, geo, a, 128, crs, x, y, 2, "ind")
    params.append("-s")
    params.append(
        "id,imputed,ind,ind_0_3,ind_11_17,ind_18_24,ind_25_39,ind_40_54,ind_4_5,ind_55_64,ind_65_79,ind_6_10,ind_80p,ind_inc"
    )
    subprocess.run(params)

    # logements
    params = getParams(year, geo, a, 128, crs, x, y, 2, "log")
    params.append("-s")
    params.append(
        "id,imputed,ind,log_45_70,log_70_90,log_ap90,log_av45,log_inc,log_soc"
    )
    subprocess.run(params)

    # menages
    params = getParams(year, geo, a, 128, crs, x, y, 2, "men")
    params.append("-s")
    params.append(
        "id,imputed,ind,men,men_1ind,men_5ind,men_coll,men_fmp,men_mais,men_pauv,men_prop,men_surf"
    )
    subprocess.run(params)

    # inc
    params = getParams(year, geo, a, 256, crs, x, y, 2, "inc")
    params.append("-s")
    params.append("id,imputed,ind,ind_snv")
    subprocess.run(params)


# lance le tuilage pour toutes les années, toutes les résolution et tous les territoires geographiques
for year in [2019, 2017, 2015]:
    for a in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
        # reunion
        tuilage(year, "reun", a, "2975", 300000, 7600000)
        # martinique
        tuilage(year, "mart", a, "5490", 600000, 1500000)
        # metropole
        tuilage(year, "met", a, "3035", 3200000, 2000000)
