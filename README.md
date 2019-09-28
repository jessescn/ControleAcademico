# Controle Acadêmico 📚

O objetivo desse crawler é obter os dados  presentes no [Controle Acadêmico](https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/). 

Esse código tem como usuário principal os estudantes da Universidade Federal de Campina Grande (UFCG).

## Comandos

Para saber mais detalhes acerca dos comandos disponíveis, é so digitar o comando abaixo.

``` bash
 $ pipenv run controle [COMANDO] --help
```

## Configuração

Para executar a aplicação, é necessário ter instalado o pip na sua máquina. Você pode verificar se você tem o pip instalado atráves desse comando

``` bash
$ pip --version
```

Instalando as dependências do projeto

``` bash
# Instalando o gerenciador de dependências
$ pip install --user pipenv

# Instalando as dependências usando o pipenv
$ pipenv install

# Executando a CLI
$ pipenv run controle [COMMAND]
```

## Estrutura

``` bash

scraper/
   |_ spiders/
        |_ historico.py
        |_ horario.py
   |_ items.py
   |_ middlewares.py
   |_ pipelines.py
   |_ settings.py

data/

run.py

```

## Contribuição

Fique livre para sugerir melhorias, abrir issues e PRs :). 

Obs: Obviamente, para ter o acesso ao Controle Acadêmico, é necessário fornecer matricula e senha, entretanto, eu não tenho nenhuma intenção de obter tais informações. Você pode dar uma olhada no código acessando o arquivo run.py
