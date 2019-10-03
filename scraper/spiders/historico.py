"""Arquivo responsável por conter o Spider
    referente ao historico academico e suas funções auxiliares
"""
import scrapy
from scraper.items import DisciplinaItem

def authentation_failed(response):
    """ Função para checar se a autenticação falhou """
    return response.css('div.alert p::text').get() == 'Erro'

class HistoricoSpider(scrapy.Spider):
    """Spider dp Histórico Acadêmico

    Spider responsável por acessar o controle
    a partir da matricula e senha fornecidos pelo
    usuário, para obter os dados das disciplinas
    pagas pelo mesmo presentes no histórico.
    """
    name = 'historico'
    start_urls = ['https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=Home']
    items = []

    def __init__(self, matricula=None, senha=None):
        self.matricula = matricula
        self.senha = senha

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
            yield scrapy.Request(response.urljoin('?command=AlunoHistorico'),
                                                     callback=self.get_subjects)

            print('\nDados obtidos com sucesso!\n')
        else:
            print('\nCredenciais inválidas!\n')


    def get_subjects(self, response):
        """ Callback da página do histórico

        O método é chamado quando ao receber os
        dados da requisição a pagina do historico
        acadêmico. Ao receber a página, ele varre a tabela
        contendo as disciplinas, pegando os dados.
        """
        table = response.xpath('//table[@class="table table-bordered"]/tbody/tr')
        for line in table:
            data = line.xpath('./td//text()').getall()

            subject = DisciplinaItem(
                                codigo=data[0],
                                disciplina=data[1],
                                tipo=data[2],
                                creditos=data[3],
                                carga_horaria=data[4],
                                media=data[5].strip().split('/n')[0],
                                situacao=data[6],
                                periodo=data[7])
            self.items.append(subject)

            yield  subject
