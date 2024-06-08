from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

m = Basemap(projection="merc", llcrnrlat=24, urcrnrlat=40, llcrnrlon=44, urcrnrlon=64, resolution="i")

cities = {
    "Tehran": (35.6895, 51.3890, 9),
    "Isfahan": (32.4279, 51.6894, 2.2),
    "Shiraz": (29.5926, 52.5836, 1.8),
    "Mashhad": (36.326389, 59.543333, 3),
    "Tabriz": (38.081389, 46.300556, 1.7),
    "Ahvaz": (31.304722, 48.678333, 1.2),
    "Kermanshah": (34.3325, 47.093333, 0.9),
    "Urmia": (37.543889, 45.064722, 0.7),
    "Zahedan": (29.5025, 60.855833, 0.5),
    "Yazd": (31.882222, 54.339722, 0.5)
}

for city,(lat, lon, pop) in cities.items():
    x, y = m(lon, lat)
    m.scatter(x, y, s=pop*100)

m.drawcountries()
m.drawcoastlines()
# m.fillcontinents(color="lightgreen",lake_color="aqua")
# m.drawmapboundary(fill_color='aqua') 

map_title=get_display(arabic_reshaper.reshape("نقشه ایران"))

plt.title(map_title)
plt.show()