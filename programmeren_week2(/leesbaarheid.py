def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman-Liau-formule.

    >>> coleman_liau(8, 4, 29)
    -1
    """
    L = 100 * letters / words
    S = 100 * sentences / words

    return round(0.0588 * L - 0.296 * S - 15.8)


def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.

    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -1

    >>> calculate_grade("Congratulations! Today is your day. You're off to Great Places! You're off and away!")
    3

    >>> calculate_grade("There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.")
    9
    """
    letters = 0
    words = 0
    sentences = 0
    in_word = False

    for char in text:
        if char.isalpha():
            letters += 1

        if char.isalpha() and not in_word:
            words += 1
            in_word = True
        elif not char.isalpha() and char != "'":
            in_word = False

        if char in ".!?":
            sentences += 1

    return coleman_liau(words, sentences, letters)


if __name__ == "__main__":
    text = input("Text: ")

    grade = calculate_grade(text)

    if grade < 1:
        print("Below Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")