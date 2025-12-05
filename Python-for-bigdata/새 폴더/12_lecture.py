import folium
from folium.plugins import MiniMap, MousePosition, MarkerCluster

# 좌표
dongyang = [37.5007, 126.8677]
chongshin = [37.4888, 126.9669]
jaeneung = [37.4751, 126.6498]

# 중심
center = [
    (dongyang[0] + chongshin[0] + jaeneung[0]) / 3,
    (dongyang[1] + chongshin[1] + jaeneung[1]) / 3
]

# 지도 생성
x = folium.Map(
    location=center,
    zoom_start=11,
    tiles="CartoDB positron"
)

# 마커 클러스터 생성
cluster = MarkerCluster().add_to(x)

# 팝업
dongyang_popup = "<b>동양미래대학교</b>"
chongshin_popup = "<b>총신대학교</b>"
jaeneung_popup = "<b>재능대학교</b>"

# 마커 (클러스터에 추가)
folium.Marker(dongyang, popup=dongyang_popup, tooltip="동양미래대학교").add_to(cluster)
folium.Marker(chongshin, popup=chongshin_popup, tooltip="총신대학교").add_to(cluster)
folium.Marker(jaeneung, popup=jaeneung_popup, tooltip="재능대학교").add_to(cluster)

# 미니맵
x.add_child(MiniMap(toggle_display=True))

# 저장
x.save("map_cluster.html")
