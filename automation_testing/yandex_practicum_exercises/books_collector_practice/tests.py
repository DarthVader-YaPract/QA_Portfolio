import pytest

from main import BooksCollector


@pytest.mark.parametrize('name', ['Дюна', 'К' * 40])
def test_add_new_book_valid_name_adds_once_without_genre(name):
    collector = BooksCollector()

    collector.add_new_book(name)

    assert collector.books_genre[name] == ''

    collector.set_book_genre(name, 'Фантастика')
    collector.add_new_book(name)

    assert collector.books_genre[name] == 'Фантастика'


@pytest.mark.parametrize('name', ['', 'К' * 41])
def test_add_new_book_invalid_name_does_not_add_book(name):
    collector = BooksCollector()

    collector.add_new_book(name)

    assert name not in collector.books_genre


@pytest.mark.parametrize(
    'book_exists, genre, expected_genre',
    [
        (True, 'Фантастика', 'Фантастика'),
        (True, 'Приключения', ''),
        (False, 'Фантастика', None),
    ],
)
def test_set_book_genre_sets_only_allowed_genre_for_existing_book(
    book_exists,
    genre,
    expected_genre,
):
    collector = BooksCollector()
    book_name = 'Дюна'
    if book_exists:
        collector.add_new_book(book_name)

    collector.set_book_genre(book_name, genre)

    assert collector.books_genre.get(book_name) == expected_genre


@pytest.mark.parametrize(
    'name, expected_genre',
    [('Дюна', 'Фантастика'), ('Неизвестная книга', None)],
)
def test_get_book_genre_returns_genre_or_none(name, expected_genre):
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')

    assert collector.get_book_genre(name) == expected_genre


def test_get_books_with_specific_genre_returns_only_matching_books():
    collector = BooksCollector()
    books = {
        'Дюна': 'Фантастика',
        'Солярис': 'Фантастика',
        'Оно': 'Ужасы',
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

    result = collector.get_books_with_specific_genre('Фантастика')

    assert result == ['Дюна', 'Солярис']


def test_get_books_genre_returns_current_books_dictionary():
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.set_book_genre('Дюна', 'Фантастика')

    result = collector.get_books_genre()

    assert result == {'Дюна': 'Фантастика'}


def test_get_books_for_children_excludes_age_rated_and_unset_genres():
    collector = BooksCollector()
    books = {
        'Винни-Пух': 'Мультфильмы',
        'Двенадцать стульев': 'Комедии',
        'Оно': 'Ужасы',
        'Шерлок Холмс': 'Детективы',
    }
    for name, genre in books.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    collector.add_new_book('Книга без жанра')

    result = collector.get_books_for_children()

    assert result == ['Винни-Пух', 'Двенадцать стульев']


def test_add_book_in_favorites_adds_existing_book_only_once():
    collector = BooksCollector()
    collector.add_new_book('Дюна')

    collector.add_book_in_favorites('Дюна')
    collector.add_book_in_favorites('Дюна')
    collector.add_book_in_favorites('Неизвестная книга')

    assert collector.favorites == ['Дюна']


def test_delete_book_from_favorites_removes_selected_book():
    collector = BooksCollector()
    for name in ('Дюна', 'Солярис'):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)

    collector.delete_book_from_favorites('Дюна')

    assert collector.favorites == ['Солярис']


def test_get_list_of_favorites_books_returns_current_favorites():
    collector = BooksCollector()
    collector.add_new_book('Дюна')
    collector.add_book_in_favorites('Дюна')

    result = collector.get_list_of_favorites_books()

    assert result == ['Дюна']
