#!/bin/sh
cat <<EOF
{
"type": "FeatureCollection",
"name": "FreeBSD_committers",
"crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
"features": [
EOF
while read line; do
	IFS="	"
	set - $(echo $line | sed -ne 's/^[ 	]*\([^#][^,]*\),[ 	]*\([^,]*\),[ 	]*"[ 	,]*\([^"]*\)".*/\1	\2	\3/p')
	lat=$1
	long=$2
	IFS=" 	,"
	for name in $3; do
		printf '%s{ "type": "Feature", "properties": { "name": "%s" }, "geometry": { "type": "Point", "coordinates": [ %s, %s ] } }' "$sep" "$name" "$long" "$lat"
		sep=","$'\n'
	done
done < freebsd.committers.markers
printf '\n]\n}'
