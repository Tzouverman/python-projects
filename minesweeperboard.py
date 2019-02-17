import random 

grammes=0
stiles=0
bombes=0


while True: 
        grammes=int(input("Give the number of rows\n"))
        if grammes >2 and grammes <51:
            print("OK!\n")
            break
        else:
            print("The number of rows has to be between the values 3 and 50\n")            
  

while True: 
        stiles=int(input("Give the number of columns\n"))
        if stiles >2 and stiles <51:
            print("OK!\n")
            break
        else:
            print("The number of columns has to be between the values 3 and 50\n")
   

megistosarithmosbombwn=stiles*grammes-1 

while True: 
    bombes=int(input(""))
    if bombes > 1 and bombes < megistosarithmosbombwn:
        print("OK!\n")
        break
    else:
        print("The number of bombs has to be between the values 2 and",megistosarithmosbombwn,")\n")
    


suntetagmenes=[]
for r in range(0,grammes):
    for c in range (0,stiles):
        suntetagmenes.append([r,c])


suntetagmenesbombas =random.sample(suntetagmenes,bombes) 
narkopedio=[[0 for i in range(stiles)]for j in range(grammes)] 

for suntetagmenesbombas in suntetagmenesbombas : 
    (x,y)=suntetagmenesbombas 
    narkopedio[x][y]="^" 


    rangegrammis=range(x-1, x+2)
    rangestilis=range(y-1,y+2)
        
    
    for i in rangegrammis:
        for j in  rangestilis:
            if (0<=i<grammes and 0<=j<stiles and narkopedio[i][j]!="^"):
                narkopedio[i][j]+=1
    
for i in range(len(narkopedio)):
    for j in range(len(narkopedio[i])):
        print(narkopedio[i][j], end="  ")
    print()
            




