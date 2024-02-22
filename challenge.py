import json
from collections import defaultdict

def gerar_chave_anagrama(palavra):
    return ''.join(sorted(palavra))

def encontrar_anagramas(array):
    anagramas_dict = defaultdict(list)

    # Agrupar palavras por seus anagramas
    for item in array:
        palavra = item["str"]
        chave_anagrama = gerar_chave_anagrama(palavra)
        anagramas_dict[chave_anagrama].append(palavra)

    # Construir o novo array mantendo a ordem original
    novo_array = []
    anagramas_processados = set()

    for item in array:
        palavra = item["str"]
        chave_anagrama = gerar_chave_anagrama(palavra)
        anagramas = anagramas_dict[chave_anagrama]

        # Adicionar apenas se houver mais de uma palavra no anagrama
        if len(anagramas) > 1 and chave_anagrama not in anagramas_processados:
            novo_array.append({"anagramas": anagramas})
            anagramas_processados.add(chave_anagrama)

    return novo_array

# Ler JSON de um arquivo
with open("json_entrada.json", "r") as arquivo:
    entrada_json = json.load(arquivo)

# Chamar a função com o JSON executado
resultado_json = encontrar_anagramas(entrada_json)

# Ordenar o resultado de acordo com a ordem original do array de entrada
resultado_json = sorted(resultado_json, key=lambda x: entrada_json.index({"str": x["anagramas"][0]}))

# Escrever o resultado em um novo arquivo JSON
with open("json_saida.json", "w") as arquivo_saida:
    json.dump(resultado_json, arquivo_saida, ensure_ascii=False, indent=2)
    
print("O novo arquivo foi criado com sucesso.")