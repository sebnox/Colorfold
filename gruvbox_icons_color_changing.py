colors = [
    "red", "rust", "lime", "jade", "grey", "gold", "blue", "white",
    "olive", "green", "black", "yellow", "violet", "tomato", "purple",
    "orange", "citron", "pumpkin", "sapphire", "lavender", "highland",
    "pistachio", "firebrick", "custom"
]

the_question1 = input("Do you want to see the colors choices? y or n: ")
the_question2 = input("Please select a folder color: ")

def changing_the_color():
    print(the_question1)
    if the_question1 == "y":
        return colors, the_question2
    else:
        return the_question2
