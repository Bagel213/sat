#https://rhodesmill.org/skyfield/earth-satellites.html
from skyfield.api import EarthSatellite
from skyfield.api import load
from skyfield.api import Topos

ts = load.timescale()

# Load the given TLE and 'create' a satellite
line1 = '1 13337U 98067A   20087.38052801 -.00000452  00000-0  00000+0 0  9995'
line2 = '2 13337  51.6460  33.2488 0005270  61.9928  83.3154 15.48919755219337'
satellite = EarthSatellite(line1, line2, 'REDACT', ts)
print(satellite)

#Set the time (not sure if the hrs min sec are right order?)
t = ts.utc(2020, 3, 26, 21, 52, 52)

geocentric = satellite.at(t)

#x,y,z coordinates
print(geocentric.position.km)

#position above the earth
subpoint = geocentric.subpoint()
print('Latitude:', subpoint.latitude)
print('Longitude:', subpoint.longitude)
print('Elevation (m):', int(subpoint.elevation.m))

#tropocentric (from where we are, the Wash Monument)
dc = Topos('38.88948 N', '77.03528 W')
difference = satellite - dc
geometry = difference.at(t)
topocentric = difference.at(t)
alt, az, distance = topocentric.altaz()
print('elevation = ',alt)
print('azimuth = ',az)
print('distance km = ',distance.km)