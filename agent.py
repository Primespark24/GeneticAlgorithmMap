# Brycen Martin, Jonathan Laughlin and Shane Snediker
# Dr. Jones CS473
# Genetic Algorithm Final Project
# Updated December 17, 2020


import random   # Used for randomly seeding DNA
import copy     # Used to create deep copies of variables
import math     # Used to calculate distance

# Agent class
# This class contains all data pertaining to the individual agents that will be navigating the problem space
class Agent:

    #########################################
    #### Class Attributes 
    #########################################

    current_orientation = 0          # Specifies which direction the agent is facing, utilizing unit circle degrees
    previous_position_map = [1,1]    # Store the agent's previous position to repaint gray on the screen. In the form of [x,y]
    current_position_map = [1,1]     # Variable holding the agent's current position, which will begin initialized to a specific location in the city. In the form of [x,y]
    previous_position_city = [0,4,4] # Store the agent's previous position in the Spokane street array. In the form of [row, column, intersection]
    current_position_city = [0,4,4]  # Variable holding the agent's current position in the Spokane street array. In the form of [row, column, intersection]
    DNA_length = 500                 # Variable representing the length of an agent's DNA structure
    fitness_score = 0                # Stores the agent's overall fitness score computed after the final movement
    DNA_mutate_strand = (DNA_length // 10) # A holder variable that captures an integer value representing 10 percent of an agent's DNA
    Deliv_reached = False            # Flag that captures the moment when an agent reaches the delivery location

    #########################################
    #### Class Methods 
    #########################################

    # Agent constructor includes two implementations of agents
    # One for the first generation, and one for subsequent generations
    # Parameters:  city: a city object that this agent will be connected to
    #              dna_length: an integer representing this agent's DNA sequence length
    #              DNA_array: a list of string values representing this agent's genes
    def __init__(self, city, dna_length, DNA_array = None):
        # Overloading constructors in Python involves handling all possible
        # instances of the constructor within 1 method
        # We begin by establishing 2 variables that every agent will have
        # An integer variable holding the length of their DNA structure
        self.DNA_length = dna_length
        # And a DNA array to hold their DNA sequence (which is really a list of actions that the agent will take)
        self.DNA = [] 
        # Now we start with the first implementation: the case where we are
        # initializing the seed population by giving them a random DNA sequence
        # This is the implementation that is used because when calling the constructor 
        # you do not include the DNA-array parameter
        if DNA_array == None:
            # generate random actions/movements to seed the first generation
            for _ in range(self.DNA_length):
                #self.DNA.append(random.choice(['N', 'S', 'E', 'W']))
                self.DNA.append(random.choice( ['L', 'F', 'R', 'B']))
        # Now we turn to the secondary implementaiton for agents which happens
        # during reproduction when a new child is born
        else:
            # Another constructor to be used in the crossover function for creating new agents
            # This constructor takes an array of DNA resulting from reproduction between 2 parents
            self.DNA = DNA_array    # Give this agent his new DNA sequence
        # spawn the agent at the start of the city
        self.current_position_map= copy.deepcopy(city.BEGIN_LOC)
        self.previous_position_map = copy.deepcopy(city.DELIVERY_LOC)
        self.Deliv_reached = False

    # Update the agent's orientation according to which direction it turns
    # Parameters:  dir: A char containing one of 3 directions ('L' for left, 'R' for right, or 'F' for straight forward, and 'B' for u-turn)
    def turn(self,dir):
        # Degrees updated based on unit circle orientation

        # If this turn is left, then we need to add 90 degrees to the agent's current orientation
        if dir == 'N':
            self.current_orientation += 90
        # If this turn is right, then we need to subtract 90 degrees from the agent's current orientation    
        elif dir == 'S':
            self.current_orientation -= 90
        elif dir == 'E':
            self.current_orientation -= 180
        # If the agent turned a full 360 degrees, reset to 0
        if self.current_orientation == 360 or self.current_orientation == -360:
            self.current_orientation = 0 
    
    
    # Calculates the next position if movement can be carried out
    # Parameter:  action: A char representing the agent's next directional movement
    #             city: A City object that the bot is traversing
    # Return:     next_pos_city: A list containing the coordinates within the Spokane street array where the bot will move next
    #             next_pos_map: A list containing the coordinates within the popup screen where the bot will move next
    #             changed_position: A boolean flag signifying whether or not the bot was permitted to make a move
    def calculate_next_pos(self, action, city):
        # Begin by setting next position variable equal to the agent's current position
        # next_pos_city is an array with the first element tracking the EAST/WEST street that the bot is on, the second
        # element tracking the NORTH/SOUTH street that the bot is on, and the 3rd element tracking the direction the bot is facing (N,S,E, or W).
        # next_pos_map is a list corresponding to the popup screen where the first index corresponds to the bot's x coordinate and
        # the second index corresponds to the bot's y coordinate. Start the agent at the current position and make modifications from there
        next_pos_map = copy.deepcopy(self.current_position_map)
        next_pos_city = copy.deepcopy(self.current_position_city)
        changed_position = False

        # This function basically tracks where the robot is at within the Spokane City street array and allows
        # it to move if and only if there is an open street in the direction that it is wanting to move

        # If the agent is currently facing WEST, determine its next position based on its next genetic sequence
        # and whether westward movement is open
        # NOTE: WEST is up on the printed screen
        # Bot wants to go West, is that direction open?
        if action == 'F':#'W':
            if(self.current_position_city[2] == 4):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][3]):
                    next_pos_city[2] = 3
                    next_pos_map[1] -= 1
                    changed_position = True
            elif(self.current_position_city[2] == 3):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]-1][2]):
                    next_pos_city[1] -= 1
                    next_pos_city[2] = 2
                    next_pos_map[1] -= 1
                    changed_position = True
            elif(self.current_position_city[2] == 2):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][4]):
                    next_pos_city[2] = 4 
                    next_pos_map[1] -= 1
                    changed_position = True
        # If the agent is currently facing EAST, determine its next position based on its next genetic sequence 
        # and whether eastward movement is open
        # NOTE: EAST is down on the printed screen
        # Bot wants to go East, is that direction open?
        elif action == 'B':#'E':
            if(self.current_position_city[2] == 4):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][2] and self.current_position_city[1] != len(city.CITY_GRID[0])-1):
                    next_pos_city[2] = 2
                    next_pos_map[1] += 1
                    changed_position = True
            elif(self.current_position_city[2] == 3):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][4]):
                    next_pos_city[2] = 4
                    next_pos_map[1] += 1
                    changed_position = True
            elif(self.current_position_city[2] == 2):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]+1][3] ):
                    next_pos_city[1] += 1
                    next_pos_city[2] = 3 
                    next_pos_map[1] += 1
                    changed_position = True
        # If the agent is currently facing NORTH, determine its next position based on its next genetic sequence 
        # and whether northward movement is open
        # NOTE: NORTH is left on the printed screen
        # Bot wants to go North, is that direction open?
        elif action == 'L':#'N':
            if(self.current_position_city[2] == 4):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][0]):
                    next_pos_city[2] = 0
                    next_pos_map[0] -= 1
                    changed_position = True
            elif(self.current_position_city[2] == 0):
                if(city.CITY_GRID[self.current_position_city[0]-1][self.current_position_city[1]][1] and self.current_position_city[0] != 0):
                    next_pos_city[0] -= 1
                    next_pos_city[2] = 1
                    next_pos_map[0] -= 1
                    changed_position = True
            elif(self.current_position_city[2] == 1):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][4]):
                    next_pos_city[2] = 4
                    next_pos_map[0] -= 1
                    changed_position = True
        # If the agent is currently facing SOUTH, determine its next position based on its next genetic sequence 
        # and whether Southward movement is open
        # NOTE: SOUTH is right on the printed screen
        # Bot wants to go South, is that direction open?            
        elif action == 'R':#'S':
            if(self.current_position_city[2] == 4):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][1]):
                    next_pos_city[2] = 1
                    next_pos_map[0] += 1
                    changed_position = True
            elif(self.current_position_city[2] == 1):
                if(city.CITY_GRID[self.current_position_city[0]+1][self.current_position_city[1]][0]):
                    next_pos_city[0] += 1
                    next_pos_city[2] = 0
                    next_pos_map[0] += 1
                    changed_position = True
            elif(self.current_position_city[2] == 0):
                if(city.CITY_GRID[self.current_position_city[0]][self.current_position_city[1]][4]):
                    next_pos_city[2] = 4
                    next_pos_map[0] += 1
                    changed_position = True
        return next_pos_city, next_pos_map, changed_position

    # Function that moves the agent to its next position if a wall is not present
    # Parameters: action_iterator: An integer to iterate through the agent's DNA structure
    #             city: 2D city array that the agent is navigating
    # Return:     changed_position: the next city location where the agent will step to
    def move(self, action_iterator, city):
        # Establish a boolean flag that stores whether or not the agent has changed position, assume no movement
        changed_position = False
        # Determine next position by capturing the next gene representing a directional movement
        action = self.DNA[action_iterator]
        # Calculate the next position of this agent based on the DNA instruction
        #print(city.DELIVERY_LOC)
        if(not self.Deliv_reached):
            next_position_city,next_position_map,changed_position = self.calculate_next_pos(action,city)
        
            # If agent makes it to exit, increase fitness score to incentivize getting there ASAP
            if (self.current_position_map[0] == city.DELIVERY_LOC[0] and self.current_position_map[1] == city.DELIVERY_LOC[1]) or (next_position_city[0] == city.DELIVERY_LOC[0] and next_position_city[1] == city.DELIVERY_LOC[1]):
                # for every round of movement before the end of the DNA, add points per "saved" action
                self.Deliv_reached = True
                self.fitness_score += 50
        # If the bot moved, update its positioning
        if(changed_position):
            self.previous_position_map = copy.deepcopy(self.current_position_map)
            self.current_position_map = copy.deepcopy(next_position_map)
            self.previous_position_city = copy.deepcopy(self.current_position_city)
            self.current_position_city = copy.deepcopy(next_position_city)
        
        # Regardless of if the agents changed positions, update its orientation accordingly
        self.turn(action)  
        # Return the flag status of this movement
        return changed_position

    # Function that gives definition to an agent's DNA mutation
    # In this implementation, we use a new DNA sequence version 
    # of DNA mutation where we take a DNA strand that is a 
    # predetermined percentage of an agent's total DNA size and 
    # we remove it, replacing it with a new random sequence of DNA.
    # Our current predetermined DNA mutation strand percentage 
    # (represented by DNA_mutate_strand) is 10%
    # No parameters
    # Return: self: the mutated agent
    def mutate(self):
        # We need to find a random starting index within this agent's DNA strand to begin the mutation
        # We declare a variable that captures a random integer.  This random integer has to be 
        # less than the difference between the length of the agent's DNA strand and the length
        # of the mutating strand so that we can mutate from any random index within the DNA sequence
        start_index = random.randint(0, (len(self.DNA) - self.DNA_mutate_strand))
        
        # Initialize an array that will hold the new DNA mutation sequence
        mutation_sequence = []

        # First let's create a brand new random sequence of DNA instructions of size DNA_mutate_strand
        for _ in range(self.DNA_mutate_strand):
            mutation_sequence.append(random.choice(['N', 'S', 'E', 'W']))

        # Now we replace the mutation strand of the agent with the new mutated values
        # We need our iterator to start at zero on account of array indices beginning at zero
        i = 0
        # Initialize a loop that will iterate once for every gene in the mutation strand
        for i in range(self.DNA_mutate_strand - 1):
            # Replace the current gene value with the new mutated value
            self.DNA[(start_index + i)] = mutation_sequence[i]

        # return the mutated agent
        return self

    # Test function to display DNA
    def print_DNA(self):
        print(self.DNA)

    # Function that calculates an agent's fitness at the conclusion of a generation of city navigating
    # Parameters:  city: 2D array that the agent is navigating
    def calculate_fitness(self, city):
        
        # Use the distance formula to calculate fitness.  Not necessary to calculate the square root,
        # however because all that is needed is a relative distance
        distance = (abs(city.DELIVERY_LOC[1] - self.current_position_map[1])) + (abs(city.DELIVERY_LOC[0] - self.current_position_map[0]) )

        # To avoid getting caught by a local minimum situation, let's give a bonus to 
        # agents that at least make it half way to their delivery location
        half_distance = (abs(city.DELIVERY_LOC[1] - city.BEGIN_LOC[1])) + (abs(city.DELIVERY_LOC[0] - city.BEGIN_LOC[0]) // 2)
        if distance > half_distance:
           distance -= 5
        
        # Now we pick an arbitrary number to subtract our current fitness score (distance) 
        # from this number to ensure that fitness scores will increase in value.
        # Because the distance calculated above favors smaller distances, we use this 
        # calculation to invert the values so that shorter distances from the city exit
        # are reflected with higher fitness scores
        self.fitness_score += (200 - distance)