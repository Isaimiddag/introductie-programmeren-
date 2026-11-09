def yell(sentence: str) -> str:
    
    """
    >>> yell("Hello world!")
    'Hello world!!'
    >>> yell("Do you want candy?")
    'Do you want candy??'
    >>> yell("I like football! And you?")
    'I like football!! And you??'
    >>> yell("I want to play football!")
    'I want to play football!!'
    >>> yell("Hello")
    'No ! or ? in sentence'
    """
    
   
    result = ""
    for char in sentence:
        if char == "!" or char == "?":
            result += char * 2
        else:
            result += char
    return result
    
if __name__ == "__main__":
    text = input("Fill in your text? ")
    print(yell(text))
          
    