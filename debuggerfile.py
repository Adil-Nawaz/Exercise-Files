import random
namesList = [
    "Ayaan", "Zara", "Hamza", "Elena",
    "Rayan", "Sophia", "Daniyal", "Maya",
    "Ibrahim", "Lina", "Arham", "Ava",
    "Saad", "Noor", "Hassan", "Amelia"
]
printList = []
while True:
    next_name = input ("Type n for next name ").lower()
    if next_name == "n":
        randomName = random.choice(namesList)
        if not randomName in printList and len(printList) < len(namesList):
            printList.append(randomName)
        elif len(printList) == len(namesList):
            break
    print(printList)

