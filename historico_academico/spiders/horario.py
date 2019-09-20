# -*- coding: utf-8 -*-
import scrapy
from historico_academico.items import HorarioItem

def authentation_failed(response):
    """ Função para checar se a autenticação falhou """
    return response.css('div.alert p::text').get() == 'Erro'

class HorarioSpider(scrapy.Spider):
    """Spider dos Horários

    Scrapy responsável por acessar o controle
    acadêmico a partir da matricula e senha
    fornecidos pelo usuário e buscar os horários
    das disciplinas de um determinado semestre. 
    """
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
        """Callback responsável por extrair as informações

        O método recebe a response e extrai os dados
        referentes aos horários das disciplinas, incluin-
        do dados como codigo, salas, dias, horários, nome,
        dentre outros.
        """
        table = response.xpath('//table[@class="table table-bordered table-striped table-condensed"]/tbody/tr')
        
        for line in table:
            data = line.xpath('./td//text()').getall()
            subject_schedules = []

            for i in range(4, len(data) - 1):
                values = data[i].replace('\r\n', '' ).split()
                schedule_pair = {
                    "dia":values[0],
                    "horario": values[1],
                    "sala": values[2].replace('(', '').replace(')', '')
                } 
                subject_schedules.append(schedule_pair)
            
            subject = data[1].replace('\r\n', '' ).split('-')
            
            schedule = HorarioItem(
                                codigo=subject[0],
                                disciplina=subject[1],
                                creditos=data[2],
                                carga_horaria=data[3],
                                turma=data[0],
                                horarios=subject_schedules)

            yield schedule
            
