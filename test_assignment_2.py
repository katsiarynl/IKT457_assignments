from random import random 
from random import choice

patients_with_recurrence = [
    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": False, "Inv-Nodes 3-5":True, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True
     },


    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": False, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": True, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True},


    {"Menopause lt40": False, "Menopause ge40": False, "Menopause premeno": True, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True},
     

]

patients_no_recurrence = [

    {"Menopause lt40": True, "Menopause ge40": False, "Menopause premeno": False, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": False, "Deg-malig 3": True},

    {"Menopause lt40": False, "Menopause ge40": True, "Menopause premeno": False, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": False, "Deg-malig 2": True, "Deg-malig 3": False},

    {"Menopause lt40": False, "Menopause ge40": False, "Menopause premeno": True, 
     "Inv-Nodes 0-2": True, "Inv-Nodes 3-5":False, "Inv-Nodes 6-8": False, 
     "Deg-malig 1": True, "Deg-malig 2": False, "Deg-malig 3": False},

]



def evaluate_condition(observation, condition):
    truth_value_of_condition = True
    # print("The observation is", observation)
    # print("The condition is ", condition)
    for feature in observation:
        if feature in condition and observation[feature] == False:
            # print("The truth value of condition is False")
            truth_value_of_condition = False
            break
        if 'NOT ' + feature in condition and observation[feature] == True:
            truth_value_of_condition = False
            # print("The truth value of condition is False")
            break
        # print("The truth value is true")
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


# Recurrence rules
rule_1=  Memory(0.2, 0.8, {'Menopause lt40':1, 'Menopause ge40':1, 'Menopause premeno':1, 
                             'NOT Menopause lt40':10, 'NOT Menopause ge40':1, 'NOT Menopause premeno':1, 
                             'Inv-Nodes 0-2': 1, 'Inv-Nodes 3-5':1, 'Inv-Nodes 6-8':1, 
                             'NOT Inv-Nodes 0-2':1, 'NOT Inv-Nodes 3-5': 1, 'NOT Inv-Nodes 6-8': 1, 
                             'Deg-malig 1':1, 'Deg-malig 2': 1, 'Deg-malig 3':10,
                             'NOT Deg-malig 1':1, 'NOT Deg-malig 2':1, 'NOT Deg-malig 3':1,
                         
                             })

rule_2=  Memory(0.2, 0.8, {'Menopause lt40':1, 'Menopause ge40':1, 'Menopause premeno':1, 
                             'NOT Menopause lt40': 1, 'NOT Menopause ge40': 1, 'NOT Menopause premeno':1, 
                             'Inv-Nodes 0-2': 1, 'Inv-Nodes 3-5':1, 'Inv-Nodes 6-8':1, 
                             'NOT Inv-Nodes 0-2':1, 'NOT Inv-Nodes 3-5': 1, 'NOT Inv-Nodes 6-8': 1, 
                             'Deg-malig 1':1, 'Deg-malig 2': 1, 'Deg-malig 3':10,
                             'NOT Deg-malig 1':1, 'NOT Deg-malig 2':1, 'NOT Deg-malig 3':1,
                         
                             })

# Non-recurrence rule
rule_3 = Memory(0.2, 0.8, {'Menopause lt40':1, 'Menopause ge40':1, 'Menopause premeno':1, 
                             'NOT Menopause lt40':1, 'NOT Menopause ge40':1, 'NOT Menopause premeno':1, 
                             'Inv-Nodes 0-2': 10, 'Inv-Nodes 3-5':1, 'Inv-Nodes 6-8':1, 
                             'NOT Inv-Nodes 0-2': 1, 'NOT Inv-Nodes 3-5': 1, 'NOT Inv-Nodes 6-8': 1, 
                             'Deg-malig 1':1, 'Deg-malig 2': 1, 'Deg-malig 3':1,
                             'NOT Deg-malig 1':1, 'NOT Deg-malig 2':1, 'NOT Deg-malig 3':1,
                    
                             })

rule_4_recurrence = Memory(0.2, 0.8, {'Menopause lt40':5, 'Menopause ge40':5, 'Menopause premeno':5, 
                             'NOT Menopause lt40':5, 'NOT Menopause ge40':5, 'NOT Menopause premeno':5, 
                             'Inv-Nodes 0-2': 5, 'Inv-Nodes 3-5':5, 'Inv-Nodes 6-8':5, 
                             'NOT Inv-Nodes 0-2': 5, 'NOT Inv-Nodes 3-5': 5, 'NOT Inv-Nodes 6-8': 5, 
                             'Deg-malig 1':5, 'Deg-malig 2': 5, 'Deg-malig 3':5,
                             'NOT Deg-malig 1':5, 'NOT Deg-malig 2':5, 'NOT Deg-malig 3':5,
                    
                             })


rule_5_recurrence = Memory(0.2, 0.8, {'Menopause lt40':5, 'Menopause ge40':5, 'Menopause premeno':5, 
                             'NOT Menopause lt40':5, 'NOT Menopause ge40':5, 'NOT Menopause premeno':5, 
                             'Inv-Nodes 0-2': 5, 'Inv-Nodes 3-5':5, 'Inv-Nodes 6-8':5, 
                             'NOT Inv-Nodes 0-2': 5, 'NOT Inv-Nodes 3-5': 5, 'NOT Inv-Nodes 6-8': 5, 
                             'Deg-malig 1':5, 'Deg-malig 2': 5, 'Deg-malig 3':5,
                             'NOT Deg-malig 1':5, 'NOT Deg-malig 2':5, 'NOT Deg-malig 3':5,
                    
                             })





def type_i_feedback(observation, memory):
    remaining_literals = memory.get_literals()
    if evaluate_condition(observation, memory.get_condition()) == True:
        for feature in observation:
            #print("Working here")
            
            if observation[feature] == True:
                # print("Case 1")
                memory.memorize(feature)
                remaining_literals.remove(feature)
            elif observation[feature] == False:
                # print("Case 2")
                memory.memorize('NOT ' + feature)
                remaining_literals.remove('NOT ' + feature)
            # print(remaining_literals)
            # print("\n=================")
    for literal in remaining_literals:
        memory.forget(literal)


def type_ii_feedback(observation, memory):
    if evaluate_condition(observation, memory.get_condition()) == True:
        for feature in observation:
            if observation[feature] == False:
                memory.memorize_always(feature)
            elif observation[feature] == True:
                memory.memorize_always('NOT ' + feature)


def classify(observation, car_rules, plane_rules):
    vote_sum = 0
    for car_rule in car_rules:
        if evaluate_condition(observation, car_rule.get_condition()) == True:
            vote_sum += 1
    for plane_rule in plane_rules:
        if evaluate_condition(observation, plane_rule.get_condition()) == True:
            vote_sum -= 1
    if vote_sum >= 0:
        return "Recurrence"
    else:
        return "No Recurrence"


#print("==========Initial Memory=========")
#print(rule_1.get_memory())
#Mixing type 1 and type 2 feedback for rule 1
for i in range(100):
    #print("========================= ", i,"=========================")
    observation_id = choice([0,1,2])
   # print("The random observation is", observation_id)
    recurrence = choice([0,1])
   # print("The recurrence is", recurrence)
    if recurrence == 1:
        type_i_feedback(patients_with_recurrence[observation_id], rule_4_recurrence)
    else:
        type_ii_feedback(patients_no_recurrence[observation_id], rule_4_recurrence)



#Mixing type 1 and type 2 feedback for rule 2
#         
for i in range(100):
    observation_id = choice([0,1,2])
    recurrence = choice([0,1])
    if recurrence == 1:
        type_i_feedback(patients_with_recurrence[observation_id], rule_5_recurrence)
    else:
        type_ii_feedback(patients_no_recurrence[observation_id], rule_5_recurrence)








print("=========Rule 1==========")
print("IF " + " AND ".join(rule_1.get_condition()) + " THEN Recurrence")
print("=========Rule 2==========")
print("IF " + " AND ".join(rule_2.get_condition()) + " THEN Recurrence")
print("=========Rule 3==========")
print("IF " + " AND ".join(rule_3.get_condition()) + " THEN Non Recurrence")
print("=========Rule 4==========")
print("IF " + " AND ".join(rule_4_recurrence.get_condition()) + " THEN Recurrence")
print("=========Rule 5==========")
print("IF " + " AND ".join(rule_5_recurrence.get_condition()) + " THEN Non Recurrence")


print("===================Classification Recurrence=====================")
print(classify(patients_with_recurrence[0], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))
print(classify(patients_with_recurrence[1], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))
print(classify(patients_with_recurrence[2], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))

print("===================Classification Non Recurrence=====================")
print(classify(patients_no_recurrence[0], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))
print(classify(patients_no_recurrence[1], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))
print(classify(patients_no_recurrence[2], [rule_1, rule_2, rule_4_recurrence], [rule_3, rule_5_recurrence]))
# print(rule_3.get_memory())



