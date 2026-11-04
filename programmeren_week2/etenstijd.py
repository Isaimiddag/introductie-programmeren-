def meal(time: str) -> str:
    uur, minuten = time.split(":")
    uur = int(uur)
    minuten = int(minuten)
    tijd = 
   
    
    
    if tijd >= 420 and tijd <= 480:
        return 
    elif tijd >= 720 and tijd <= 780:
        return
    elif tijd >= 1080 and tijd <= 1140:
        return
    else:
        return None

if __name__ == "__main__":
    kloktijd = input("Hoe laat is het? ")
    maaltijd = meal(kloktijd)
    print(f"{maaltijd}")
    
    