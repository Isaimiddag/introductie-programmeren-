def check_input(dna: str) -> bool:
    """
    >>>check_input("paq")
    False
    >>>check_input("APT")
    False
    >>>check_input("TAG")
    True
    >>>check_input("CGA")
    True
    """
    for letter in dna:
        if letter.upper() not in "AGCT":
            return False
        return True
            

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    """
    rna = ""
    for letter in dna.upper():
        

if __name__ == '__main__':
    <Hoofdprogramma>