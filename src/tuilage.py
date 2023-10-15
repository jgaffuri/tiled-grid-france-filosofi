import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tuilage.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tuilage.py

# increase javascript heap size
# export NODE_OPTIONS="--max-old-space-size=16384"
# subprocess.run(['export NODE_OPTIONS="--max-old-space-size=16384"'])


def getParams(year, geo, a, t, crs, x, y, outFolder):
    return [
        "gridtiler",
        "-i",
        "./tmp/" + year + "_" + geo + ".csv",
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
        "./out/csv/" + outFolder + "/" + year + "/" + geo + "/" + str(a * 200) + "m/",
        "-t",
        str(t),
        "-e",
        "csv",
    ]


def tuilage(year, geo, a, crs, x, y):
    print("*** " + year + " " + geo + " " + str(a * 200) + "m")

    # ind
    params = getParams(year, geo, a, 128, crs, x, y, "ind")
    params.append("-s")
    params.append("id,imputed,ind,ind_0_3,ind_11_17,ind_18_24,ind_25_39,ind_40_54,ind_4_5,ind_55_64,ind_65_79,ind_6_10,ind_80p,ind_inc")
    subprocess.run(params)

    # log
    params = getParams(year, geo, a, 128, crs, x, y, "log")
    params.append("-s")
    params.append("id,imputed,ind,log_45_70,log_70_90,log_ap90,log_av45,log_inc,log_soc")
    subprocess.run(params)

    # men
    params = getParams(year, geo, a, 128, crs, x, y, "men")
    params.append("-s")
    params.append("id,imputed,ind,men,men_1ind,men_5ind,men_coll,men_fmp,men_mais,men_pauv,men_prop,men_surf")
    subprocess.run(params)

    # inc
    params = getParams(year, geo, a, 256, crs, x, y, "inc")
    params.append("-s")
    params.append("id,imputed,ind,ind_snv")
    subprocess.run(params)




for a in [1, 2, 5, 10, 20, 50, 100, 200, 500]:
    #tuilage("2019", "met", a, "3035", 0, 0)
    tuilage("2019", "reun", a, "2975", 300000, 7600000)
    tuilage("2019", "mart", a, "5490", 0, 0)
