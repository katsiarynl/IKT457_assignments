import random
import matplotlib.pyplot as plt
import numpy as np
class Environment:
    def __init__(self, penalty_probability):
        self.penalty_probability = penalty_probability #probability of receiving a punishment regardless of the action
         
    
    #! changes have to be done here:
    def penalty(self, counter, ta):
        random_value=random.random()
        if counter>=0 and counter<4: 
           
            self.penalty_probability=1-(counter*0.2)

            print("Random number is", ta, "is", random_value, "\n")
            print("Penalty prob for", ta, "is", self.penalty_probability, "\n")
            if random_value <= self.penalty_probability:
                    return True
            else:
                    return False
        
        if counter==4 or counter==5:
            self.penalty_probability=1-(0.6-(counter-3)*0.2)
            print("Penalty prob for", ta, "is", self.penalty_probability, "\n")
            if random_value <= self.penalty_probability:
                    return True
            else:
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

env = Environment(1)

la1 = Tsetlin(3)
la2 = Tsetlin(3)
la3 = Tsetlin(3)
la4= Tsetlin(3)
la5= Tsetlin(3)
array=[]

for i in range(100):
    word1=la1.makeDecision()
    word2=la2.makeDecision()
    word3=la3.makeDecision()
    word4=la4.makeDecision()
    word5=la5.makeDecision()

    yes_and_no=[word1, word2, word3, word4, word5]
    print("=========Loop ",i,"==========\n")
    print(yes_and_no)
 
    counter=yes_and_no.count("yes")
    array.append(counter)
    print("Counter: ", counter, "\n")
    print("^^^^^^^^^^^^^^^^^^^\n")
    penalty_for_la1 = env.penalty(counter, "LA1")
    penalty_for_la2 = env.penalty(counter, "LA2")
    penalty_for_la3 = env.penalty(counter, "LA3")
    penalty_for_la4 = env.penalty(counter, "LA4") 
    penalty_for_la5 = env.penalty(counter, "LA5")
    print("^^^^^^^^^^^^^^^^^^^\n")
  
         
    if penalty_for_la1:
        print("Penalty for LA1", end = ' ')
        la1.penalize()
    else:
        print("Reward for LA1", end = ' ')
        la1.reward()
  

    if penalty_for_la2:
        print("Penalty for LA2", penalty_for_la2, end = ' ')
        la2.penalize()
    else:
        print("Reward for LA2", end = ' ')
        la2.reward()

    if penalty_for_la3:
        print("Penalty for LA3", end = ' ')
        la3.penalize()
    else:
        print("Penalty for LA3", end = ' ')
        la3.reward()


    if penalty_for_la4:
        print("Penalty for LA4", end = ' ')
        la4.penalize()
    else:
        print("Reward for LA4", end = ' ')
        la4.reward()

    if penalty_for_la5:
        print("Penalty for LA5", end = ' ')
        la5.penalize()
    else:
        print("Reward for LA5", end = ' ')
        la5.reward()
    
    print("\n")
    print("===================\n")





# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# y = array
# x = range(100)

# plt.title("Line graph")
# plt.plot(x, y, color="red")

# plt.xlabel("Loop")
# plt.ylabel("Number of TA saying yes")
# plt.show()