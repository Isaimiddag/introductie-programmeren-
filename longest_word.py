def longest_word_from_list(lst: list[str]) -> str:
    lst = lst.split()
    langste = len(word[0])
    for word in lst:
        if len(word) > langste:
            langste = word
    return langste

def print_banner(lst: list[str]) -> str:
    aantal_hekjes = longest_word_from_list(langste)
    print(aantal_hekjes)
    print(lst"n/")
    print(aantal_hekjes)
    
def string_to_list(words: str) -> list[str]:
    for word in words: 
        
    
if __name__ == "__main__":
    banner = input("geef wat woorden: ")
    print(print_banner(banner))