
#Simple program to convert kilos to stone or vice versa

class WeightConversion:

    def __init__():
        pass

    def KiloToStone():
        kilo = input("Enter your weight in kilos: ")
        mathdone = float(kilo) * 0.15747
        print("Your weight of " + str(kilo) + " kilos is approximatley " + str(mathdone) + " stone")

    def StoneToKilo():
        stone = input("Enter your weight in stone: ")
        mathdone = float(stone) / 0.15747
        print("Your weight of " + str(stone) + " stone is approximatley " + str(mathdone) + " kilos")

    def ConversionUser():
        userinput = input("Press k for kilo to stone\nPress s for stone to kilo\nEnter your choice: ")

        if userinput == "k":
            WeightConversion.KiloToStone()
        elif userinput == "s":
            WeightConversion.StoneToKilo()
        else:
            print("Invalid Choice! Try again")

class HeightConversion:

    def __init__():
        pass

    def CmToFt():
        cm = input("Enter your height in centimeters: ")
        mathinches = float(cm) / 2.54
        mathft = mathinches / 12
        ftfinal = int(mathft)

        inchesfinal = int(mathinches - (12*ftfinal))

        ftconv = str(ftfinal)
        inchconv = str(inchesfinal)
        print("Your height is " + ftconv + " feet and " + inchconv + " inches")



HeightConversion.CmToFt()
WeightConversion.ConversionUser()