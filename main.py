import json
import os

from simple_term_menu import TerminalMenu
from termcolor import colored


def _text_style_1(text: str) -> str:
    return colored(text=text, color='light_cyan', attrs=['bold', 'underline'])


def _header():
    print('\n' + horizontal_align(_text_style_1('BIBLIA SAGRADA')) + '\n\n')


def get_book_list(bible: json) -> list:
    book_list = []
    for book in bible:
        book_list.append(book['name'])
    return book_list


def menu(options: list, title: str) -> int:
    print(_text_style_1(title) + '\n\n')
    terminal_menu = TerminalMenu(
        menu_entries=options,
        menu_cursor_style=['bg_black', 'fg_cyan', 'bold'],
        menu_highlight_style=['bg_black', 'fg_cyan', 'bold', 'underline'],
    )
    return terminal_menu.show()


def main_menu() -> int:
    os.system('clear')
    _header()
    return menu(['[1] Ler Agora (ACF)', '[2] SAIR'], '>> MENU')


def book_menu(bible: json) -> int:
    books = get_book_list(bible)
    # for book_index in range(0, len(books)):
    #     books[book_index] = f'[{book_index + 1}] ' + books[book_index]
    os.system('clear')
    _header()
    return menu(books, '>> LIVROS')


def chapter_menu(book: json) -> int:
    chapters = []
    for chapter_index in range(0, len(book)):
        chapters.append(f'Capítulo {chapter_index + 1}')
    os.system('clear')
    _header()
    return menu(chapters, '>> CAPÍTULOS')


def vertical_align(text: str, lines: int) -> None:
    terminal_height = os.get_terminal_size().lines
    terminal_half_height = int((terminal_height - lines) / 2)
    new_text = ''
    for line in range(0, terminal_height):
        if line == terminal_half_height:
            new_text = new_text + text
            continue
        new_text = new_text + '\n'
    return new_text


def horizontal_align(text: str) -> str:
    return text.center(os.get_terminal_size().columns)


if __name__ == '__main__':

    option = main_menu()

    if option == 0:
        manuscripts = open(
            os.path.join(os.getcwd(), 'biblia', 'json', 'acf.json'), 'r'
        )
        bible = json.load(manuscripts)
        book_index = book_menu(bible)
        book = bible[book_index]
        chapter_index = chapter_menu(book)
        chapter = book['chapters'][chapter_index]

        os.system('clear')
        print('\n' + horizontal_align(_text_style_1(book['name'])) + '\n')
        print(
            horizontal_align(_text_style_1(f'Capítulo {chapter_index + 1}'))
            + '\n'
        )

        for counter in range(0, len(chapter)):
            verse = chapter[counter]
            print(
                '',
                colored(
                    f'{counter + 1}',
                    color='light_cyan',
                    attrs=['bold', 'underline'],
                ),
                '-',
                verse,
            )
        print('\n\n')

    if option == 1:
        exit()