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
        if teken != " ":
            huidig_woord += teken
        else:
            lijst.append()
    
        
    
if __name__ == "__main__":
    banner = input("geef wat woorden: ")
    print(print_banner(banner))