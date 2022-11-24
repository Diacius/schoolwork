#https://www.easyflip.co.uk/CPC_Catalogue_2021/large/{PAGERNUMBER}.jpg?uid=1669291932599
#TRADE - https://www.easyflip.co.uk/CPC_Catalogue/large/{pagenumber}.jpg?uid=1669292098880
import requests
for i in range(2270):
    response = requests.get(f"https://www.easyflip.co.uk/CPC_Catalogue/large/{i}.jpg?uid=1669292098880")
    with open(f"{i}.jpg", "wb") as filehandle:
        filehandle.write(response.content)