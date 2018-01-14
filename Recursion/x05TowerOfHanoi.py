class TowerOfHanoi:
    
    def __init__(self, height):
        self.towers = [[], [], []]
        self.height = height
        self.generateTowers(self.height)
    
    def generateTowers(self,height):
        for i in range(0,height):
            self.towers[0].append(' '*i + '_'*2*(height-i) + ' '*i)
        self.displayTowers()
        
    def displayTowers(self):
          # DISPLAYINY TOWERS
        for disk in range(self.height-1,-1,-1):
            for tower in range(3):
                try:
                    print(self.towers[tower][disk], end=' ')
                except:
                    print(' ' * 2 * self.height, end=' ')
            print('') # inserting a new line
        print('*'*20)
     
    def solve(self):
        self.moveTower(self.height,0,2,1)
        
    def moveTower(self,height,fromPole, toPole, middlePole):
    
        if height >=  1:
            self.moveTower(height-1, fromPole, middlePole, toPole)
            self.moveDisk(fromPole, toPole)
            self.moveTower(height-1, middlePole, toPole, fromPole)
        
    def moveDisk(self,fromPole, toPole):
        self.towers[toPole].append(self.towers[fromPole].pop())
        self.displayTowers()
    
t = TowerOfHanoi(4)
t.solve()