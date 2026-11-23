
    >>> string_to_list("a b c d")
    ['a', 'b', 'c', 'd']
    >>> string_to_list("Margherita Tutta la Vita")
    ['Margherita', 'Tutta', 'la', 'Vita']
    >>> string_to_list("Ik hou van programmeren")
    ['Ik', 'hou', 'van', 'programmeren']
    """
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