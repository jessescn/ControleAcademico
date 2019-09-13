# Controle Acadêmico 📚

O objetivo desse crawler é obter os dados referentes as disciplinas presentes no histórico acadêmico do estudante no [_Controle Acadêmico_]('https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/). 

Esse código tem como usuário principal os estudantes da Universidade Federal de Campina Grande (UFCG).

## Configuração

Para instalar as dependências do projeto, é necessário ter instalado o [pipenv]('https://docs.pipenv.org/en/latest/install/'). Após a instalação, você so precisa executar esses dois comandos dentro da pasta do projeto.

``` bash
# Instalando as dependências usando o pipenv
$ pipenv install

# Executando o crawler e baixando as informações
$ pipenv run historico
```

Obs: Obviamente, para ter o acesso ao Controle Acadêmico, é necessário fornecer matricula e senha, entretanto, eu não tenho nenhuma intenção de obter tais informações. Você pode dar uma olhada no código acessando /historic_academic/spiders/controle.py. 
