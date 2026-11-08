def remove_vowels(text: str) -> str:
    """
    >>>remove_vowels("Hallo")
    "hll"
    >>> remove_vowels("Hello world")
    "Hll
    vowels = "a, e, i, o, u"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    text = input("Geef een zin: ")
    print(remove_vowels(text))
