import fiona
import pyproj
import matplotlib
import folium

from shapely.strtree import STRtree
from shapely.geometry import shape
from shapely.geometry import Polygon
from shapely.geometry import MultiPolygon
from shapely.geometry import Point

import pandas as pd
import numpy as np

from scipy import stats
from folium import plugins