def longest_word_from_list(lst: list[str]) -> str:
      """
    Geeft het langste woord uit een lijst terug.

    >>> longest_word_from_list(["hond", "kat", "olifant"])
    'olifant'

    >>> longest_word_from_list(["fiets", "auto", "trein"])
    'fiets'

    >>> longest_word_from_list(["abc"])
    'abc'

    >>> longest_word_from_list(["a", "ab", "abc", "abcd"])
    'abcd'

    >>> longest_word_from_list(["pizza", "pasta", "salade"])
    'salade'
    """
    langste = lst[0]
    for word in lst:
        if len(word) > len(langste):
            langste = word
    return langste

def print_banner(lst: list[str]) -> str:
    
    aantal_hekjes = longest_word_from_list(lst)
    banner = "#" * len(aantal_hekjes)
    print(banner)
    for woord in lst:
        print(woord)
    print(banner)
    
def string_to_list(words: str) -> list[str]:
    lijst = []
    huidig_woord = ""
    for char in words:
        if char != " ":
            huidig_woord += char
        else:
            lijst.append(huidig_woord)
            huidig_woord = ""
    lijst.append(huidig_woord)
    return lijst
    
        
    
if __name__ == "__main__":
    banner = input("Geef wat woorden: ")

    woordenlijst = string_to_list(banner)

    print_banner(woordenlijst)