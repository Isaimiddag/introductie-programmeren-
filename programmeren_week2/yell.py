def yell(sentence: str) -> str:
    
    """
    >>> yell("Hello world!")
    Hello world!!
    >>> yell("Do you want candy?")
    Do you want candy??
    >>> 
    teken = " !, ? "
    result = teken  *2 
    for char in sentence:
        if char not in sentence:
            return "No ? or ! in sentence."
        else:
            return
    