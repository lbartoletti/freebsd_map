with open('freebsd.committers.markers') as f:
    with open('freebsd_committers.geojson', 'w') as g:
        g.write('{\n')
        g.write('"type": "FeatureCollection",\n')
        g.write('"name": "FreeBSD_committers",\n')
        g.write('"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },\n')
        g.write('"features": [\n')
        lines = f.readlines()
        nb = len(lines)
        for i, l in enumerate(lines):
            if len(l) > 1 and l[0] != '#':
                splittedLine = "".join(l[0:l.replace('align=','#').index('#')].replace(' ,','').replace(',"','').replace('"', '').split()).split(',')
                lat, lon = splittedLine[0:2]
                for name in splittedLine[2:len(splittedLine)]:
                    # print('{},{},{}'.format(lon,lat,name))
                    g.write('{ "type": "Feature", "properties": { "name": "' + name + '" }')
                    g.write(', "geometry": { "type": "Point", "coordinates": [ ' + lon + ', ' + lat +' ] } }')
                    if i+1 < nb:
                        g.write(',\n')
        g.write('\n]\n}')
