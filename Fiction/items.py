# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FictionItem(scrapy.Item):
    # define the fields for your item here like:
    #小说名称
    name = scrapy.Field()
    #小说章节名字
    chapter_name = scrapy.Field()
    #小说章节内容
    chapter_content = scrapy.Field()

