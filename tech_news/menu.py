import sys
from datetime import date
import tech_news.analyzer.ratings as ratings
import tech_news.analyzer.search_engine as search
import tech_news.scraper as scraper


def show_menu():
    input(
        """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""",
    )


def num_news():
    command = input("Digite quantas notícias serão buscadas:")
    scraper.get_tech_news(command)


def search_news():
    command = input("Digite o título:")
    search.search_by_title(command)


def src_by_date():
    command = input("Digite a data no formato aaaa-mm-dd:")
    search.search_by_date(date(command))


def src_by_tag():
    command = input("Digite a tag:")
    search.search_by_tag(command)


def src_by_cat():
    command = input("Digite a categoria:")
    search.search_by_category(command)


def analyzer_menu():
    show_menu()
    _, path, args = sys.argv
    try:
        command = dict({
            '0': search_news,
            '1': num_news,
            '2': src_by_date,
            '3': src_by_tag,
            '4': src_by_cat,
            '5': ratings.top_5_news,
            '6': ratings.top_5_categories,
            '7': sys.stdout.write("Encerrando script\n"),
        })
        if path not in command or path == "":
            raise KeyError
        command[path]
    except KeyError:
        sys.stderr.write("Opção inválida\n")
# path do sys.argv, controle somente do comando tech-news-analyzer?
#       preciso de outros args? necessário apenas pra teste no terminal?
# + outros erros
