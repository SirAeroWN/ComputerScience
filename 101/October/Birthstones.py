#takes birth month and returns birthstone

monthNames = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
birthstones = ["Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl", "Ruby", "Ruby", "Peridot", "Sapphire", "Opal", "Topaz", "Turquoise"]

userMonth = input("Enter your birth month: ").lower()

print("Your birthstone is", birthstones[monthNames.index(userMonth)])