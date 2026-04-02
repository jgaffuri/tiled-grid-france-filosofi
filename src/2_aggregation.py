from pygridmap import gridtiler



for geo in ["mart","reun","met"]:
    for year in ["2015","2017","2019","2021"]:
        for res in ["200","400","600","1000","2000","5000","10000","20000","50000"]:
            print("*** "+year+" "+geo+" "+res)
            gridtiler.grid_aggregation(input_file=aggregated_folder+"1000.csv", resolution=1000, output_file=aggregated_folder+str(a*1000)+".csv", a=a, aggregation_fun=aggregation_fun)

