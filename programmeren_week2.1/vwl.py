def remove_vowels(text: str) -> str:
    """
    >>> remove_vowels("just setting up my twitter")
    'jst sttng p my twttr'

    >>> remove_vowels("hallo")
    'hll'

    >>> remove_vowels("AEIOU")
    ''

    >>> remove_vowels("Python")
    'Pythn'

    >>> remove_vowels("aAeEiIoOuU")
    ''
    """
    result = ""

    for char in text:
        if char.lower() not in "aeiou":
            result += char

    return result


if __name__ == "__main__":
    text = input()
    print(remove_vowels(text))