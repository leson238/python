import cv2
import folium as fl
m = fl.Map(location=[20.996469, 105.829733], zoom_start=12, tiles='Stamen Terrain')
m.save('map.html')