from lesson_21_recursion import tasks


def test_is_palindrome():
    assert not tasks.is_palindrome('Kola')
    assert tasks.is_palindrome('')
    assert tasks.is_palindrome('tenet')
    assert tasks.is_palindrome('radar')
    assert tasks.is_palindrome('radar', index=-1)
