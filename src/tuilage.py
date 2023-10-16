import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tuilage.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tuilage.py

def tuilage(year, geo, a, rounding, theme):
    # défini les paramètres du tuilage en fonction du theme
    if theme == "ind":
        t = 128
        cols = "id,imputed,ind,ind_0_3,ind_11_17,ind_18_24,ind_25_39,ind_40_54,ind_4_5,ind_55_64,ind_65_79,ind_6_10,ind_80p,ind_inc"
    elif theme == "log":
        t = 128
        cols = "id,imputed,ind,log_45_70,log_70_90,log_ap90,log_av45,log_inc,log_soc"
    elif theme == "men":
        t = 128
        cols = "id,imputed,ind,men,men_1ind,men_5ind,men_coll,men_fmp,men_mais,men_pauv,men_prop,men_surf"
    elif theme == "inc":
        t = 256
        cols = "id,imputed,ind,ind_snv"

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


# augmente la taille mémoire utilisable par javascript / nodejs
# export NODE_OPTIONS="--max-old-space-size=16384"


# lance le tuilage pour tous les territoires geographiques, toutes les années, tous les thèmes et toutes les résolution

#for geo in ["reun", "mart", "met"]:
for geo in ["met"]:
    for year in [2019, 2017, 2015]:
        for theme in ["ind", "log", "men", "inc"]:
            #for a in [1, 2, 3, 5, 10, 25, 50, 100, 250, 500]:
            for a in [3]:
                print("*** " + geo + " " + str(year) + " " + theme + " " + str(a*200) + "m")
                tuilage(year, geo, a, 2, theme)
