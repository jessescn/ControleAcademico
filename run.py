
import click
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from historico_academico.spiders.controle import ControleSpider

@click.group()
def cli():
    """Método que agrupa os comandos da CLI"""
    pass


@cli.command('historico', short_help="Retorna dados das disciplinas do historico acadêmico.")
@click.option('--matricula', prompt=True, type=str)
@click.option('--password', prompt=True, hide_input=True)
def get_subjects(matricula, password):
    """ Retorna os dados das disciplinas do aluno disponiveis no controle acadêmico. """
    process = CrawlerProcess(get_project_settings())
    ControleSpider.matricula = matricula
    ControleSpider.senha = password
    process.crawl(ControleSpider)
    process.start()
    

if __name__ == '__main__':
    cli()
