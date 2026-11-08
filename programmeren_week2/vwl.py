def remove_vowels(text: str) -> str:
    vowels = "a, e, i, o, u"
    result = ""
    for char in text:
        if char in vowels:
            result -= char
        return result

if __name__ == "__main__":
    text = input("Geef een zin: ")
    inp
