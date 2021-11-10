#Simple CMD Line Tool to Convert Weight/Height

class WeightConversion:
    def KiloToStone():
        userinput = float(input("Enter your Weight in Kilograms: "))
        userinput = round(userinput, 2)

        math = float(userinput * 0.15747304)
        math = str(round(math, 2))
        
        print("Your Weight in Kilograms is: " + str(userinput) + " Kg.\nYour weight in Stones is: " + math + " Stone")
        MainMenu.MainMenuChoices()

    def StoneToKilo():
        userinput = float(input("Enter your weight in Stone: "))
        userinput = round(userinput, 2)

        math = float(userinput / 0.15747304)
        math = str(round(math, 2))

        print("Your Weight in Stone is: " + str(userinput) + " Stone\nYour Weight in Kilograms is: " + math + " Kg.")
        MainMenu.MainMenuChoices()
class HeightConversion:
    def CmToFt():
        userinput = int(input("Enter your height in centimeters: "))

        mathft = int((userinput / 2.54) / 12)
        mathinches = int((userinput / 2.54) - (12 * mathft))

        print("Your Height in Centimeters is: " + str(userinput) + "cm. Which is "+ str(userinput * 0.01) + " Meters\nYour height in Feet and Inches is: " + str(mathft) + " Ft " + str(mathinches) + " Inches.")
        MainMenu.MainMenuChoices()
    
"""     def FttoCm():
        userinput = ("Enter your height in feet and inches: ") """
        
class MainMenu:
    def MainMenuChoices():
        MenuInput = input("---------------------------------------------------------------\nChoose from one of the following options: \nPress K on your keyboard to convert Kilograms to Stone\nPress S on your keyboard to convert Stone to Kilograms\nPress C on your keyboard to convert centimeters to Feet and Inches\nEnter your choice: ")

        if MenuInput == "k":
            WeightConversion.KiloToStone()
        elif MenuInput == "s":
            WeightConversion.StoneToKilo()
        elif MenuInput == "c":
            HeightConversion.CmToFt()
        else:
            print("Invalid Choice! Please try again")
            MainMenu.MainMenuChoices()



#Call Main Menu
MainMenu.MainMenuChoices()