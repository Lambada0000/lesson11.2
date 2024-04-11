def large_letters(word):
    """Функция возвращает слово из заглавных букв"""
    return word.upper()


def capital_letter(word):
    """Функция возвращает слово с первой заглавной буквой"""
    word = ' '.join(word.capitalize() for word in word.split())
    return word
