# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HousingHydItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    property_age = scrapy.Field()
    parking = scrapy.Field()
    parkingDesc = scrapy.Field()
    balconies = scrapy.Field()
    furnishingDesc = scrapy.Field()
    type_bhk = scrapy.Field()
    rent_amount = scrapy.Field()
    property_size = scrapy.Field()
    loanAvailable = scrapy.Field()
    combineDescription = scrapy.Field()
    id = scrapy.Field()
    localityId = scrapy.Field()
    bathroom = scrapy.Field()
    propertyTitle = scrapy.Field()
    locality = scrapy.Field()
    active = scrapy.Field()
    maintenanceAmount = scrapy.Field()
    weight = scrapy.Field()
    waterSupply = scrapy.Field()
    completeStreetName = scrapy.Field()
    totalFloor = scrapy.Field()
    lift = scrapy.Field()
    deposit = scrapy.Field()
    reactivationSource = scrapy.Field()
    amenities = scrapy.Field()
    shortUrl = scrapy.Field()
    ownerName = scrapy.Field()
    propertyType = scrapy.Field()
    floor = scrapy.Field()
    location = scrapy.Field()
    sharedAccomodation = scrapy.Field()
    isMaintenance = scrapy.Field()
    facingDesc = scrapy.Field()
    facing =  scrapy.Field()
    swimmingPool = scrapy.Field()
    gym = scrapy.Field()
