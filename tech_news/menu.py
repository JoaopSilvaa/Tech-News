import sys


# Requisito 12
def analyzer_menu():
    answer = True
    while answer != "7":
        print("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")
        answer = input()
        if answer == "0":
            print("Digite quantas notícias serão buscadas:")
            break
        elif answer == "1":
            print("Digite o título:")
            break
        elif answer == "2":
            print("Digite a data no formato aaaa-mm-dd:")
            break
        elif answer == "3":
            print("Digite a tag:")
            break
        elif answer == "4":
            print("Digite a categoria:")
            break
        elif answer == "7":
            print("bye")
        else:
            print("Opção inválida", file=sys.stderr)
            break
