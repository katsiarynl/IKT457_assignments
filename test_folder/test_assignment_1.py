import random



class Environment:
    def __init__(self, c_1, c_2):
        self.c_1 = c_1 #probability of punishing for saying yes
        self.c_2 = c_2 #probability of punishing for action no 
    
    #! changes have to be done here:
    def penalty(self, action, counter):
        if counter>=0 and counter<4: 
            probability_penalty=1-(counter*0.2)
            self.c_1=probability_penalty
            self.c_2=self.c_1
            if action == "yes":
                if random.random() <= self.c_1:
                    print("penalty true case1yes")
                    return True
                else:
                    print("penalty false case1yes")
                    return False
            elif action == "no":
                if random.random() <= self.c_2:
                    print("penalty true case1no")
                    return True
                else:
                    print("penalty false case1no")
                    return False
        if counter==4 or counter==5:
            probability_penalty=1-(0.6-(counter-3)*0.2)
            self.c_1=probability_penalty
            self.c_2=self.c_1
            if action == "yes":
                if random.random() <= self.c_1:
                    print("penalty true case2yes")
                    return True
                else:
                    print("penalty false case2yes")
                    return False
            elif action == "no":
                if random.random() <= self.c_2:
                    print("penalty true case2no")
                    return True
                else:
                    print("penalty false case2no")
                    return False          


  

class Tsetlin:
    def __init__(self, n):
        # n is the number of states per action
        self.n = n

        # Initial state selected randomly
        self.state = random.choice([self.n, self.n+1])

    #no changes here
    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2*self.n:
            self.state += 1


    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1
    #a little change here:

    def makeDecision(self):
        if self.state <= self.n:
            return "yes"
        else:
            return "no"


yes_no_count=[0,0]

env = Environment(0.2, 2)

la1 = Tsetlin(3)
la2 = Tsetlin(3)
la3 = Tsetlin(3)
la4= Tsetlin(3)
la5= Tsetlin(3)

for i in range(5):
    word1=la1.makeDecision()
    word2=la2.makeDecision()
    word3=la3.makeDecision()
    word4=la4.makeDecision()
    word5=la5.makeDecision()

    yes_and_no=[word1, word2, word3, word4, word5]
    print("\n")
    print(yes_and_no)
    print("\n")
    counter=yes_and_no.count("yes")
    print("Counter", counter)
    penalty_for_la1 = env.penalty(word1, counter)
    penalty_for_la2 = env.penalty(word2, counter)
    penalty_for_la3 = env.penalty(word3, counter)
    penalty_for_la4 = env.penalty(word4, counter)
    penalty_for_la5 = env.penalty(word5, counter)
    
    if penalty_for_la1:
        print("Penalty", end = ' ')
        la1.penalize()
    else:
        print("Reward", end = ' ')
        la1.reward()
  

    if penalty_for_la2:
        print("Penalty", end = ' ')
        la2.penalize()
    else:
        print("Reward", end = ' ')
        la2.reward()
    if penalty_for_la3:
        print("Penalty", end = ' ')
        la3.penalize()
    else:
        print("Reward", end = ' ')
        la3.reward()
    if penalty_for_la4:
        print("Penalty", end = ' ')
        la2.penalize()
    else:
        print("Reward", end = ' ')
        la4.reward()
    if penalty_for_la5:
        print("Penalty", end = ' ')
        la5.penalize()
    else:
        print("Reward", end = ' ')
        la5.reward()

