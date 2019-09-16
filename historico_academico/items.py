# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DisciplinaItem(scrapy.Item):
    # define the fields for your item here like:
    codigo = scrapy.Field()
    disciplina = scrapy.Field()
    tipo = scrapy.Field()
    creditos = scrapy.Field()
    carga_horaria = scrapy.Field()
    media = scrapy.Field()
    situacao = scrapy.Field()
    periodo = scrapy.Field()

    pass
