#initial state : empty board
#actions: get the optimal actions and find out whats the next states and choose the highst or the smallest score

currentState=[["1","2","3"],["4","5","6"],["7","8","9"]]
m1=0
m2=0
symbol=""
class minimax:
    def __init__(self,s):
        self.s=s
    def player(self):
        m1=0
        m2=0
        for i1 in range(0,3):
            for i in range(0,3):
                if self.s[i1][i]=="X":
                    m1+=1
                elif self.s[i1][i] =="O":
                    m2+=1
                else:
                    pass
            if m1>m2:
                return True
            elif m1==m2==0:
                return 1
            else:
                return False
#-------------------------------------
    def actions(self,s):
        pass
#-------------------------------------
    def maxplayer(self,s,a):
        pass
#-------------------------------------
    def miniplayer(self,s,a):
        pass
#-------------------------------------
    def result(s,a):
        pass
#-------------------------------------
    def terminal(self,s):
        pass
#-------------------------------------
    def utility(self,s):
        pass
#-------------------------------------
class game:
    
    def __init__(self):
        self.player=minimax(currentState).player()
        self.state=minimax(currentState).s
    def draw(self):
        for a in range(0,3):
            print(currentState[a])
    def moveSymboler(self):
        if self.player==True:
            symbol="O"
        elif self.player==False:
            symbol="X"
        if self.player==1:
            symbol="X"
    def mover(self):
        index=input("Where you want your next move>>> ")
        
            
            
        
    
g=game()
g.draw()
