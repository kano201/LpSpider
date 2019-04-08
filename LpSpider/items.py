# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LpspiderItem(scrapy.Item):
    Postname = scrapy.Field()
    Salary = scrapy.Field()
    Location = scrapy.Field()
    Company = scrapy.Field()
    Company_type = scrapy.Field()
    welfare = scrapy.Field()
    Experience = scrapy.Field()
    Education = scrapy.Field()
    pos_id = scrapy.Field()