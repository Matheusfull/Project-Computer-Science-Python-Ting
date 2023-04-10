import sys


def txt_importer(path_file):
    path = path_file.split('.')
    if path[1] != 'txt':
        return sys.stderr.write('Formato inválido\n')
    try:
        with open(path_file, mode='r') as file:
            file_lines = file.read().split('\n')
            return file_lines
    except FileNotFoundError:
        return sys.stderr.write(f'Arquivo {path_file} não encontrado\n')


print(txt_importer('matheus.txt'))