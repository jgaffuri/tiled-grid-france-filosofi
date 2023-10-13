# tiled-grid-insee-filisofi
Preparation des statistiques carroyées INSEE-FR FILOSOFI pour une visualisation avec [GridViz](https://github.com/eurostat/gridviz/).

## Données en entrée

Les données peuvent être téléchargées depuis le site de l'INSEE, par année:
- 2015: https://www.insee.fr/fr/statistiques/4176290
- 2017: https://www.insee.fr/fr/statistiques/6215217
- 2019: https://www.insee.fr/fr/statistiques/7655515

Les fichiers en entrée sont dans le répertoire [/input/]. Les fichiers ont été renomés pour suivre le même modèle de nom.

## Harmonisation de structure

Malheureusement, les fichers CSV n'ont pas la même structure et doivent être harmonisés.
- Les colonnes principale sont bien présentes, mais nommées avec des majuscules pour 2015 et 2017 files, et pas pour 2019. Cela concerne: *ind,men,men_pauv,men_1ind,men_5ind,men_prop,men_fmp,ind_snv,men_surf,men_coll,men_mais,log_av45,log_45_70,log_70_90,log_ap90,log_inc,log_soc,ind_0_3,ind_4_5,ind_6_10,ind_11_17,ind_18_24,ind_25_39,ind_40_54,ind_55_64,ind_65_79,ind_80p,ind_inc* 
- Les identifiants des carreaux sont *idcar_200m* pour 2019, *Idcar_200m* pour 2017 et *IdINSPIRE* pour 2015.
- Les données d'imputation sont *i_est_200* pour 2019, *I_est_200* pour 2015 et *I_est_cr* pour 2015.

Les autre colonnes peuvent être supprimées:
- Pour 2019, nous avons: idcar_1km,idcar_nat,i_est_1km,lcog_geo,
- Pour 2017, nous avons: Idcar_1km,Idcar_nat,I_est_1km,lcog_geo, Groupe
- Pour 2015, nous avons: Id_carr1km,Id_carr_n,Groupe,Depcom,I_pauv,Id_car2010,I_est_1km

TODO: script d'harmonisation
TODO: voir https://github.com/jgaffuri/tiledgrids/tree/main/data/france/filosofi


## Tiling

