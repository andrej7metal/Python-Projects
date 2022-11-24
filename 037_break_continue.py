def loopBreak():
    for x in range(0,50):
     if x == 29:
         break       
    print("break numero: ",x)
def loopContinue():
 for x in range(1,50):
     if x == 30:
        continue  
loopBreak()
loopContinue()