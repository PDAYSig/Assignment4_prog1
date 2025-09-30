name = input()

firstName = name.split(", ")[1]
lastName = name.split(", ")[0]


lastNameCapitalized = lastName[0].upper() + lastName[1:]

firstLetter = firstName[0]


print(firstLetter.upper(), ". ", lastNameCapitalized, sep="")
