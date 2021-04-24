import fiona
import pyproj
import matplotlib
import folium
import py3dep
import json
import shapely

from shapely.strtree import STRtree
from shapely.geometry import shape
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import Point

import geopandas as gpd
import pandas as pd
import numpy as np

from scipy import stats
from folium import plugins
from matplotlib import cm



from IPython.display import clear_output, display