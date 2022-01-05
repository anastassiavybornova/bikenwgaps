# parameters for plotting

plotparam = {"dpi": 96}

# create basemaps dict for folium tile layers
basemaps = {
    'Google Maps': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Maps',
                overlay = True,
                control = True
        ),
    'Google Satellite': folium.TileLayer(
                tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
                attr = 'Google',
                name = 'Google Satellite',
                overlay = True,
                control = True
        ),
'st_lite_op3': folium.TileLayer(
        tiles = 'https://stamen-tiles.a.ssl.fastly.net/toner-lite/{z}/{x}/{y}.png',
        attr = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        name = 'Stamen Toner Lite O3',
        overlay = True,
        control = True,
        opacity = 0.3),
    'osm': folium.TileLayer(
        tiles = "openstreetmap", 
        name = "OpenStreetMap",
        control = True, 
        overlay = True),
    'white_background': folium.TileLayer(
        tiles = 'https://api.mapbox.com/styles/v1/krktalilu/ckrdjkf0r2jt217qyoai4ndws/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1Ijoia3JrdGFsaWx1IiwiYSI6ImNrcmRqMXdycTB3NG8yb3BlcGpiM2JkczUifQ.gEfOn5ttzfH5BQTjqXMs3w',
        name = "White background",
        attr = 'Mapbox',
        control = True,
        overlay = True
        )

}