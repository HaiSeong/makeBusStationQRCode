
from openpyxl import load_workbook
import qrcode
from PIL import *


# 서울시 정류장 정보 엑셀파일 가져오기
load_wb = load_workbook("/Users/apple/Desktop/공부/휴학/학술제/서울시정류장정보.xlsx", data_only=True)
load_ws = load_wb['Sheet0']
get_cells = load_ws['B2' : 'C11180']
station_len = 11180-1

# 서울시 정류장 정보를 리스트에 튜플형태로 저장
busStationListInSeoul = []
for row in get_cells:
    list = []
    for cell in row:
        list.append(cell.value)
    tuple = (list[0],list[1]) # (stNm / arsId / )
    busStationListInSeoul.append(tuple)


for station in busStationListInSeoul:
    print('----------------------------------------')
    print(station)
    arsId = station[1]
    print(arsId)
    stNm = station[0]
    print(stNm)
    url = "http://13.124.23.169//getBusList/?arsId=" + arsId
    print(url)
    img = qrcode.make(url)
    img.save("qrcode/" + arsId + "_" + stNm + ".png")
    print(str(stNm) + "의 qrcode 생성")
