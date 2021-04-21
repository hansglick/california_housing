from lib import *

proj_buffer = pyproj.Proj(proj="utm", ellps="WGS84", datum="WGS84")


def toFromUTM(shp, proj_buffer, inv=False):

	geoInterface = shp.__geo_interface__
	shpType = geoInterface['type']
	coords = geoInterface['coordinates']
	if shpType == 'Polygon':
		newCoord = [[proj_buffer(*point, inverse=inv) for point in linring] for linring in coords]
	elif shpType == 'MultiPolygon':
		newCoord = [[[proj_buffer(*point, inverse=inv) for point in linring] for linring in poly] for poly in coords]

	return shape({'type': shpType, 'coordinates': tuple(newCoord)})


def Buffer_A_Shape(myshape,distance_buffer_meters):

	init_shape_utm = toFromUTM(myshape, proj_buffer)
	buffer_shape_utm = init_shape_utm.buffer(distance_buffer_meters)
	buffer_shape_lonlat = toFromUTM(buffer_shape_utm, proj_buffer, inv=True)

	return buffer_shape_lonlat




def ColorMapper(minval,maxval,values,palette = "PiYG"):
    norm = matplotlib.colors.Normalize(vmin=minval, vmax=maxval)
    cmap = cm.get_cmap(palette)
    m = cmap(norm(values))[:,:-1]
    hex_array = [matplotlib.colors.rgb2hex(item) for item in [tuple(m[row,:]) for row in range(m.shape[0])]]
    return hex_array