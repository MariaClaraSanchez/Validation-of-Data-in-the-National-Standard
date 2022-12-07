from validate_docbr import CPF, CNPJ

class CPF_CNPJ:
    def __init__(self, documento, tipo_documento) -> None:
        documento = str(documento)
        self.tipo_documento = tipo_documento
        
        if self.tipo_documento == "cpf":
            self.objeto_cpf = CPF()
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            self.objeto_cnpj = CNPJ()
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    # CPF
    def cpf_eh_valido(self, cpf) -> bool:
        if len(cpf) == 11:
            return self.objeto_cpf.validate(cpf)

        raise ValueError("Quantidade de Dígitos Inválida!")
    
    def format_cpf(self) -> str:
        return self.objeto_cpf.mask(self.cpf)
    
    def format_cnpj(self) -> str:
        return self.objeto_cnpj.mask(self.cnpj)
    
    def __str__(self) -> str:
        if self.tipo_documento == "cpf":
            return self.format_cpf()
        elif self.tipo_documento == "cnpj":
            return self.format_cnpj()
        else:
            raise ValueError("Sem tipo válido!!")

    # CNPJ
    def cnpj_eh_Valido(self, cnpj):
            if len(cnpj)==14:
                return self.objeto_cnpj.validate(cnpj)
            else:
                raise ValueError("Quantidade de dígitos inválida!")