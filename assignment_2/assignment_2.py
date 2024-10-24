import numpy 
from random import random
def booleanize(value): 
    if (value=="lt40"):
        return [True, False, False]
    if (value=="ge40"):
        return [False, True, False ]
    if (value=="premeno"):
        return [False, False, True]
    if (value=="0-2"): 
        return [True, False, False]
    if (value=="3-5"):
        return [False, True, False]
    if (value=="6-8"):
        return [False, False, True]
    if (value==1): 
        return [True, False, False]
    if (value==2):
        return [False, True, False]
    if (value==3):
        return [False, False, True]
    if (value=="yes"):
        return True
    if (value=="no"):
        return False

#Boolenization
patients = [
    {"Menopause": booleanize("ge40"), "Inv-Nodes": booleanize("3-5"), "Deg-malig": booleanize(3), "Recurrence": booleanize("yes")},
    {"Menopause": booleanize("lt40"), "Inv-Nodes": booleanize("0-2"), "Deg-malig": booleanize(3), "Recurrence": booleanize("no")},
    {"Menopause": booleanize("ge40"), "Inv-Nodes": booleanize("6-8"), "Deg-malig": booleanize(3), "Recurrence": booleanize("yes")},
    {"Menopause": booleanize("ge40"), "Inv-Nodes": booleanize("0-2"), "Deg-malig": booleanize(2), "Recurrence": booleanize("no")},
    {"Menopause": booleanize("premeno"), "Inv-Nodes": booleanize("0-2"), "Deg-malig": booleanize(3), "Recurrence": booleanize("yes")},
    {"Menopause": booleanize("premeno"), "Inv-Nodes": booleanize("0-2"), "Deg-malig": booleanize(1), "Recurrence": booleanize("no")}

]

test_observation=["ge40"]
print(patients[0])



def negate(value):
    return 0
   

def simplify():
    return 0

def evaluate_condition(observation, condition):
    truth_value_of_condition = True

    for feature in observation:
        # print(patients[0], "Menopause")
        print(observation)
    
        if len(feature)==1:
          if feature in condition and observation[feature] == False:
             truth_value_of_condition = False
             break
          if 'NOT ' + feature in condition and observation[feature] == True:
             truth_value_of_condition = False
             break
    return truth_value_of_condition

example_condition = [[False, True, False], [True, False, False], [False, False, True], False]

print(evaluate_condition(patients[0], "geo40" ))


class Memory:
    def __init__(self, forget_value, memorize_value, memory):
        self.memory = memory
        self.forget_value = forget_value
        self.memorize_value = memorize_value
    
    def get_memory(self):
        return self.memory
    
    def get_literals(self):
        return list(self.memory.keys())
    
    def get_condition(self):
        condition = []
        for literal in self.memory:
            if self.memory[literal] >= 6:
                condition.append(literal)
        return condition
        
    def memorize(self, literal):
        if random() <= self.memorize_value and self.memory[literal] < 10:
            self.memory[literal] += 1
            
    def forget(self, literal):
        if random() <= self.forget_value and self.memory[literal] > 1:
            self.memory[literal] -= 1
            
    def memorize_always(self, literal):
        if  self.memory[literal] < 10:
            self.memory[literal] += 1




