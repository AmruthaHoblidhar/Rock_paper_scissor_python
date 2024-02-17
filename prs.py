import random

print("*************************************")

print("*    *PAPER  * ROCK * SCISSOR *     *")

print("*************************************")

print("LETS START THE GAME!!!......")

point=0

ai=0

hs=0

cs=0

ma=0

while(True):
   
 c=input("choose the option:paper->p rock->r scissor->s stop->stop: ")

    if(c=="p"):
       
 print("paper")
        
point=10+random.randint(1,3)
       
 match point:
           
 case 11:
               
 ma=ma+1
               
 hs=hs+1
                
print("Human:paper", "AI:rock")
               
 print("match:",ma,"Human score:",hs,"AI score:",cs,)
  
 print("Human: wins","AI :lost")
               
 print("-----------------------")
           
 case 12:
               
 ma=ma+1
                
cs=cs+1
               
 print("Human:paper","AI:scissor")
  
 print("match:",ma,"Human score:",hs,"AI score:",cs,)
 
 print("Human :lost","AI:wins")
 
 print("-----------------------")
            
case 13:
               
 ma=ma+1
               
 hs=hs+1
                
cs=cs+1
                
print("Human:paper", "AI:paper")
               
print("match:",ma,"Human score:",hs,"AI score:",cs,)
           
print("match draw")
 
 print("-----------------------")
   
 elif(c=="R"):
        
print("Rock")
       
 point=20+random.randint(1,3)
       
 match point:
            
case 21:
                
ma=ma+1
                
hs=hs+1
                
print("Human:rock", "AI:paper")
 
print("match:",ma,"Human score:",hs,"AI score:",cs,)
    
print("Human: wins","AI :lost")
               
print("-----------------------")
           
 case 22:
               
 ma=ma+1
               
 cs=cs+1
                
print("Human:rock","AI:scissor")
               
print("match:",ma,"Human score:",hs,"AI score:",cs,)
                
print("Human :lost","AI:wins")
              
print("-----------------------")
            
case 23:
                
ma=ma+1
                
hs=hs+1
                
cs=cs+1
                
print("Human:rock", "AI:rock")
                
print("match:",ma,"Human score:",hs,"AI score:",cs,)
                
print("match draw")
                
print("-----------------------")
   
elif(c=="s"):
        
print("scissor")
        
point=30+random.randint(1,3)
        
match point:
            
case 31:
                
ma=ma+1
                
hs=hs+1
                
print("Human:scissor","AI:paper")
                
print("match:",ma,"Human score:",hs,"AI score:",cs,)
                
print("Human: wins","AI :lost")
                
print("-----------------------")
            
case 32:
                
ma=ma+1
                
cs=cs+1
                
print("Human:scissor","AI:rock")
                
print("match:",ma,"Human score:",hs,"AI score:",cs,)
                
print("Human :lost","AI:wins")
                
print("-----------------------")
            
case 33:
               
 ma=ma+1
                
hs=hs+1
                
cs=cs+1
                
print("Human:scissor", "AI:scissor")
                
print("match:",ma,"Human score:",hs,"AI score:",cs,)
                
print("match draw")
                
print("-----------------------")
    
elif(c=="stop"):
       
 break

print("Program End")