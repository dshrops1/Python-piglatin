# Author: Dustin shropshire
#transforms a text file into pig latin

#better this than an additonal function call?
vowels = "aeiouAEIOU"
finalList = []


fileChoice = input("Please enter file choice: ")

newFile = fileChoice[0:-4] + "PL.txt"

#lets write unit tests for this as well
def transformToPigLatin(line):
    newLine = []
    firstOccurenceIndex = None

    for word in line:

        if word[0] in vowels:
            newLine.append(word + "way")
        else:

            firstOccurenceIndex = firstOccurrenceOfVowel(word)
            newLine.append(word[firstOccurenceIndex: len(word)] + word[0:firstOccurenceIndex] + "ay")

    return newLine

def firstOccurrenceOfVowel(word):
    indexOfOccurence = []
    for x in vowels[0:5]:
        indexOfOccurence.append(word.find(x))
        indexOfOccurence.sort()
        indexOfOccurence = list(filter(lambda a: a != -1, indexOfOccurence))
    return indexOfOccurence[0]




with open(fileChoice) as f:

    for line in f:

        finalList.append(transformToPigLatin(line.strip().split(" ")))


with open(newFile, "w+") as f2:
    pass



for line in finalList:
    for word in line:
        with open(newFile, "a") as f2:
            #not making the common case fast here but thats fine
            if line.index(word) == len(line)-1:
                f2.write(word + "\n")
            else:
                f2.write(word + " ")



# write back to new file with same name added with PL
