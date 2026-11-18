def longest_word_from_list(lst: list[str]) -> str:
    lst = lst.split()
    langste = len(lst[0])
    for word in lst:
        if len(word) > len(langste):
            langste = word
    return langste

def print_banner(lst: list[str]) -> str:
    aantal_hekjes = longest_word_from_list(lst)
    banner = "#" * len(aantal_hekjes)
    print(banner)
    for woord in lst:
        print(woord)
    print(banner)
    
def string_to_list(words: str) -> list[str]:
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