import sys
from tech_news.scraper import (
    get_tech_news,
)
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import (
    top_5_news,
    top_5_categories
)


def answer_0():
    answer2 = int(input("Digite quantas notícias serão buscadas:"))
    print(answer2)
    get_tech_news(answer2)


def answer_1():
    answer2 = input("Digite o título:")
    result = search_by_title(answer2)
    print(result)


def answer_2():
    answer2 = input("Digite a data no formato aaaa-mm-dd:")
    result = search_by_date(answer2)
    print(result)


def answer_3():
    answer2 = input("Digite a tag:")
    result = search_by_tag(answer2)
    print(result)


def answer_4():
    answer2 = input("Digite a categoria:")
    result = search_by_category(answer2)
    print(result)


def answer_5():
    result = top_5_news()
    print(result)


def answer_6():
    result = top_5_categories()
    print(result)


def answer_7():
    print("Encerrando script")


def invalid_answer():
    print("Opção inválida", file=sys.stderr)


# Requisito 12
def analyzer_menu():
    answer = ""
    answers = ["0", "1", "2", "3", "4", "5", "6", "7"]
    functions = [
            answer_0, answer_1, answer_2,
            answer_3, answer_4, answer_5,
            answer_6, answer_7
        ]
    try:
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
            if answer in answers:
                function = functions[int(answer)]
                function()
                break
            else:
                invalid_answer()
                break
    except ValueError:
        print("Opção inválida", file=sys.stderr)
