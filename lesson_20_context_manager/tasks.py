total = 1


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) <= 1:
        return True
    if index == len(looking_str) // 2:
        return True

    return looking_str[index] == looking_str[-(index + 1)] and \
           is_palindrome(looking_str, index + 1)


print(
    is_palindrome('Kola')
)