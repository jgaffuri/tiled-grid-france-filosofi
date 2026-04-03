from pygridmap import gridtiler
import os


def tuilage(year, geo, resolution, theme, format):
    # défini les paramètres du tuilage en fonction du theme: les colonnes à conserver et la taille de tuile en nombre de cellules
    if theme == "ind":
        cols = ["x","y","imputed","ind","ind_0_3","ind_11_17","ind_18_24","ind_25_39","ind_40_54","ind_4_5","ind_55_64","ind_65_79","ind_6_10","ind_80p","ind_inc"]
        t = 128
    elif theme == "log":
        cols = ["x","y","imputed","ind","log_45_70","log_70_90","log_ap90","log_av45","log_inc","log_soc"]
        t = 128
    elif theme == "men":
        cols = ["x","y","imputed","ind","men","men_1ind","men_5ind","men_coll","men_fmp","men_mais","men_pauv","men_prop","men_surf"]
        t = 128
    elif theme == "inc":
        cols = ["x","y","imputed","ind","ind_snv"]
        t = 256

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

    # transformation par thème: garde uniquement les colonnes d'interet pour le thème
    cols = set(cols)
    def cell_transformation_fun(c):
        for k in list(c.keys()):
            if k not in cols: del c[k]
        return c

    # tuilage
    gridtiler.grid_tiling(
        "tmp/" + str(year) + "_" + geo + "_" + str(resolution) + ".csv",
        "./out/"+format+"/" + geo + "/" + theme + "/" + str(year) + "/" + str(resolution) + "m/",
        resolution,
        tile_size_cell = t,
        x_origin = x,
        y_origin = y,
        format = format,
        crs = crs,
        clean_output_folder = True,
        transform_fun = cell_transformation_fun,
    )



# lance le tuilage pour tous les territoires geographiques, toutes les années, tous les thèmes, toutes les résolution

for geo in ["reun", "mart", "met"]:
    for year in [2021, 2019, 2017, 2015]:
        for resolution in [200, 400, 600, 1000, 2000, 5000, 10000, 20000, 50000, 100000]:
            for theme in ["ind", "log", "men", "inc"]:
                print("*** " + geo + " " + str(year) + " " + theme)
                tuilage(year, geo, resolution, theme, "csv")
                #tuilage(year, geo, resolution, theme, "parquet")
