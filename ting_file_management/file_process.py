from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    # 1 - instancia a classe para fazer o enfileiramento
    # 2 - com o endereço, eu uso a função do req 2 e
    # separo cada linha em dicionários
    # 3 - Faço a  verificação se aquele endereço já foi usado
    # 4 - pego os dicionários e enfilero
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    lines = txt_importer(path_file)
    dict_of_lines = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    instance.enqueue(dict_of_lines)
    sys.stdout.write(str(dict_of_lines))
    return dict_of_lines


def remove(instance):
    if len(instance.queue) == 0:
        sys.stdout.write(str("Não há elementos\n"))
        return  # 340 dias para descobrir que tinha que colocar
# esse return a fim de parar a função.

    first_queue = instance.dequeue()
    path_first_queue = first_queue["nome_do_arquivo"]
    sys.stdout.write(f'Arquivo {path_first_queue} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
