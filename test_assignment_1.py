import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

#Probability of penalty 
# P(0)=1
# P(1)=0.8
# P(2)=0.6
# P(3)=0.4
# P(4)= 0.6
# P(5)=0.8

class Environment:
    def __init__(self, penalty_probability):
        self.penalty_probability = penalty_probability

    def penalty(self, counter, ta):
        random_value = random.random()
        if counter >= 0 and counter < 4:
            self.penalty_probability = 1 - (counter * 0.2)
            if random_value <= self.penalty_probability:
                return True
            else:
                return False

        if counter == 4 or counter == 5:
            self.penalty_probability = 1 - (0.6 - (counter - 3) * 0.2)
            if random_value <= self.penalty_probability:
                return True
            else:
                return False

class Tsetlin:
    def __init__(self, n):
        self.n = n
        self.state = random.choice([self.n, self.n + 1])

    def reward(self):
        if self.state <= self.n and self.state > 1:
            self.state -= 1
        elif self.state > self.n and self.state < 2 * self.n:
            self.state += 1

    def penalize(self):
        if self.state <= self.n:
            self.state += 1
        elif self.state > self.n:
            self.state -= 1

    def makeDecision(self):
        if self.state <= self.n:
            return "yes"
        else:
            return "no"

env = Environment(1)

la1 = Tsetlin(3)
la2 = Tsetlin(3)
la3 = Tsetlin(3)
la4 = Tsetlin(3)
la5 = Tsetlin(3)
array = []

fig, ax = plt.subplots()
bins = np.arange(0, 7) - 0.5  # To center the bins around integers
ax.set_xlim(-0.5, 5.5)
ax.set_ylim(0, 100)  # Adjust the y-axis limit as needed
ax.set_xlabel("Number of TA saying yes")
ax.set_ylabel("Frequency")
ax.set_title("Histogram of Yes Counts Over Iterations")
bars = ax.hist([], bins=bins, edgecolor="black")[2]

def update_hist(num):
    word1 = la1.makeDecision()
    word2 = la2.makeDecision()
    word3 = la3.makeDecision()
    word4 = la4.makeDecision()
    word5 = la5.makeDecision()

    yes_and_no = [word1, word2, word3, word4, word5]
    counter = yes_and_no.count("yes")
    array.append(counter)

    penalty_for_la1 = env.penalty(counter, "LA1")
    penalty_for_la2 = env.penalty(counter, "LA2")
    penalty_for_la3 = env.penalty(counter, "LA3")
    penalty_for_la4 = env.penalty(counter, "LA4")
    penalty_for_la5 = env.penalty(counter, "LA5")

    if penalty_for_la1:
        la1.penalize()
    else:
        la1.reward()

    if penalty_for_la2:
        la2.penalize()
    else:
        la2.reward()

    if penalty_for_la3:
        la3.penalize()
    else:
        la3.reward()

    if penalty_for_la4:
        la4.penalize()
    else:
        la4.reward()

    if penalty_for_la5:
        la5.penalize()
    else:
        la5.reward()

    ax.cla()  # Clear the previous histogram
    ax.hist(array, bins=bins, edgecolor="black")
    ax.set_xlim(-0.5, 5.5)
    ax.set_ylim(0, 100)
    ax.set_xlabel("Number of TA saying yes")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram")


number_of_frames=101
ani = FuncAnimation(fig, update_hist, frames=number_of_frames-1, repeat=False, interval=200)

plt.show()


y = array
x = range(number_of_frames)

plt.title("Graph")
plt.plot(x, y, color="red")

plt.xlabel("Loop")
plt.ylabel("Number of TA saying yes")
plt.show()


