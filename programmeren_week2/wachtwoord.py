def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.

    >>> check_length("abc")
    False
    >>> check_length("abcdefgh")
    True
    """
    if len(password) >= 8:
        return True
    else:
        return False

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.

    >>> check_letter("abc")
    False
    >>> check_letter("ABC")
    False
    >>> check_letter("Abc")
    True
    """
    heeft_hoofdletter = False
    heeft_kleine_letter = False

    for letter in password:
        if letter.isupper():
            heeft_hoofdletter = True
        elif letter.islower():
            heeft_kleine_letter = True

    return heeft_hoofdletter and heeft_kleine_letter

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.

    >>> check_number("abc")
    False
    >>> check_number("abc1")
    True
    """
    for letter in password:
        if letter.isdigit():
            return True
            
    return False

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
    """
    return (
        check_letter(password),
        check_number(password),
        check_length(password)
        )

if __name__ == '__main__':
    wachtwoord = input("Wat is uw wachtwoord? ")
    if check_password(wachtwoord):
        print("Uw wachtwoord is valide.")
    else:
        print("Uw wachtwoord is niet valide.")