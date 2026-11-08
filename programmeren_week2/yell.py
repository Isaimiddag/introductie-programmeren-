def yell(sentence: str) -> str:
    teken = " !, ? "
    result = teken  *2 
    for char in sentence:
        if char not in sentence:
            return "No ? or ! in sentence
    