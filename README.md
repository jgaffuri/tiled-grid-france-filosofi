# tiled-grid-insee-filisofi
Préparation des statistiques carroyées [INSEE](https://www.insee.fr) Filosofi pour une visualisation avec [GridViz](https://github.com/eurostat/gridviz/).

## Données en entrée

Les données Filosofi en entrée sont téléchargeables depuis le site de l'INSEE, par année et territoire:
- 2015: https://www.insee.fr/fr/statistiques/4176290
- 2017: https://www.insee.fr/fr/statistiques/6215217
- 2019: https://www.insee.fr/fr/statistiques/7655515

Il y a un fichier pour la france métropolitaine (*met*), un pour le Réunion (*reun*) et un pour la Martinique (*mart*).

Les fichiers téléchargés doivent tout d'abord être décompressés et renommés pour suivre le même modèle de nom: Par exemple *2019_reun.csv* pour les données de 2019 sur la réunion. Ces fichiers doivent être placés dans un répertoire `input/` pour pouvoir être ensuite traités automatiquement.

## Harmonisation

Malheureusement, ces fichers CSV n'ont pas les mêmes structures et doivent être harmonisés.

Concernant la structure:
- Les colonnes principales sont bien présentes, mais nommées avec des majuscules pour 2015 et 2017, et pas pour 2019. Cela concerne: *ind,men, men_pauv, men_1ind, men_5ind, men_prop, men_fmp, ind_snv, men_surf, men_coll, men_mais, log_av45, log_45_70, log_70_90, log_ap90, log_inc, log_soc, ind_0_3, ind_4_5, ind_6_10, ind_11_17, ind_18_24, ind_25_39, ind_40_54, ind_55_64, ind_65_79, ind_80p, ind_inc* 
- La colonne d'identifiant des carreaux est nommée *idcar_200m* pour 2019, *Idcar_200m* pour 2017 et *IdINSPIRE* pour 2015.
- La colonne sur la donnée d'imputation est nommée *i_est_200* pour 2019, *I_est_200* pour 2015 et *I_est_cr* pour 2015.

Les autre colonnes ne sont pas utilisées et peuvent être supprimées:
- Pour 2019: *idcar_1km, idcar_nat, i_est_1km, lcog_geo*
- Pour 2017: *Idcar_1km, Idcar_nat, I_est_1km, lcog_geo, Groupe*
- Pour 2015: *Id_carr1km, Id_carr_n, Groupe, Depcom, I_pauv, Id_car2010, I_est_1km*

Le script d'harmonisation `harmonise.py`, en Python, est [**ICI**](/src/harmonise.py). Il produit de nouveaux fichiers harmonisés dans un répertoire `tmp/`.

## Tuilage

Le script `tuilage.py` [**ICI**](/src/tuilage.py) formate les données harmonisées (filtrage, transformation, tuilage). Le programme [GridTiler](https://github.com/eurostat/gridtiler#installation) doit être installé au préalable.

Les données sont groupées par thème: Population et niveau de vie, population par âge, logements, ménages.

Les données tuilées finales sont produites dans le répertoire `out/` et peuvent être utilisées directement dans [GridViz](https://github.com/eurostat/gridviz/).

Note: Pour exécuter le script de tuilage, il peut être nécessaire d'augmenter la taille mémoire de nodeJS en exécutant l'instruction `export NODE_OPTIONS="--max-old-space-size=16384"`.

## Séries temporelles

Le script `series_temporelles.py` [**ICI**](/src/series_temporelles.py) joint les données harmonisées pour construire des fichiers de séries temporelles sur les trois années 2015, 2017 et 2019. Les données tuilées finales sont produites dans le répertoire `out/`.

## Visualisation avec GridViz

Par exemple, pour visualiser la grille à 1000m des données de population par âge se France métropolitaine, utiliser l'URL: https://raw.githubusercontent.com/jgaffuri/tiled-grid-france-filosofi/main/out/csv/met/ind/2019/1000m/info.json

Voir des exemples de visualisation [GridViz](https://github.com/eurostat/gridviz/) [**ICI**](https://eurostat.github.io/gridviz/examples/FR.html) et [**LA**](https://eurostat.github.io/gridviz/examples/FR_pop.html). 
