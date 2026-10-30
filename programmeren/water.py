def hoeveelheid_water(minuten: int) -> int
if __name__ == "__main__":
    minuten = int(input("hoeveelheid minuten douchen: "))
    result = minuten * 12
    print(f"met {minuten} minuten douchen verbruik je {result} flesjes water van 500ml.Dat is {result*0.5} liter")