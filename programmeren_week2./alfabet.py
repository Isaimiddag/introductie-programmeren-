def compare(word1: str, word2: str) -> int:
    """
    >>> compare("aap", "banaan")
    -1
    >>> compare("banaan", "appel")
    1
    >>> compare("fiets", "auto")
    1
    >>> compare("trein", "banaan")
    1
    >>> compare("Amanda", "amanda")
    0
    """
    i = 0

    while i < len(word1) and i < len(word2):
        letter1 = word1[i].lower()
        letter2 = word2[i].lower()

        if letter1 < letter2:
            return -1
        elif letter1 > letter2:
            return 1

        i += 1

    if len(word1) < len(word2):
        return -1
    elif len(word1) > len(word2):
        return 1
    else:
        return 0


if __name__ == '__main__':
    woord1 = input("Woord 1: ")
    woord2 = input("Woord 2: ")

    resultaat = compare(woord1, woord2)

    if resultaat == -1:
        print(f"{woord1} first")
    elif resultaat == 1:
        print(f"{woord2} first")
    else:
        print("No need to decide!")
