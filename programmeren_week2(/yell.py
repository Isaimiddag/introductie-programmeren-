def yell(text: str) -> str:
    """
    >>> yell("Hallo!")
    'Hallo!!'

    >>> yell("Wat?")
    'Wat??'

    >>> yell("Cringe? CRINGE!")
    'Cringe?? CRINGE!!'

    >>> yell("Geen speciale tekens")
    'Geen speciale tekens'

    >>> yell("!?")
    '!!??'
    """
    result = ""

    for char in text:
        if char == "!":
            result += "!!"
        elif char == "?":
            result += "??"
        else:
            result += char

    return result


if __name__ == "__main__":
    text = input()
    print(yell(text))
    