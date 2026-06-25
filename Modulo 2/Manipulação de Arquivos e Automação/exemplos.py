"""
Biblioteca Python qye permite se comunicar com o protocolo 
HTTP de forma facil e instuitiva.

- Requisiçao
-- Cabeçalhos
-- Corpos

- Resposta
-- Estatus
-- Cabeçalhos
-- Corpo
"""
import requests

cep = input("Digete o cep que deseja cunsultar: ")

resposta = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")

print(resposta.status_code)
if resposta.status_code == 200:
   print(resposta.json())
   dados = resposta.json()
   print(dados.get("address"))
   print(f"{dados.get("city")} — {dados.get("state")}")
else:
   print("CEP invaçido, verifique o CEP e tente novamente.")

