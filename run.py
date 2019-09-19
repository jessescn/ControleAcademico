
import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from historico_academico.spiders.controle import ControleSpider

class User(object):

    def __init__(self):
        self.matricula = None
        self.senha = None


pass_user = click.make_pass_decorator(User, ensure=True)

def authentication(user):
    """Recebe os dados de autenticação do usuário"""
    user.matricula = click.prompt('Insira sua matricula', type=str)
    user.senha =  click.prompt('Insira sua senha', hide_input=True, type=str)

@click.group()
def cli():
    """CLI para obter dados do controle acadêmico"""
    pass

@cli.command('historico', short_help="Retorna dados das disciplinas do historico acadêmico.")
@pass_user
def get_subjects(user):
    """ Retorna os dados das disciplinas do aluno disponiveis no controle acadêmico. """
    authentication(user)
    process = CrawlerProcess(settings={
    'FEED_FORMAT': 'json',
    'FEED_URI': 'historico.json',
    'FEED_EXPORT_ENCODING':'utf-8'
    })
    ControleSpider.matricula = user.matricula
    ControleSpider.senha = user.senha
    process.crawl(ControleSpider)
    process.start()

@cli.command('horario', short_help="Retorna os horários das disciplinas.")
@pass_user
def get_schedule(user):
    """Retorna as disciplinas que estão sendo cursadas e seus respectivos horários."""
    authentication(user)
    pass
    
if __name__ == '__main__':
    cli()
