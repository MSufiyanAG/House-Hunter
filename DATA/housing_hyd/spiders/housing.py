import scrapy
from ..items import HousingHydItem

base_url = "https://www.nobroker.in/api/v1/multi/property/filter?pageNo={}&searchParam=W3sibGF0IjoxNy40NDcwNTY5NDg3OTM1LCJsb24iOjc4LjU2ODcxMzk1MDMyMjEsInNob3dNYXAiOmZhbHNlLCJwbGFjZUlkIjoiQ2hJSng5THI2dHFaeXpzUnd2dTZrb08zazY0IiwicGxhY2VOYW1lIjoiSHlkZXJhYmFkIiwiY2l0eSI6Imh5ZGVyYWJhZCJ9XQ==&rent=0,100000&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&city=hyderabad"
class HousingSpider(scrapy.Spider):
    name = 'housing'
    start_urls = [
        base_url.format(1)
    ]
    page_number = 2

    def parse(self, response):
        items = HousingHydItem()
        data = response.json()

        for i in range(len(data['data'])):
            try:
                items['property_age'] = data['data'][i]['propertyAge']
            except:
                items['property_age'] = "None"    
            try:
                items['parking'] = data['data'][i]['parking']
            except:
                items['parking'] = "None"
            try:
                items['balconies'] = data['data'][i]['balconies']
            except:
                items['balconies'] = "None"
            try:
                items['parkingDesc'] = data['data'][i]['parkingDesc']
            except:
                items['parkingDesc'] = "None"
            try:
                items['furnishingDesc'] = data['data'][i]['furnishingDesc']
            except:
                items['furnishingDesc'] = "None"
            try:
                items['type_bhk'] = data['data'][i]['type']
            except:
                items['type_bhk'] = "None"
            try:
                items['rent_amount'] = data['data'][i]['rent']
            except:
                items['rent_amount'] = "None"
            try:
                items['property_size'] = data['data'][i]['propertySize']
            except:
                items['property_size'] = "None"
            try:
                items['loanAvailable'] = data['data'][i]['loanAvailable']
            except:
                items['loanAvailable'] = "None"
            try:
                items['id'] = data['data'][i]['id']
            except:
                items['id'] = "None"
            try:
                items['localityId'] = data['data'][i]['localityId']
            except:
                items['localityId'] = "NOT_FOUND"
            try:
                items['bathroom'] = data['data'][i]['bathroom']
            except:
                items['bathroom'] = "None"
            try:
                items['propertyTitle'] = data['data'][i]['propertyTitle']
            except:
                items['propertyTitle'] = "None"
            try:
                items['locality'] = data['data'][i]['locality']
            except:
                items['locality'] = "None"
            try:
                items['active'] = data['data'][i]['active']
            except:
                items['active'] = "None"
            try:
                items['maintenanceAmount'] = data['data'][i]['maintenanceAmount']
            except:
                items['maintenanceAmount'] = "None"
            try:
                items['swimmingPool'] = data['data'][i]['swimmingPool']
            except:
                items['swimmingPool'] = "None"
            try:
                items['completeStreetName'] = data['data'][i]['completeStreetName']
            except:
                items['completeStreetName'] = "None"
            try:
                items['totalFloor'] = data['data'][i]['totalFloor']
            except:
                items['totalFloor'] = "None"
            try:
                items['lift'] = data['data'][i]['lift']
            except:
                items['lift'] = "None"
            try:
                items['deposit'] = data['data'][i]['deposit']
            except:
                items['deposit'] = "None"
            try:
                items['gym'] = data['data'][i]['gym']
            except:
                items['gym'] = "None"
            try:
                items['facingDesc'] = data['data'][i]['facingDesc']
            except:
                items['facingDesc'] = "None"
            try:
                items['amenities'] = data['data'][i]['amenities']
            except:
                items['amenities'] = "None"
            try:
                items['shortUrl'] = data['data'][i]['shortUrl']
            except:
                items['shortUrl'] = "None"
            try:
                items['facing'] = data['data'][i]['facing']
            except:
                items['facing'] = "None"
            try:
                items['ownerName'] = data['data'][i]['ownerName']
            except:
                items['ownerName'] = "None"
            try:
                items['propertyType'] = data['data'][i]['propertyType']
            except:
                items['propertyType'] = "None"
            try:
                items['floor'] = data['data'][i]['floor']
            except:
                items['floor'] = "None"
            try:
                items['location'] = data['data'][i]['location']
            except:
                items['location'] = "None"
            try:
                items['isMaintenance'] = data['data'][i]['maintenance']
            except:
                items['isMaintenance'] = "false"
            try:
                items['sharedAccomodation'] = data['data'][i]['sharedAccomodation']
            except:
                items['sharedAccomodation'] = "None"
            try:
                items['waterSupply'] = data['data'][i]['waterSupply']
            except:
                items['waterSupply'] = "None"
            try:
                items['reactivationSource'] = data['data'][i]['reactivationSource']
            except:
                items['reactivationSource'] = "None"

            yield items

        next_page = "https://www.nobroker.in/api/v1/multi/property/filter?pageNo=" + str(HousingSpider.page_number) + "&searchParam=W3sibGF0IjoxNy40NDcwNTY5NDg3OTM1LCJsb24iOjc4LjU2ODcxMzk1MDMyMjEsInNob3dNYXAiOmZhbHNlLCJwbGFjZUlkIjoiQ2hJSng5THI2dHFaeXpzUnd2dTZrb08zazY0IiwicGxhY2VOYW1lIjoiSHlkZXJhYmFkIiwiY2l0eSI6Imh5ZGVyYWJhZCJ9XQ==&rent=0,100000&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&city=hyderabad"       
        if HousingSpider.page_number <= 910:
            HousingSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)   