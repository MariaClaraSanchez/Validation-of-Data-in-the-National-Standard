from classes.documento import Documento
from classes.cels_br import CEL
from classes.date import DATES
from classes.acesso_cep import BuscaEndereco

import re
import requests

if __name__ == "__main__":

    cep = "01001000"
    objeto_cep = BuscaEndereco(cep)
    
    bairro, cidade, uf = objeto_cep.acessar_via_cep()

    print(f"Bairro: {bairro}, cidade: {cidade}, UF: {uf}")

    #r = requests.get(f'https://viacep.com.br/ws/01001000/json/')
    #print(r.text)





    # cadastro = DATES()
    # print(cadastro.tempo_cadastro())

 
    #texto = "o número que eu escolhi para meu cel é 35998983333, e tbm o 1989892345"
    # telefone = "552126481234"
    # telefone_objeto = CEL(telefone)

    # print(telefone_objeto)

    # exemplo_cnpj = "35379838000112"
    # documento = Documento.create_doc(exemplo_cnpj)
    # print(documento)