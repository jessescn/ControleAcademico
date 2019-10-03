import re
from functools import reduce

def print_credits(subjects):
    subjects = list(filter(approved, subjects))
    mandatory = get_mandatory(subjects)
    
    genaral_opt = get_general_optative(subjects)
    specific_opt = get_specific_optative(subjects)
    print("              Créditos\n")
    print("Obrigatórios:           (" + mandatory + "/132)")
    print("Optativos Específicos:  (" + specific_opt + "/40)")
    print("Optativos Gerais:       (" + genaral_opt + "/16)\n")

def get_general_optative(subjects):
    optative = list(filter(general_optative, subjects))
    return get_credits_sum(optative)

def get_specific_optative(subjects):
    optative = list(filter(specific_optative, subjects))
    return get_credits_sum(optative)

def get_mandatory(subjects):
    mand = list(filter(mandatory, subjects))
    return get_credits_sum(mand)

def get_credits_sum(subjects):
    return reduce(sum_credits, subjects, {"creditos": "0"})["creditos"]

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

