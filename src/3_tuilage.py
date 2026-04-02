from pygridmap import gridtiler
import os


def tuilage(year, geo, resolution, theme):
    # défini les paramètres du tuilage en fonction du theme
    if theme == "ind":
        t = 128
        cols = ["x","y","imputed","ind","ind_0_3","ind_11_17","ind_18_24","ind_25_39","ind_40_54","ind_4_5","ind_55_64","ind_65_79","ind_6_10","ind_80p","ind_inc"]
    elif theme == "log":
        t = 128
        cols = ["x","y","imputed","ind","log_45_70","log_70_90","log_ap90","log_av45","log_inc","log_soc"]
    elif theme == "men":
        t = 128
        cols = ["x","y","imputed","ind","men","men_1ind","men_5ind","men_coll","men_fmp","men_mais","men_pauv","men_prop","men_surf"]
    elif theme == "inc":
        t = 256
        cols = ["x","y","imputed","ind","ind_snv"]

    cols = set(cols)

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

    # transformation par thème
    def cell_transformation_fun(c):
        for k in list(c.keys()):
            if k not in cols: del c[k]

    input_file = "tmp/" + str(year) + "_" + geo + "_" + str(resolution) + ".csv"
    out_file = "tmp/" + str(year) + "_" + geo + "_" + str(resolution) + "_" + theme + ".csv"
    gridtiler.grid_transformation(input_file, cell_transformation_fun, out_file)

    #create output folder
    #out_folder = 'out/csv/' +geo+ str(resolution)
    #if not os.path.exists(out_folder): os.makedirs(out_folder)

    # tuilage
    gridtiler.grid_tiling(
        out_file,
        "./out/csv/" + geo + "/" + theme + "/" + str(year) + "/" + str(resolution) + "m/",
        resolution,
        tile_size_cell = t,
        x_origin = x,
        y_origin = y,
        format = "csv", #"parquet",
        crs = crs,
        clean_output_folder = True,
    )



'''
    # execute tuilage, via gridtiler
    subprocess.run(
        [
            "gridtiler",
            "-i", "./tmp/" + str(year) + "_" + geo + ".csv",
            "-r", "200",
            "-c", crs,
            "-x", str(x),
            "-y", str(y),
            "-p", "const a = c.id.split('N')[1].split('E'); return { x:a[1],y:a[0] };",
            "-m", "delete c.id",
            "-a", str(a),
            "-o", "./out/csv/" + geo + "/" + theme + "/" + str(year) + "/" + str(a * 200) + "m/",
            "-t", str(t),
            "-s", cols,
            "-R", str(rounding),
            "-e", "csv",
        ]
    )
'''



# lance le tuilage pour tous les territoires geographiques, toutes les années, tous les thèmes et toutes les résolution

for geo in ["reun", "mart", "met"]:
    for year in [2021, 2019, 2017, 2015]:
        for resolution in [200, 400, 600, 1000, 2000, 5000, 10000, 20000, 50000, 100000]:
            for theme in ["ind", "log", "men", "inc"]:
                print("*** " + geo + " " + str(year) + " " + theme)
                tuilage(year, geo, resolution, theme)
