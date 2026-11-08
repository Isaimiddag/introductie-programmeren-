def convert(text: str) -> str:
    result = ""
    for char in text:
        if char.isupper():
            return "_"+ char.lower()
        
            
            