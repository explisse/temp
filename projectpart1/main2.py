import os
f = open(os.path.join(r"data\mot_found.txt"),"w")
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

        file1 = open(os.path.join(r"data\mots_7.txt"), "r")

        readfile = file1.read()

        if string1 in readfile:
            score = 0
            string2 = str(string1)
            file2 = open(os.path.join(r"data\mot_found.txt"), "r")

            readfile = file2.read()

            if string1 in readfile:
                break
            else:
                filer = open(os.path.join(r"data\mot_found.txt"), "a")
                filer.write(str(string1))
                filer.close()

                print("""
                
                        """)

                print("found world: " + str(string1))
                #count the score
                M1 = str(string1)
                a = 'a'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                
                
                M1 = str(string1)
                a = 'b'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                
                M1 = str(string1)
                a = 'c'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
             
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21

                

                M1 = str(string1)
                a = 'd'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'e'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'f'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'g'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'h'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'i'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'j'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'k'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40


                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'l'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'm'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())
                
                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14



                M1 = str(string1)
                a = 'n'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4


                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'o'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'p'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                M1 = str(string1)
                a = 'q'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'r'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 's'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                


                M1 = str(string1)
                a = 't'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'u'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'v'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28


                M1 = str(string1)
                a = 'w'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70
                    
                M1 = str(string1)
                a = 'x'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'y'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70



                M1 = str(string1)
                a = 'z'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1
                
                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70

                score_2 = int(score) * 2
                

                print("score: " + str(score_2))                
        else:
            break
        
        file1.close()


A = [str(data1), str(data2), str(data3), str(data4), str(data5), str(data6), str(data7)]
  
comb = permutations(A, 6) 
  
for i in list(comb):
    s = str(i)
    s_new = s.replace(',', '')
    s_new = s_new.replace('(', '')
    s_new = s_new.replace(')', '')
    s_new = s_new.replace("'", "")
    s_new = s_new.replace(' ', '')
    while True:

        string1 = str(s_new)

        file1 = open(os.path.join(r"data\mots_6.txt"), "r")

        readfile = file1.read()

        if string1 in readfile:
            score = 0
            string2 = str(string1)
            file2 = open(os.path.join(r"data\mot_found.txt"), "r")

            readfile = file2.read()

            if string1 in readfile:
                break
            else:
                filer = open(os.path.join(r"data\mot_found.txt"), "a")
                filer.write(str(string1))
                filer.close()

                print("""
                
                        """)

                print("found world: " + str(string1))
                #count the score
                M1 = str(string1)
                a = 'a'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                
                
                M1 = str(string1)
                a = 'b'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                
                M1 = str(string1)
                a = 'c'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
             
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21

                

                M1 = str(string1)
                a = 'd'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'e'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'f'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'g'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'h'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'i'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'j'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'k'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40


                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'l'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'm'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())
                
                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14



                M1 = str(string1)
                a = 'n'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4


                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'o'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'p'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                M1 = str(string1)
                a = 'q'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'r'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 's'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                


                M1 = str(string1)
                a = 't'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'u'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'v'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28


                M1 = str(string1)
                a = 'w'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70
                    
                M1 = str(string1)
                a = 'x'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'y'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70



                M1 = str(string1)
                a = 'z'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1
                
                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70

                score_2 = int(score) * 2
                

                print("score: " + str(score_2))


                
        else:
            break

        file1.close()


A = [str(data1), str(data2), str(data3), str(data4), str(data5), str(data6), str(data7)]
  
comb = permutations(A, 5) 
  
for i in list(comb):
    s = str(i)
    s_new = s.replace(',', '')
    s_new = s_new.replace('(', '')
    s_new = s_new.replace(')', '')
    s_new = s_new.replace("'", "")
    s_new = s_new.replace(' ', '')
    while True:

        string1 = str(s_new)

        file1 = open(os.path.join(r"data\mots_5.txt"), "r")

        readfile = file1.read()

        if string1 in readfile:
            score = 0
            string2 = str(string1)
            file2 = open(os.path.join(r"data\mot_found.txt"), "r")

            readfile = file2.read()

            if string1 in readfile:
                break
            else:
                filer = open(os.path.join(r"data\mot_found.txt"), "a")
                filer.write(str(string1))
                filer.close()

                print("""
                
                        """)

                print("found world: " + str(string1))
                #count the score
                M1 = str(string1)
                a = 'a'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                
                
                M1 = str(string1)
                a = 'b'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                
                M1 = str(string1)
                a = 'c'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
             
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21

                

                M1 = str(string1)
                a = 'd'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'e'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'f'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'g'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'h'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'i'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'j'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'k'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40


                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'l'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'm'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())
                
                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14



                M1 = str(string1)
                a = 'n'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4


                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'o'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'p'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                M1 = str(string1)
                a = 'q'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'r'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 's'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                


                M1 = str(string1)
                a = 't'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'u'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'v'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28


                M1 = str(string1)
                a = 'w'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70
                    
                M1 = str(string1)
                a = 'x'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'y'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70



                M1 = str(string1)
                a = 'z'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1
                
                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70

                score_2 = int(score) * 2
                

                print("score: " + str(score_2))


                
        else:
            break

        file1.close()


