def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.

    >>> check_input("ATGC")
    True

    >>> check_input("atGcAgtAttGCA")
    True

    >>> check_input("hello")
    False

    >>> check_input("TAG")
    True

    >>> check_input("APT")
    False
    """
    for letter in dna:
        if letter.upper() not in "AGCT":
            return False
    return True


def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).

    >>> transcribe_dna_to_rna("ATGC")
    'UACG'

    >>> transcribe_dna_to_rna("atGcAgtAttGCA")
    'UACGUCAUAACGU'

    >>> transcribe_dna_to_rna("cga")
    'GCU'

    >>> transcribe_dna_to_rna("TAG")
    'AUC'
    """
    rna = ""

    for letter in dna.upper():
        if letter == "A":
            rna += "U"
        elif letter == "G":
            rna += "C"
        elif letter == "C":
            rna += "G"
        elif letter == "T":
            rna += "A"

    return rna


if __name__ == "__main__":
    dna = input("DNA: ")

    if check_input(dna):
        print(f"RNA: {transcribe_dna_to_rna(dna)}")
    else:
        print("That is not a valid DNA string")