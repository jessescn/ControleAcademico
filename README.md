# Controle Acadêmico 📚

O objetivo desse crawler é obter os dados  presentes no [Controle Acadêmico](https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/). 

Esse código tem como usuário principal os estudantes da Universidade Federal de Campina Grande (UFCG).

## Comandos

Abaixo estão algumas pequenas explicações acerca dos comandos e seus retornos. Os exemplos abaixo foram baseados em uma exportação no formato JSON, entretanto, você é livre para escolher o formato de exportação desejado.

### Histórico

``` bash
 $ pipenv run controle historico
```

Retorna os dados acerca das disciplinas do histórico acadêmico. Tais dados estão estruturados da seguinte maneira:

``` bash
{
 codigo, # Código de cadastro da disciplina
 disciplina, # Nome da disciplina 
 tipo, # Tipo da disciplina ['Obrigatória', 'Extracurricular', 'Optativa']
 creditos, # Quantidades de créditos da disciplina
 carga_horaria, # A sua carga horária, em horas
 media, # A média do aluno nessa disciplina
 situacao, # A situação do aluno na disciplina ['Aprovado', 'Dispensa', 'Em curso']
 periodo # O período recomendado na qual a disciplina deve ser paga segundo o plano de curso 
}
```

### Horários

``` bash
 $ pipenv run controle horario
```

Retorna as disciplinas e seus respectivos horários e salas de um determinado período letivo. Eles estão estruturados da seguinte maneira:

```bash
{
 codigo, # Código de cadastro da disciplina
 disciplina, # Nome da disciplina
 turma, # Número da turma 
 creditos, # Quantidades de créditos da disciplina
 horarios: [ # Lista dos horários da disciplina 
  {
   dia, # Em formato de números [2,3,4,5,6]
   horario, # Horário da disciplina nesse dia 
   sala # Sala em que acontece a aula 
  },
  ...]
 carga_horaria # A sua carga horária, em horas
}
```


### help

Para saber mais detalhes acerca dos comandos disponíveis, é so digitar o comando abaixo.

``` bash
 $ pipenv run controle [COMANDO] --help
```

## Configuração

Para executar a aplicação, é necessário ter instalado o pip na sua máquina. Você pode verificar se você tem o pip instalado atráves desse comando

``` bash
$ pip --version
```

###  Development version 

Instalando as dependências do projeto

``` bash
# Instalando o gerenciador de dependências
$ pip install --user pipenv

# Instalando as dependências usando o pipenv
$ pipenv install

# Executando a versão development  da CLI  
$ pipenv run controle [COMMAND]
```

### Releasing version

Caso você queira instalar o comando na sua máquina, será necessário ter a versão do pip para python 3

``` bash
# Instalando as dependências da CLI
$ pip3 install --editable --user .

# Executando a CLI em qualquer diretório do sistema
 $ controle [COMMAND]
```

A partir da instalação acima, o comando **controle** fica acessível através do terminal globalmente na sua máquina. 

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

Disclaimer: Obviamente, para ter o acesso ao Controle Acadêmico, é necessário fornecer matricula e senha, entretanto, eu não tenho nenhuma intenção de obter tais informações. Você pode dar uma olhada no código acessando o arquivo run.py