A = [str(data1), str(data2), str(data3), str(data4), str(data5), str(data6), str(data7)]
  
comb = permutations(A, 4) 
  
for i in list(comb):
    s = str(i)
    s_new = s.replace(',', '')
    s_new = s_new.replace('(', '')
    s_new = s_new.replace(')', '')
    s_new = s_new.replace("'", "")
    s_new = s_new.replace(' ', '')
    while True:

        string1 = str(s_new)

        file1 = open(os.path.join(r"data\mots_4.txt"), "r")

        readfile = file1.read()

        if string1 in readfile:
            score = 0
            string2 = str(string1)
            file2 = open(os.path.join(r"data\mot_found.txt"), "r")

            readfile = file2.read()

            if string1 in readfile:
                break
            else:
                filer = open(os.path.join(r"data\mot_found.txt"), "a")
                filer.write(str(string1))
                filer.close()

                print("""
                
                        """)

                print("found world: " + str(string1))
                #count the score
                M1 = str(string1)
                a = 'a'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                
                
                M1 = str(string1)
                a = 'b'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                
                M1 = str(string1)
                a = 'c'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
             
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21

                

                M1 = str(string1)
                a = 'd'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'e'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'f'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'g'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14


                M1 = str(string1)
                a = 'h'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28

                M1 = str(string1)
                a = 'i'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'j'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'k'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40


                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'l'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'm'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())
                
                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 2

                if result == 2:
                    score = int(score) + 4

                if result == 3:
                    score = int(score) + 6
                if result == 4:
                    score = int(score) + 8

                if result == 5:
                    score = int(score) + 10

                if result == 6:
                    score = int(score) + 12
                if result == 7:
                    score = int(score) + 14



                M1 = str(string1)
                a = 'n'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4


                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'o'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7



                M1 = str(string1)
                a = 'p'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
              
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 3

                if result == 2:
                    score = int(score) + 6

                if result == 3:
                    score = int(score) + 9
                if result == 4:
                    score = int(score) + 12

                if result == 5:
                    score = int(score) + 15

                if result == 6:
                    score = int(score) + 18
                if result == 7:
                    score = int(score) + 21


                M1 = str(string1)
                a = 'q'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 8

                if result == 2:
                    score = int(score) + 16

                if result == 3:
                    score = int(score) + 24
                if result == 4:
                    score = int(score) + 32

                if result == 5:
                    score = int(score) + 40

                if result == 6:
                    score = int(score) + 48
                if result == 7:
                    score = int(score) + 56


                M1 = str(string1)
                a = 'r'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 's'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                


                M1 = str(string1)
                a = 't'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'u'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
               
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 1

                if result == 2:
                    score = int(score) + 2

                if result == 3:
                    score = int(score) + 3
                if result == 4:
                    score = int(score) + 4

                if result == 5:
                    score = int(score) + 5

                if result == 6:
                    score = int(score) + 6
                if result == 7:
                    score = int(score) + 7


                M1 = str(string1)
                a = 'v'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 4

                if result == 2:
                    score = int(score) + 8

                if result == 3:
                    score = int(score) + 12
                if result == 4:
                    score = int(score) + 16

                if result == 5:
                    score = int(score) + 20

                if result == 6:
                    score = int(score) + 24
                if result == 7:
                    score = int(score) + 28


                M1 = str(string1)
                a = 'w'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70
                    
                M1 = str(string1)
                a = 'x'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70


                M1 = str(string1)
                a = 'y'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1

                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70



                M1 = str(string1)
                a = 'z'
                lst = []
                for pos,char in enumerate(s):
                    if(char == a):
                        lst.append(pos)

                lst1 = str(lst)
                lst2 = lst1.replace("[", '')
                lst2 = lst2.replace("]", '')
                lst2 = lst2.replace(",", '')
                
                result = len(lst2.split())

                if result == 0:
                    nothing = 1
                
                if result == 1:
                    score = int(score) + 10

                if result == 2:
                    score = int(score) + 20

                if result == 3:
                    score = int(score) + 30
                if result == 4:
                    score = int(score) + 40

                if result == 5:
                    score = int(score) + 50

                if result == 6:
                    score = int(score) + 60
                if result == 7:
                    score = int(score) + 70

                score_2 = int(score) * 2
                

                print("score: " + str(score_2))
                
        else:
            break


    break





#PART 2









   

