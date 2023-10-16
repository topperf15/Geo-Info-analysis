// matlab script for lesson 6
// based on lesson 2
// read in the shapefiles
// WGS84 UTM 18N is EPSG 32618
txCo = readgeotable(txco.shp); //alt is shapefileread
txSeat = readgeotable(txseat.shp);
figure
axesm('eqaconic','MapLatLimit',[38,40],'MapLonLimit',[-79,-76]) // what is is for TX
//geoshow(lat,lon) projects and displays the latitude and longitude vectors lat and lon 
//using the projection stored in the current axesm-based map (previously referred to as map axes).
//If there is no current axesm-based map, then lat and lon are projected
//using a default Plate Carrée projection on a set of regular axes.
//geoshow('landareas.shp','FaceColor','black')
geoshow(txCo)
geoshow(txSeat)
//buffer the seats
[latb,lonb] = bufferm(txSeat.lat,txSeat.lon,km2deg(200))
geoshow(latb.lonb,'k--')
//drop a circle on an input point
[latin,lonin] = inputm(1);
circrad = km2deg(10); //10 km in deg
[lats,lons] = scircle1(latin,lonin,circrad);
geoshow(lats,lons)
//new figure with georaster play with sea surface temps
//script in folder already
//vec2mtx
//geoplot for thematic maps found in plots