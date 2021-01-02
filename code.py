alphabet=[['A','B','C','D'], ['E','F','G','H'], ['I','J','K','L'], ['M','N','O','P'], ['Q','R','S','T'], ['U','V','W','X'], ['Y','Z']]

def tpose(array): #Transpose function i copied from internet
    return [ [row[c] for row in array if c < len(row)] for c in range(0, max([len(row) for row in array])) ]

def printalp():
   print("`````WORD GUESS````")
   print("1     2     3     4")
   for i in range(7):
     print(alphabet[i])


printalp()
length = int(input("Enter the length of your word "))
maxcolumns=[1,2,3,4,5,6,7]



def guess():
    columnopt=[]
    lengthofinput = 1
    while lengthofinput <=length:
         guessinp = int(input("Enter the column of the {}".format(lengthofinput) + "th alphabet "))
         if guessinp >4 or guessinp<1:
             print("Pls enter correct column number")
         else:    
            columnopt.append(guessinp) #adding the input value in a list so it can be fetched later
            lengthofinput = lengthofinput+1
            columnopt = list(dict.fromkeys(columnopt)) #a dictionary cannot have duplicate values so we turn it into one and make it back into a list again          
    ranget= len(columnopt)
    for i in range(ranget):
              alp2=tpose(alphabet) #Transposed the array
              alpt=[] #Created new array
              alpt.append(alp2[i]) #added selected columns in new array
              print(alpt)

     
guess()    
