def yell(sentence: str) -> str:
    
    """
    >>> yell("Hello world!")
    Hello world!!
    >>> yell("Do you want candy?")
    Do you want candy??
    >>> yell("I like football! And you?")
    I like football!! And you??
    >>> yell("I want to play football!")
    I want to play football!!
    >>> yell("Hello")
    No ! or ? in sentence
    """
    
   
    result = ""
    for char in sentence:
        if char not in sentence:
            return "No ? or ! in sentence."
        else:
            return
    