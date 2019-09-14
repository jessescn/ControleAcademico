# -*- coding: utf-8 -*-
import scrapy
from getpass import getpass
import os

def authentation_failed(response):
    return response.css('div.alert p::text').get() == 'Erro'

class ControleSpider(scrapy.Spider):
    name = 'controle'
    start_urls = ['https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=Home']

    def parse(self, response):
        print('\n--------------- AUTENTICAÇÃO ---------------\n')
        matricula = input('Insira sua matrícula: ')
        senha = getpass('Digite sua senha: ')
        return scrapy.FormRequest.from_response(
            response,
            formdata={'login': str(matricula), 'senha':senha},
            callback=self.after_login
        )

    def after_login(self, response):
        if not authentation_failed(response):
            yield scrapy.Request(response.urljoin('?command=AlunoHistorico'), callback=self.get_subjects)
        else:
            print('\nCredenciais inválidas!\n')
            os.remove('historico.csv')

    def get_subjects(self, response):
            table = response.xpath('//table[@class="table table-bordered"]/tbody/tr')
            for tr in table:
                data  = tr.xpath('./td//text()').getall()
                sub_register = data[0]
                sub_name = data[1]
                sub_type = data[2]
                sub_credits = data[3]
                sub_workload = data[4]
                sub_mean = data[5].strip().split('/n')[0]
                sub_status = data[6]
                sub_period = data[7]

                yield  {
                    "Código": sub_register,
                    "Disciplina": sub_name,
                    "Tipo": sub_type,
                    "Créditos": sub_credits,
                    "Carga horária": sub_workload,
                    "Média": sub_mean,
                    "Situação": sub_status,
                    "Período": sub_period
                }
