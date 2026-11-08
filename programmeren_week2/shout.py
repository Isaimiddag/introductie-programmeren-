def shout(text: str) -> str:
    result = ""
    
    for letter in text:
        result += letter.upper()
    return resultaat
        
if __name__ == "__main__":
    text = input("Geef een zin: ")
   
    print(shout(text))
