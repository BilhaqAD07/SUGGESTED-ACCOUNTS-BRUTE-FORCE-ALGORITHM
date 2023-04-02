from typing import List, Tuple
import os
import time


def fileHandle(FileName: str) -> List[Tuple[str, str]]:
    # { I.S. File terdapat isi/ terdefinisi dan tidak kosong }
    # { F.S. Return list berupa Pair yang mempunyai 2 elemen nama akun yang saling follow antara satu sama lain.}

    # DECLARE
    List = []
    temp = []

    # ALGORITHM
    if os.path.exists(FileName):
        with open(FileName, 'r') as file:
            for line in file:
                temp = line.strip().split()
                List.append((temp[0], temp[1]))
    else:
        print("Error, File not found!")
        exit(0)

    return List


def notInList(name: str, List: List[Tuple[str, str]]) -> bool:
    # { I.S. File terdapat isi/ terdefinisi dan tidak kosong, nama terdefinisi }
    # { F.S. Return nilai true bila name tidak pada list dan false bila nama terdapat pada list }

    # ALGORITHM
    for element in List:
        if name == element[0] or name == element[1]:
            return False

    return True


def mutualNum(List: List[str]) -> List[Tuple[str, int]]:
    # { I.S. File terdapat isi/ terdefinisi dan tidak kosong }
    # { F.S. Return list yaitu Pair yang mempunyai 2 elemen berupa elemen ke-1 nama akun (unique) dan elemen ke-2 berupa jumlah munculnya nama akun pada list}

    # DECLARE
    Pair = []
    Count = 0

    # ALGORITHM
    for i in List:
        Count = 0
        if notInList(i, Pair):
            for j in List:
                if j == i:
                    Count += 1
            Pair.append((i, Count))

    return Pair


def sortingPair(pair: List[Tuple[str, int]]) -> List[Tuple[str, int]]:
    # { I.S. Pair terdefinisi dan tidak kosong }
    # { F.S. Return Pair yang pada elemen kedua telah terurut mengecil }

    # DECLARE
    temp = ()

    # ALGORITHM
    for i in range(len(pair)):
        for j in range(len(pair) - 1):
            if pair[j][1] < pair[j+1][1]:
                temp = pair[j]
                pair[j] = pair[j+1]
                pair[j+1] = temp

    return pair


# Input
fileName = input("Enter filename : ")
List = fileHandle(fileName)
user = input("Enter name of user : ")

start = time.time()

# Searching
Recom = []
Mutual = []

for pair in List:
    # Checking user in pair
    if (pair[0] == user or pair[1] == user):
        # Condition 1, user inside pair[0]
        if (pair[0] == user):
            if (notInList(pair[1], Mutual)):
                Mutual.append(pair[1])
            for following in List:
                if (following[0] != user and following[1] != user):
                    if (following[0] == pair[1]):
                        Recom.append(following[1])
                    elif (following[1] == pair[1]):
                        Recom.append(following[0])

        # Condition 2, user inside pair[1]
        elif (pair[1] == user):
            if (notInList(pair[0], Mutual)):
                Mutual.append(pair[0])
            for following in List:
                if (following[0] != user and following[1] != user):
                    if (following[0] == pair[0]):
                        Recom.append(following[1])
                    elif (following[1] == pair[0]):
                        Recom.append(following[0])


# Delete mutual account that already followed by user
newRecom = [r for r in Recom if r not in Mutual]

# Output
print("\n" + user + " Tiktok")

print("\nSuggested accounts : ")
i = 1
newRecom = mutualNum(newRecom)
sortingPair(newRecom)
for suggested in newRecom:
    print(str(i) + ". " + suggested[0] + ", has " +
          str(suggested[1]) + " mutual friends")
    i += 1

end = time.time()
print("\n" + str(end - start) + " seconds")
