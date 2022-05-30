
# Take a paragraph and store it in a string, then seperate the string into words and
# store them into a list, finally, find the number of occurrences of each word in the
# mentioned list and store them into a dictionary where the word itself represents the
# key and the number of occurrences represents the value for each key.


def checkOccurences():
    # take paragraph from user
    para = input("Enter a paragraph ")
    # split the paragraph and store it in a list of strings
    splitedPara = para.split(' ')
    print(splitedPara)

checkOccurences()

