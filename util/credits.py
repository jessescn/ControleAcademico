import re
from functools import reduce

def print_credits(subjects):
    lista = list(filter(approved, subjects))
    mandatory = get_mandatory(lista)
    
    genaral_opt = get_general_optative(lista)
    specific_opt = get_specific_optative(lista)
    print("              Créditos\n")
    print("Obrigatórios:           (" + mandatory + "/132)")
    print("Optativos Específicos:  (" + specific_opt + "/40)")
    print("Optativos Gerais:       (" + genaral_opt + "/16)\n")

def get_general_optative(subjects):
    optativas = list(filter(general_optative, subjects))
    return reduce(sum_credits, optativas)["creditos"]

def get_specific_optative(subjects):
    optativas = list(filter(specific_optative, subjects))
    return reduce(sum_credits, optativas)["creditos"]

def sum_credits(subject1, subject2):
  return {"creditos": str(int(subject1['creditos']) + int(subject2['creditos']))}

def approved(subject):
  return subject['situacao'] == 'Aprovado' or subject['situacao'] == 'Dispensa'

def mandatory(subject):
  return subject['tipo'] == 'Obrigatória'

def general_optative(subject):
  return subject['tipo'] == 'Optativa' and not(re.search("\A141",subject['codigo']))

def specific_optative(subject):
  return subject['tipo'] == 'Optativa' and (re.search("\A141",subject['codigo']))

def get_mandatory(subjects):
    mand = list(filter(mandatory, subjects))
    return reduce(sum_credits, mand)["creditos"]