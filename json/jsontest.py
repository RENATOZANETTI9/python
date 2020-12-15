import json
dados = {"nome": "Rernato Zanetti Gomes", "profissao": "Desenvolvedor Senior"}

with open("dados.json","w") as json_file:
    json.dump(dados,json_file,indent=4)

with open("dados.json","r") as json_file_read:
    dados_json = json.load(json_file_read)

print(dados_json)        