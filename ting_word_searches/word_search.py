def exists_word(word, instance):
    # 1 - vou passar por cada instanciação, que nesse caso
    # é cada "arquivo" lido
    # 2 - agora vamos passar por cada linha e verificar se há
    # a palavra procurada.
    data = []
    for index in range(len(instance)):
        occurences = []
        dict_lines = instance.search(index)
        for i, line in enumerate(dict_lines["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                occurences.append({"linha": i + 1})
        if occurences:
            data.append({
                "palavra": word,
                "arquivo": dict_lines["nome_do_arquivo"],
                "ocorrencias": occurences
            })
    return data


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
