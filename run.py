
import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from historico_academico.spiders.historico import HistoricoSpider 

class User(object):

    def __init__(self):
        self.matricula = None
        self.senha = None

pass_user = click.make_pass_decorator(User, ensure=True)

def authentication(user):
    """Recebe os dados de autenticação do usuário"""
    user.matricula = click.prompt('\nInsira sua matricula', type=str)
    user.senha =  click.prompt('Insira sua senha', hide_input=True, type=str)

def file_configs():
    """Recebe os dados referentes ao arquivo destino dos dados"""
    file_name = click.prompt('\nQual será nome arquivo do arquivo?', default="dados")
    file_extension = click.prompt('Qual será o formato do arquivo?', default="json")
    return [ file_name , file_extension ]

@click.group()
def cli():
    """CLI para obter dados do controle acadêmico"""
    pass

@cli.command('historico', short_help="Retorna dados das disciplinas do historico acadêmico.")
@pass_user
def get_subjects(user):
    """ Retorna os dados das disciplinas do aluno disponiveis no controle acadêmico. """
    authentication(user)
    [ file_name, file_extension ] = file_configs()

    process = CrawlerProcess(settings={
    'FEED_FORMAT': file_extension,
    'FEED_URI': file_name + '.' + file_extension,
    'FEED_EXPORT_ENCODING':'utf-8',
    'LOG_ENABLED': False
    })

    HistoricoSpider.matricula = user.matricula
    HistoricoSpider.senha = user.senha
    process.crawl(HistoricoSpider)
    process.start()

@cli.command('horario', short_help="Retorna os horários das disciplinas.")
@pass_user
def get_schedule(user):
    """Retorna as disciplinas que estão sendo cursadas e seus respectivos horários."""
    pass
    
if __name__ == '__main__':
    cli()
