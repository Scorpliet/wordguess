row1=['A','B','C','D']
row2=['E','F','G','H']
row3=['I','J','K','L']
row4=['M','N','O','P']
row5=['Q','R','S','T']
row6=['U','V','W','X']
row7=['Y','Z']
alphabet=[row1,row2,row3,row4,row5,row6,row7]
def tpose(array): #Transpose function i copied from internet
    return [ [row[c] for row in array if c < len(row)] for c in range(0, max([len(row) for row in array])) ]

def printalp():
   print("`````WORD GUESS````")
   print("1     2     3     4")
   for i in range(7):
     print(alphabet[i])

def guess():
    columnopt=[]
    alpt=[]
    alpt2=[]
    x = 1
    while x <=length:
         guessinp = int(input("Enter the column of the {}".format(x) + "th alphabet "))
         if guessinp >4 or guessinp<1:
             print("Pls enter correct column number")
         else:    
            columnopt.append(guessinp) #adding the input value in a list so it can be fetched later
            x = x+1
            #columnopt = list(dict.fromkeys(columnopt))  #a dictionary cannot have duplicate values so we turn it into one and make it back into a list
  
    ranget= len(columnopt)
    print(columnopt)
    for i in columnopt:
              alp2=tpose(alphabet) #Transposed the array
              alpt.append(alp2[i-1]) #added selected columns in new array
    
    length_max_value = len(max(alpt, key=len))
    range_of_array = len(alpt)
    for i in range(range_of_array):
        print(alpt[i])
    columnopt.clear()
    x=1    
    
    while x<=length:
        guessinp = int(input("Enter the column of the {}".format(x) + "th alphabet "))
        if guessinp>length_max_value or guessinp<1:
             print("Pls enter correct column number")
        else:
             columnopt.append(guessinp) #adding the input value in a list so it can be fetched later
             x = x+1
    range2= len(columnopt)
    print(columnopt)
    for i in columnopt:
            alp3=tpose(alpt)
            alpt2.append(alp3[i-1])
    range_of_tpose2 = len(alpt2)
    columnopt.clear()
    length_max_value2 = len(max(alpt2, key=len))
    for i in range(length_max_value2):
        print(alpt2[i])  
    print("YOUR WORD WAS")
    for i in range(length_max_value2):
        j=i
        print(alpt2[i][j])    

printalp()
length = int(input("Enter the length of your word "))
guess()



   
