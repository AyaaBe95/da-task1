
# Take a paragraph and store it in a string, then seperate the string into words and
# store them into a list, finally, find the number of occurrences of each word in the
# mentioned list and store them into a dictionary where the word itself represents the
# key and the number of occurrences represents the value for each key.




def checkOccurences():
    check = True
    # take paragraph from user
    para = input("Enter a paragraph ")
    while(check):
        # check if the para is not empty
        if(para ):
            # converte paragraph to lower case
            lowerPara= para.lower()
            # initializing punctuations
            punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~”'''
            # remove punctuations from paragraph
            for var in lowerPara:
                if var in punc:
                    lowerPara = lowerPara.replace(var, ' ') 
            # split the paragraph and store it in a list of strings
            splitedPara = lowerPara.split(' ')
            # create dictionarry
            occurences = {}

            # loop over the list 
            for word in splitedPara:
                # check if the word exists in dict increase its value by one 
                if word in occurences:
                    occurences[word] +=1
                elif word=='':
                    continue
                # if not exist add the word an put 1 as its value
                else:
                    occurences[word]=1
            print(occurences)
            check=False
        else:
            print('Enter non-empty paragraph ')
            para = input("Enter a paragraph ")

       
checkOccurences()



