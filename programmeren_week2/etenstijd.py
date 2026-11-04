def meal(time: str) -> str:
    tijd = time * 60
    
    if tijd >= 420 and tijd <= 480:
        return 
    elif tijd >= 720 and tijd <= 780:
        return
    elif tijd >= 1080 and tijd <= 1140:
        return
    else:
        return

if __name__ == "__main__":
    kloktijd = int(input("Hoe laat is het? "))
    maaltijd = meal(kloktijd)
    print(f"{maaltijd}")
    
    