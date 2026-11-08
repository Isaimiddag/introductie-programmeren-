def convert(text: str) -> str:
    result = ""
    for char in text:
        if char.isupper():
            return "_"+ char.lower()
        else:
            return char
if __name__ == "__main__":
    input = input("Geef een camelcase: ")
    print(convert(input))
            
            