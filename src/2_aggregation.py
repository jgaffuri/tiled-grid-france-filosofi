from pygridmap import gridtiler


for geo in ["mart","reun","met"]:
    for year in ["2015","2017","2019","2021"]:
        for a in [2,3,5,10,25,50,100,250,500]:
            res = int(a*200)
            print("*** "+year+" "+geo+" "+str(res))
            gridtiler.grid_aggregation(input_file="tmp/"+year+"_"+geo+"_200.csv", resolution=200, output_file="tmp/"+year+"_"+geo+"_"+str(res)+".csv", a=a)

