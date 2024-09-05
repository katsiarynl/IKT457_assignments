from random import random 
patients = [
    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": False, "Inv-Nodes 3-5":True, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True, 
     "Recurrence": True},
    {"Menopause lt40": True, "Menopause ge40": False, "Menopause premeno": False, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True, 
     "Recurrence": False},
    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": False, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": True, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True, 
     "Recurrence": True},
    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": True, "Deg-malig 3": False, 
     "Recurrence": False},
    {"Menopause lt40": False, "Menopause ge40": False, "Menopause premeno": True, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True, 
     "Recurrence": True},
    {"Menopause lt40": False, "Menopause ge40": False, "Menopause premeno": True, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": True, "Deg-malig 2": False, "Deg-malig 3": False, 
     "Recurrence": False},


]



def evaluate_condition(observation, condition):
    truth_value_of_condition = True
    for feature in observation:
        if feature in condition and observation[feature] == False:
            truth_value_of_condition = False
            break
        if 'NOT ' + feature in condition and observation[feature] == True:
            truth_value_of_condition = False
            break
    return truth_value_of_condition


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



car_rule = Memory(0.9, 0.1, {'Menopause lt40':0, 'Menopause ge40':0, 'Menopause premeno':0, 
                             'NOT Menopause lt40':0, 'NOT Menopause ge40':0, 'NOT Menopause premeno':0, 
                             'Inv-Nodes 0-2': 10, 'Inv-Nodes 3-5':0, 'Inv-Nodes 6-8':0, 
                             'NOT Inv-Nodes 0-2':0, 'NOT Inv-Nodes 3-5': 10, 'NOT Inv-Nodes 6-8': 10, 
                             'Deg-malig 1':0, 'Deg-malig 2': 5, 'Deg-malig 3':0,
                             'NOT Deg-malig 1':0, 'NOT Deg-malig 2':0, 'NOT Deg-malig 3':0,
                            #  'Recurrence':0,
                            #  'NOT Recurrence':4,
                             })


# print("IF " + " AND ".join(car_rule.get_condition()) + " THEN Recurrence")

# print(evaluate_condition(patients[1], car_rule.get_condition()))

# print(car_rule.memory)
# car_rule.memorize('Deg-malig 2')
# print("\n")
# car_rule.memorize('Deg-malig 2')
# car_rule.memorize("Deg-malig 2")
# print(car_rule.memory)