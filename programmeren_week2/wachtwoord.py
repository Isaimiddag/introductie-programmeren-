def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    """
    if password < 8:
        return True
    else:
        return False

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """
    for letter in password:
        if letter.isdigit

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
    """
    if check_length = True and check_number = True and check_letter = True:
        return True 

if __name__ == '__main__':
    wachtwoord = input("Wat is uw wachtwoord? ")
    check = check_password(wachtwoord)
    if check = True:
        print("Uw wachtwoord is valide.")
    else:
        print("Uw wachtwoord is niet valide.")