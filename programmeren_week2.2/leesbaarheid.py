
        if char.isalpha():
            letters += 1
        elif char == " ":
            words += 1
        elif char in ".!?":
            sentences += 1

    return coleman_liau(words, sentences, letters)


if __name__ == "__main__":
    text = input("Text: ")

    grade = calculate_grade(text)

    if grade < 1:
        print("Below Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")