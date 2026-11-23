def longest_word_from_list(lst: list[str]) -> str:
    huidig_langste = lst[0]
    for word in lst:
        if len(word) > len(huidig_langste):
            huidig_langste = word
    return huidig_langste

def print_banner(lst: list[str]) -> str:
    banner = ""
    for char in longest_word_from_list(lst):
        banner += "*"
    for word in lst:
        banner += word + "\n"
    for char in longest_word_from_list(lst):
        banner += "*"
    return banner

print_banner
    

