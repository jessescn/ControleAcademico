# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv
class HistoricoAcademicoPipeline(object):

    def open_spider(self, spider):
        self.file = open('historico.csv', 'w')
        field_names = ['codigo','disciplina','tipo','creditos','carga_horaria','media','situacao','periodo']
        self.writer =  csv.DictWriter(self.file, fieldnames=field_names)
        self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(dict(item))
        return item

    def close_spider(self, spider):
        self.file.close()