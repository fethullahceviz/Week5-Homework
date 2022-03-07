#Rock-Paper-Scissoros game with class 

import random
class Game():   

    myList     = ["R", "P", "S"]    
    def userSelection(self):                        
        self.userChoice = input("[ R-> Rock | P-> Paper | S-> Scissors ] ").upper()
        if self.userChoice not in self.myList:
            return "InputError" 
        else:
            return self.userChoice

    #computer selection    
    def compSelection(self):      
       return random.choice(self.myList)
        
    def gameBrain(self):
        #score counter
        computerscore       = 0
        userscore           = 0
        self.computerscore  = computerscore
        self.userscore      = userscore
        #user name and game range input
        self.user           = input("Enter your Name :")
        n                   = int(input("The number of games you want to play :"))
        for _ in range(n):
            ccc = self.compSelection()
            ddd = self.userSelection() 
            if ddd not in self.myList:
                pass
            else:
                if ccc == ddd:
                    pass
                elif (ccc=="R" and ddd=="P") or (ccc=="P" and ddd=="S") or (ccc=="S" and ddd=="R"):            
                    self.userscore+=1 
                else:
                    self.computerscore+=1            

                print ( "ComputerChoice: " f"{ccc}",
                        "Comp "f"{self.computerscore:2}" ":"f"{self.userscore:<2}{ self.user}",sep="\n")
      
    def result(self):

        if self.computerscore > self.userscore:
            x = "Game Winner --> Computer"
        elif self.computerscore < self.userscore:
            x = "Game Winner -->" f" {self.user}"
        else:
            x = "Game Tied"
        return x
      
data = Game()
data.gameBrain()
print(data.result())