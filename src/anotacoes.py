# Exemplo de e-mail com Regex
import re
padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc maria234@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta.group())