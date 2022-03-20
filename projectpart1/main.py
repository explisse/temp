invite = "1ère lettre: "
while True:
    data1 = input(invite)
    break

invite = "2ème lettre: "
while True:
    data2 = input(invite)
    break


invite = "3ème lettre: "
while True:
    data3 = input(invite)
    break

invite = "4ème lettre: "
while True:
    data4 = input(invite)
    break

invite = "5ème lettre: "
while True:
    data5 = input(invite)
    break

invite = "6ème lettre: "
while True:
    data6 = input(invite)
    break

invite = "7ème lettre: "
while True:
    data7 = input(invite)
    break



  
from itertools import permutations 
A = [str(data1), str(data2), str(data3), str(data4), str(data5), str(data6), str(data7)]
  
comb = permutations(A, 7) 
  
for i in list(comb):
    s = str(i)
    s_new = s.replace(',', '')
    s_new = s_new.replace('(', '')
    s_new = s_new.replace(')', '')
    s_new = s_new.replace("'", "")
    s_new = s_new.replace(' ', '')
    while True:
        
        string1 = str(s_new)

        file1 = open(r"C:\Users\Tristan\Desktop\scrabble\projectpart1\data\mots_7.txt", "r")

        readfile = file1.read()

        if string1 in readfile:
            string2 = str(s_new)
            file3 = open(r"C:\Users\Tristan\Desktop\scrabble\projectpart1\data\mot_found.txt", "r")
            readfile3 = file3.read()
            if string2 in readfile:
                break
                file3.close()
            
            else:

                filer = open(r"C:\Users\Tristan\Desktop\scrabble\projectpart1\data\mot_found.txt", "a")
                filer.write(str(string1))
                filer.close()
                break
                
        else:
            break
        file1.close()
            

    
    

  


    
    





