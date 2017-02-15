#Dit is een aanpassing
def main():
    geslacht_docent = str(input("Is de docent een man of een vrouw? "))
    mentor_docent = str(input("Is de docent een mentor? "))
    geslacht = geslacht_docent.lower()
    mentor = mentor_docent.lower()
    print(geslacht_en_mentor(geslacht, mentor))

def geslacht_en_mentor(geslacht, mentor):
    if geslacht == "man" and mentor == "ja":
        return("De docent Jan heeft rood haar, is mentor en draagt een bril.")
    elif geslacht == "vrouw" and mentor == "nee":
        return("De docente Kim heeft zwart haar, is geen mentor en draagt geen bril.")
    else:
        haar_docent = str(input("Welke kleur haar heeft de docent? "))
        haar = haar_docent.lower()
        print(haarkleur(geslacht, mentor, haar))

def haarkleur(geslacht, mentor, haar):
    if geslacht == "man" and mentor == "nee":
        if haar == "zwart":
            return("De docent Said heeft zwart haar, is geen mentor en draagt geen bril.")
        elif haar == "bruin":
            return("De docent Jacob heeft bruin haar, is geen mentor en draagt geen bril.")

    elif geslacht == "vrouw" and mentor == "ja":
        if haar == "bruin":
            return("De docente Bo heeft bruin haar, is mentor en draagt een bril.")
        elif haar == "zwart":
            return("De docente Hanieh heeft zwart haar, is mentor en draagt geen bril.")

    else:
        print("Er is geen docent met de combinatie van deze eigenschappen. Probeer het opnieuw.")
        print(main())

print(main())
