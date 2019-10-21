from ..util import credits
import unittest

class GetGeneralOptativesMethodTestCase(unittest.TestCase):
    def setUp(self):
        self.credits = credits

    def test_exists_general_optatives(self):
        sample = [{"codigo": "1109103", "disciplina": "CALCULO DIFERENCIAL E INTEGRAL I", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "8,3", "situacao": "Aprovado", "periodo": "2017.1"},
                            {"codigo": "1411174", "disciplina": "INTRODUÇÃO A COMPUTAÇÃO", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "9,0", "situacao": "Aprovado", "periodo": "2017.1"},
                            {"codigo": "1109035", "disciplina": "ALGEBRA VETORIAL E GEOMETRIA ANALÍTICA", "tipo": "Optativa", "creditos": "4", "carga_horaria": "60", "media": "8,3", "situacao": "Aprovado", "periodo": "2017.1"}]
        
        self.assertEqual(self.credits.get_general_optative(sample), "4", "Incorrect value of optative credits")
        
    def test_empty_subjects(self):
        sample = []
        self.assertEqual(self.credits.get_general_optative(sample), "0", "Empty sample should return 0 credits")

    def test_non_general_optatives(self):
        sample = [{"codigo": "1109049", "disciplina": "ALGEBRA LINEAR I", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "7,2", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1109053", "disciplina": "CALCULO DIFERENCIAL E INTEGRAL II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "6,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411181", "disciplina": "LABORATÓRIO DE PROGRAMAÇÃO II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "9,3", "situacao": "Aprovado", "periodo": "2017.2"}]
    
        self.assertEqual(self.credits.get_general_optative(sample), "0", "Non optative subjects should return 0 credits")


class  GetSpecificOptativeTestCase(unittest.TestCase):
    def setUp(self):
        self.credits = credits

    def test_exists_specific_optatives(self):
        sample = [{"codigo": "1419049", "disciplina": "VISUALIZAÇÃO DE DADOS", "tipo": "Optativa", "creditos": "4", "carga_horaria": "60", "media": "7,2", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1109053", "disciplina": "CALCULO DIFERENCIAL E INTEGRAL II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "6,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411181", "disciplina": "CIÊNCIAS DE DADOS PREDITIVA", "tipo": "Optativa", "creditos": "2", "carga_horaria": "60", "media": "9,3", "situacao": "Aprovado", "periodo": "2017.2"}]

        self.assertEqual(self.credits.get_specific_optative(sample), "6", "Incorrect number of credits")

    def test_empty_subjects(self):
        sample = []

        self.assertEqual(self.credits.get_specific_optative(sample), "0", "empty list of subjects should return 0 credits")

    def test_non_specific_optatives(self):
        sample = [{"codigo": "1109049", "disciplina": "ALGEBRA LINEAR I", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "7,2", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1109053", "disciplina": "CALCULO DIFERENCIAL E INTEGRAL II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "6,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411181", "disciplina": "LABORATÓRIO DE PROGRAMAÇÃO II", "tipo": "Obrigatória", "creditos": "2", "carga_horaria": "60", "media": "9,3", "situacao": "Aprovado", "periodo": "2017.2"}]

        self.assertEqual(self.credits.get_specific_optative(sample), "0", "Non specific optatives should return 0 credits")

    def test_incorrect_optative_code(self):
        sample = [{"codigo": "12", "disciplina": "VISUALIZAÇÃO DE DADOS", "tipo": "Optativa", "creditos": "4", "carga_horaria": "60", "media": "7,2", "situacao": "Aprovado", "periodo": "2017.2"}]
        self.assertEqual(self.credits.get_specific_optative(sample), "0", "Should return 0 credits because optative have incorrect code (don't start with '141')")
        

class GetMandatoryTestCase(unittest.TestCase):
    def setUp(self):
        self.credits = credits

    def test_exists_mandatory_subject(self):
        sample = [{"codigo": "1109053", "disciplina": "CALCULO DIFERENCIAL E INTEGRAL II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "6,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411181", "disciplina": "LABORATÓRIO DE PROGRAMAÇÃO II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "9,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411168", "disciplina": "PROGRAMAÇÃO II", "tipo": "Obrigatória", "creditos": "4", "carga_horaria": "60", "media": "9,1", "situacao": "Aprovado", "periodo": "2017.2"}]
        self.assertEqual(self.credits.get_mandatory(sample), "12", "Incorrect number of credits")

    def test_non_mandatory_subjects(self):
        sample = [{"codigo": "1109113", "disciplina": "MATEMÁTICA DISCRETA", "tipo": "Extracurricular", "creditos": "4", "carga_horaria": "60", "media": "7,3", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411300", "disciplina": "TECC(APLICACOES DE TEORIA DOS GRAFOS)", "tipo": "Extracurricular", "creditos": "2", "carga_horaria": "30", "media": "10,0", "situacao": "Aprovado", "periodo": "2017.2"},
                            {"codigo": "1411170", "disciplina": "TEORIA DOS GRAFOS", "tipo": "Extracurricular", "creditos": "2", "carga_horaria": "30", "media": "9,8", "situacao": "Aprovado", "periodo": "2017.2"}]

        self.assertEqual(self.credits.get_mandatory(sample), "0", "Non mandatory subjects should return 0 credits")

    def test_empty_subjects(self):
        sample = []
        self.assertEqual(self.credits.get_mandatory(sample), "0", "Empty subjects should return 0 credits")

if __name__ == "__main__":
    unittest.main()