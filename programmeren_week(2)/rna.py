def check_input(dna: str) -> bool:
    """
    >>> check_input("paq")
    False
    >>> check_input("APT")
    False
    >>> check_input("TAG")
    True
    >>> check_input("CGA")
    True
    >>> check_input("agct")
    True
    """
    for letter in dna:
        if letter.upper() not in "AGCT":
            return False
    return True
            

def transcribe_dna_to_rna(dna: str) -> str:
    """
    >>> transcribe_dna_to_rna("cga")
    'GCU'

    >>> transcribe_dna_to_rna("AGC")
    'UCG'

    >>> transcribe_dna_to_rna("TAG")
    'AUC'

    >>> transcribe_dna_to_rna("TTT")
    'AAA'

    >>> transcribe_dna_to_rna("ACGT")
    'UGCA'
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
        

if __name__ == '__main__':
    dna = input("Vul dna in: ")
    if check_input(dna):
        print(transcribe_dna_to_rna(dna))
    else:
        print("That is not a valid DNA string")