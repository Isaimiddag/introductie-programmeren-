def check_answer(answer: str) -> bool:
    """
    check_answer("42")
    True
    
    check_answer("honderd")
    False
    
    check_answer("tweeenveertig")
    True
    
    """
if answer = "42":
    return True
elif answer = "tweeenveertig":
    return True
elif answer = "tweeënveertig":
    return True
else:
    return False


if __name__ == "__main__":
    answer = input("Wat is het antwoord op het leven, het universum en alles? "
    if check_answer(answer):
        print("Dat is helemaal goed")
    else:
        print("Helaas, dat is fout")


    
    
