
import os, stat
import json
import click
from scrapy.crawler import CrawlerProcess
from scraper.spiders.historico import HistoricoSpider
from scraper.spiders.horario import HorarioSpider
from util.credits import print_credits

class User(object):

    def __init__(self):
        self.matricula = None
        self.senha = None

pass_user = click.make_pass_decorator(User, ensure=True)

@pass_user
def authentication(user):
    """Recebe os dados de autenticação do usuário"""
    try:
        home = os.path.expanduser('~')
        file_path = '{}/controleAcademico/user.json'.format(home)
        file = open(file_path, "r")
        student = json.loads(file.read())
        user.matricula = student["matricula"]
        user.senha = student["senha"]
    except:
        user.matricula = click.prompt('\nInsira sua matricula', type=str)
        user.senha = click.prompt('Insira sua senha', hide_input=True, type=str)

def setup_process():
    """Retorna o processo que executará o Spider"""
    [file_name, file_extension] = file_config()

    process = CrawlerProcess(settings={
        'FEED_FORMAT': file_extension,
        'FEED_URI': file_name,
        'FEED_EXPORT_ENCODING':'utf-8',
        'LOG_ENABLED': False
    })
    return process

def file_config():
    """Recebe os dados referentes ao arquivo destino dos dados"""
    file_name = click.prompt('\nQual será nome do arquivo?', default="dados")
    file_extension = click.prompt('Qual será o formato do arquivo?', default="json")
    file = '{}.{}'.format(file_name, file_extension)
    file_path = '{}/controleAcademico/data/{}'.format(os.path.expanduser('~'), file)

    return [file_path, file_extension]

@click.group()
def cli():
    """CLI para obter dados do controle acadêmico"""
    pass

@cli.command('historico', short_help="Retorna dados das disciplinas do historico acadêmico.")
@pass_user
def get_subjects(user):
    """ Retorna os dados das disciplinas do aluno disponiveis no controle acadêmico. """
    authentication()
    process = setup_process()
    process.crawl(HistoricoSpider, matricula=user.matricula, senha=user.senha)
    process.start()

@cli.command('horario', short_help="Retorna os horários das disciplinas.")
@pass_user
def get_schedule(user):
    """Retorna as disciplinas que estão sendo cursadas e seus respectivos horários."""
    authentication()

    periodo = click.prompt('\nPeríodo', default="2019.1", type=str)
    ano = periodo.split('.')[0]
    semestre = periodo.split('.')[1]

    process = setup_process()
    process.crawl(HorarioSpider, matricula=user.matricula, senha=user.senha, ano=ano, semestre=semestre)
    process.start()

@cli.command('colacao', short_help="Retorna a situação atual dos creditos para colação de grau")
@pass_user
def get_degree_collation(user):
    """Retorna uma visualização da situação do aluno em relação
    a quantidade de créditos pagos e faltantes para colação de grau.
    A quantidade de créditos no curso de CC são:\n
    Obrigatórias: 132 créditos\n
    Optativas específicas: 40 créditos\n
    Optativas gerais: 16 créditos\n
    PTCC + TCC: 8 créditos"""
    authentication()
    process = CrawlerProcess({'LOG_ENABLED':False})
    process.crawl(HistoricoSpider, matricula=user.matricula, senha=user.senha)
    process.start()
    print_credits(HistoricoSpider.items)


def get_credentials_file():
    """Retorna o objeto file referente as credenciais do aluno"""
    home = os.path.expanduser('~')
    file_path = home + "/controleAcademico/user.json"

    try:
        open(file_path, "w+")
    except:
        os.mkdir(home + '/controleAcademico')
        os.mkdir(home + '/controleAcademico/data')

    file = open(file_path, "w+")
    os.chmod(file_path, stat.S_IRWXU)

    return file

@cli.command('credenciais', short_help="Armazena as credenciais do aluno")
def store_user():
    """Guarda as credenciais do aluno para futuras requisições
    """
    file = get_credentials_file()
    user = click.prompt('\nInsira sua matricula', type=str)
    senha = click.prompt('Insira sua senha', hide_input=True, type=str)

    file.write(json.dumps({"matricula": user, "senha": senha}))
    file.close()

    print('\nCredenciais salvas!\n')

if __name__ == '__main__':
    cli()
