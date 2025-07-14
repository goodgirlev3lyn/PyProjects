from cardAttributes import Card

# HMS Hood, Dreadnought, Bellerophon, Queen Elizabeth, Warspite, King George V, Vanguard
# USS Texas, New Mexico, Colorardo, North Carolina, Iowa, Montana
# KMS/DKM Bismarck/Tirpitz, H42, Konig, Graf Spee
# IJN Yamato, Nagato, Ise

#Card(name, country, firepower, tonnage, speed, armour)

global Cards
Cards = [
    Card("HMS Hood", "UK", 72, 45, 94, 63, "img/hood.jpg"),
    Card("HMS Dreadnought", "UK", 31, 38, 42, 100, "img/dreadnought.jpg"),
    Card("HMS Bellerophon", "UK", 34, 41, 47, 74, "img/bellerophon.jpg"),
    Card("HMS Queen Elizabeth", "UK", 72, 61, 54, 79, "img/queen_elizabeth.jpg"),
    Card("HMS Warspite", "UK", 73, 59, 55, 78, "img/warspite.jpg"),
    Card("HMS King George V", "UK", 61, 64, 84, 67, "img/kingGeorgeV.jpg"),
    Card("HMS Vanguard", "UK", 64, 68, 73, 63, "img/vanguard.jpg"),

    Card("USS Texas", "US", 47, 54, 22, 57, "img/texas.jpg"),
    Card("USS New Mexico", "US", 48, 51, 24, 59, "img/newmexico.jpg"),
    Card("USS Colorado", "US", 52, 63, 21, 53, "img/colorado.jpg"),
    Card("USS North Carolina", "US", 57, 37, 51, 61, "img/northcarolina.jpg"),
    Card("USS Iowa", "US", 79, 65, 83, 71, "img/iowa.jpg"),
    Card("USS Montana", "US", 77, 63, 87, 82, "img/montana.jpg"),

    Card("DKM Bismarck", "Germany", 64, 65, 71, 66, "img/bismarck.jpg"),
    Card("DKM Tirpitz", "Germany", 63, 66, 72, 67, "img/tirpitz.jpg"),
    Card("H42-Hutten", "Germany", 85, 100, 41, 92, "img/h42.jpg"),
    Card("DKM Graf Spee", "Germany", 41, 37, 79, 44, "img/grafSpee.jpg"),

    Card("IJN Yamato", "Japan", 100, 82, 31, 82, "img/yamato.jpg"),
    Card("IJN Nagato", "Japan", 51, 61, 82, 61, "img/nagato.jpg"),
    Card("IJN Ise", "Japan", 75, 82, 77, 42, "img/ise.jpg"),
    Card("HMS OP Debugging", "Debug", 100, 100, 100, 100, "None"),
    Card("HMS Weak Debugging", "Debug", 0, 0, 0, 0, "None")
]