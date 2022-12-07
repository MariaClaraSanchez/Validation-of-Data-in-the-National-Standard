from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def create_doc(documento):
        len_doc = len(documento)
        if len_doc == 11:
            return DocCPF(documento)
        elif len_doc == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError("Quantidade de Dígitos do documento está incorreta!!")

class DocCPF:
    
    def __init__(self,docummento):
        self.obj_cpf = CPF()

        if self.valida(docummento):
            self.cpf = docummento
        else:
            raise ValueError("CPF inválido!!")
    
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        return self.obj_cpf.validate(documento)
    
    def format(self):
        return self.obj_cpf.mask(self.cpf)


class DocCNPJ:
    
    def __init__(self,docummento):
        self.obj_cnpj = CNPJ()

        if self.valida(docummento):
            self.CNPJ = docummento
        else:
            raise ValueError("Cnpj inválido!!")
    
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        return self.obj_cnpj.validate(documento)
    
    def format(self):
        return self.obj_cnpj.mask(self.CNPJ)
        