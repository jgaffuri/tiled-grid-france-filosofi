import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tuilage.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tuilage.py


# increase javascript heap size
# export NODE_OPTIONS="--max-old-space-size=16384"
# subprocess.run(['export NODE_OPTIONS="--max-old-space-size=16384"'])


def tuilage(year, geo, a, t, crs, x, y):
    print(year + " " +geo+ " " + str(a * 200) + "m")

    # gridtiler -i ./input/out_ALTER_KURZ.csv -r 100 -c 3035 -x 3900000 -y 2600000 -p "const a = c.grd_id.split('N')[1].split('E'); return { x:100*a[1],y:100*a[0] };" -m "delete c.grd_id" -a 1 -o ./out/ALTER_KURZcsv/100m/ -e csv

    subprocess.run(
        [
            "gridtiler",
            "-i",
            "./tmp/"+year+"_" + geo + ".csv",
            "-r",
            "200",
            "-c",
            crs,
            "-x",
            x,
            "-y",
            y,
            "-p",
            "const a = c.grd_id.split('N')[1].split('E'); return { x:a[1],y:a[0] };", #TODO check that
            "-m",
            "delete c.id",
            "-a",
            str(a),
            "-o",
            "./out/csv/" + year + "/" + geo + "/" + str(a * 200) + "m/",
            "-t",
            str(t),
            "-e",
            "csv",
        ]
    )
