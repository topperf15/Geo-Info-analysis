vel = 200; %nm per hr (kts)
theta = 15; %degrees bank angle
acTurnRad = vel^2/(11.26*tan(theta); %feet
[latin,lonin] = inputm(2);
circrad = nm2deg(acTurnRad/6076); 
[latb,lonb] = bufferm(latin,lonin,circrad);
geoshow(lats,lons)
