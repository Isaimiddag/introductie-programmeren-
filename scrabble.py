POINTS = [
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
    1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.

    >>> compute_score("a")
    1
    >>> compute_score("cat")
    5
    >>> compute_score("dog")
    5
    >>> compute_score("Hallo")
    8
    >>> compute_score("Hardly?")
    13
    """
    score = 0
    for letter in word:
        score += compute_letter_score(letter)

    return score


def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.

    >>> compute_letter_score("a")
    1
    >>> compute_letter_score("b")
    3
    >>> compute_letter_score("z")
    10
    >>> compute_letter_score("H")
    4
    >>> compute_letter_score("?")
    0
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    positie = 0
    for teken in alphabet:
        if teken == letter:
            return POINTS[positie]
        positie += 1
    return 0


if __name__ == "__main__":
    speler1 = input("Speler 1: ")
    speler2 = input("Speler 2: ")

    score1 = compute_score(speler1)
    score2 = compute_score(speler2)

    if score1 > score2:
        print("Speler 1 wint!")
    elif score2 > score1:
        print("Speler 2 wint!")
    else:
        print("Gelijkspel!")

