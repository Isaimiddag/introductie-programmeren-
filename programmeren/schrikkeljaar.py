if __name__ = "__main__":
    jaartal = int(input("Welk jaartal wilt u weten?: "))
    if jaartal % 4 == 0:
        print(f"Het jaartal {jaartal} is een schrikkeljaar!")
    elif jaartal % 400 == 0: