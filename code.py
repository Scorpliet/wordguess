alphabet=['A','B','C','D'],['E','F','G','H'],['I','J','K','L'],['M','N','O','P'],['Q','R','S','T'],['U','V','W','X'],['Y','Z','.','.']]

def tpose(array): #Transpose function i copied from internet
    return [ [row[c] for row in array if c < len(row)] for c in range(0, max([len(row) for row in array])) ]

def printalp():
   print("`````WORD GUESS````")
   print("1     2     3     4")
   for i in range(7):
     print(alphabet[i])

def guess():
    col_options=[]
    alpha_tpose=[]
    alpha_tpose2=[]
    x = 1
    while x <=length:
         guessinp = int(input("Enter the column of the {}".format(x) + "th alphabet "))
         if guessinp >4 or guessinp<1:
             print("Pls enter correct column number")
         else:    
            col_options.append(guessinp) #adding the input value in a list so it can be fetched later
            x = x+1 
    print(col_options)
    
    for i in col_options:
              alp2=tpose(alphabet) #Transposed the array
              alpha_tpose.append(alp2[i-1]) #added selected columns in new array
    
    length_max_value = len(max(alpha_tpose, key=len))
    range_of_array = len(alpha_tpose)
    
    for i in range(range_of_array):
        print(alpha_tpose[i])
    col_options.clear()
    x=1    
    
    while x<=length:
        guessinp = int(input("Enter the column of the {}".format(x) + "th alphabet "))
        if guessinp>length_max_value or guessinp<1:
             print("Pls enter correct column number")
        else:
             col_options.append(guessinp) #adding the input value in a list so it can be fetched later
             x = x+1
    print(col_options)
    
    for i in col_options:
            alp3=tpose(alpha_tpose)
            alpha_tpose2.append(alp3[i-1])
    range_of_tpose2 = len(alpha_tpose2)
    
    col_options.clear()
    length_max_value2 = len(max(alpha_tpose2, key=len))
   
    for i in range(length_max_value2):
        print(alpha_tpose2[i])  
   
    print("YOUR WORD WAS")
   
    for i in range(length_max_value2):
           j=i 
           print(alpha_tpose2[i][j])           

printalp()
length = int(input("Enter the length of your word "))
guess()
