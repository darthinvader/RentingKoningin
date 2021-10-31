# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundaItem(scrapy.Item):
    link = scrapy.Field()

    photos = scrapy.Field()

    address1 = scrapy.Field()
    street = scrapy.Field()

    livingArea = scrapy.Field()
    bedrooms = scrapy.Field()

    description = scrapy.Field()

    price = scrapy.Field()
    deposit = scrapy.Field()
    rentalAgreement = scrapy.Field()
    listedSince = scrapy.Field()
    status = scrapy.Field()
    acceptance = scrapy.Field()

    typeApartment = scrapy.Field()
    buildingType = scrapy.Field()
    yearOfConstruction = scrapy.Field()

    numberOfRooms = scrapy.Field()
    numberOfBathrooms = scrapy.Field()
    bathroomFacilities = scrapy.Field()

    insulation = scrapy.Field()

    balconyRoofGarden = scrapy.Field()

    storageSpace = scrapy.Field()
    facilities = scrapy.Field()

    last_updated = scrapy.Field(serializer=str)
