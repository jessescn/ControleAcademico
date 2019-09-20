# -*- coding: utf-8 -*-
import scrapy

def authentation_failed(response):
    """ Função para checar se a autenticação falhou """
    return response.css('div.alert p::text').get() == 'Erro'

class HorarioSpider(scrapy.Spider):
    name = 'horario'
    start_urls = ['https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=Home']

    def __init__(self, matricula=None, senha=None, semestre=1, ano=2019):
        self.matricula = matricula
        self.senha = senha
        self.semestre = semestre
        self.ano = ano

    def parse(self, response):
        """ Callback default da requisição as URLs presentes no array 'start_urls """
        return scrapy.FormRequest.from_response(
            response,
            formdata={'login': self.matricula, 'senha':self.senha},
            callback=self.after_login
        )

    def after_login(self, response):
            """ Callback da página de login

            O método recebe a response e chama
            o authentication_falied para checar se
            os dados do login eram válidos.
            """
            if not authentation_failed(response):
                yield scrapy.Request(response.urljoin('?command=AlunoHorarioConfirmar&ano={}&periodo={}'.format(self.ano, self.semestre)),
                                                        callback=self.get_schedules)

                print('\nDados obtidos com sucesso!\n')
            else:
                print('\nCredenciais inválidas!\n')

    def get_schedules(self, response):
        table = response.xpath('//table[@class="table table-bordered table-striped table-condensed"]/tbody/tr')
        
        for line in table:
            data = line.xpath('./td//text()').getall()
             
            turma = data[0]
            codigo = data[1]
            nome = data[2]
            creditos = data[3]
            horas = data[4]
            horarios = []

            for i in range(4, len(data) - 1):
                sala_horario = {
                    "horario": data[i].split(' ')[1],
                    "sala": data[i].split(' ')[2].replace('(', '').replace(')', '')
                } 
                horarios.append(sala_horario)

            
