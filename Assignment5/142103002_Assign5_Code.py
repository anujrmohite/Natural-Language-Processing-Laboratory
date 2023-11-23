import nltk
from nltk.parse.dependencygraph import DependencyGraph
from enum import Enum
import random
import sys


# Enum to represent different transition types
class Transition(Enum):
    SHIFT = 1
    LEFT_ARC = 2
    RIGHT_ARC = 3
    REDUCE = 4


# Class representing the state of the parser
class ParserState:
    def __init__(self, sentence):
        # Initialize the stack with a tuple for ROOT
        self.stack = [("ROOT", 0)]
        self.buffer = list(enumerate(nltk.word_tokenize(sentence), start=1))
        self.dependencies = []

    def shift(self):
        # Move a word from the buffer to the stack
        self.stack.append(self.buffer.pop(0))

    def left_arc(self):
        # Add a left arc relation and pop the second topmost item from the stack
        dependent = self.stack[-2]
        head = self.stack[-1]
        self.dependencies.append((dependent[1], "left", head[1]))
        self.stack.pop(-2)

    def right_arc(self):
        # Add a right arc relation and pop the topmost item from the stack
        head = self.stack[-2]
        dependent = self.stack[-1]
        self.dependencies.append((dependent[1], "right", head[1]))
        self.stack.pop()

    def reduce(self):
        # Pop the topmost item from the stack
        self.stack.pop()

    def is_final_state(self):
        # Check if the parser has reached the final state
        return len(self.stack) == 1 and not self.buffer


# Class representing a transition-based dependency parser
class TransitionBasedDependencyParser:
    def __init__(self):
        pass

    def parse(self, sentence):
        # Initialize the parser state
        state = ParserState(sentence)
        transitions = []

        # Perform transitions until the final state is reached
        while not state.is_final_state():
            # Choose the next transition based on the state of the parser
            if len(state.stack) > 1 and not state.buffer:
                transition = Transition.REDUCE
            elif len(state.stack) > 1 and random.choice([True, False]):
                transition = random.choice([Transition.LEFT_ARC, Transition.RIGHT_ARC])
            else:
                transition = Transition.SHIFT

            # Record the chosen transition
            transitions.append(transition.name)

            # Perform the chosen transition
            if transition == Transition.SHIFT:
                state.shift()
            elif transition == Transition.LEFT_ARC:
                state.left_arc()
            elif transition == Transition.RIGHT_ARC:
                state.right_arc()
            elif transition == Transition.REDUCE:
                state.reduce()

        # Return the resulting dependencies and the sequence of transitions
        return state.dependencies, transitions


# Redirect stdout to the output file
sys.stdout = open("142103002-No_Assign5_Output.txt", "w")

# Example usage:
parser = TransitionBasedDependencyParser()
sentence = "The quick brown fox jumps over the lazy dog."
dependencies, transitions = parser.parse(sentence)

# Print the resulting dependencies and transitions
print("Dependencies:")
for dep in dependencies:
    print(dep)

print("\nTransitions:")
for trans in transitions:
    print(trans)

# Close the file
sys.stdout.close()
