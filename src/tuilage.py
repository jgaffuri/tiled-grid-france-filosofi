import subprocess

# /home/juju/pythonvenvgridDE/bin/python ./src/tuilage.py /usr/bin/python3 /home/juju/workspace/tiled-grid-germany-zensus2011/src/tuilage.py


#ind
#log
#men
#pop


def tuilage(year, geo, a, t, crs, x, y):
    print(year + " " +geo+ " " + str(a * 200) + "m")

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
            "const a = c.grd_id.split('N')[1].split('E'); return { x:a[1],y:a[0] };",
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
