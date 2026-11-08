def shout(text: str) -> str:
    """
    
    result = ""
    
    for letter in text:
        result += letter.upper()
    return result
        
if __name__ == "__main__":
    text = input("Geef een zin: ")
   
    print(shout(text))
