# Brycen Martin, Jonathan Laughlin and Shane Snediker
# Dr. Jones CS473
# Genetic Algorithm Final Project
# Updated December 17, 2020


import City         # Import user defined class that provides graphical city data
import Agent        # Import user defined class that defines individual agents
import pygame       # Import Python library in order to be able to display stats to the screen
import random       # Import Python random library for generating random numbers
import copy         # Import Python copy library for making deep copies
from operator import itemgetter, attrgetter # used in sorting agents by fitness score

# Colors
RED = (255,0,0)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

# Population class
# Class for organizing the agent population and reproduction
class Reproduction:

    #########################################
    #### Class Attributes 
    #########################################

    pop_size = None             # The size of each generation of agents
    Agent_quiver = []           # An array containing the current Agent objects in the population
    number_of_survivors = None  # Value representing the amount of agents left alive after each round of evolution
    global_gen_counter = 1      # A counter that tracks the current generation number
    agent_DNA_length = None     # Store how long the agents DNA strands are
    city = None                 # city object that the population is bound to
    average_fitness = 100       # Double data type representing a generation's average fitness score
    top_score = 120             # Integer representing the generation's highest fitness score
    agent_color = RED           # Defines what color the agent will be displayed as
    mutation_rate = 0.5         # Probability of mutation occuring after crossover

    #########################################
    #### Class Methods 
    #########################################

    # Reproduction constructor to initialize a population of agents to traverse the city
    # Parameters:  size: An integer value representing the amount of agents in this population
    #              city: A city object representing the space that this population will traverse
    #              dna_length: An integer value representing the amount of genes each agent in the population has
    def __init__(self, size, city, dna_length):
        # Give this population's member variables their values based on the population you're instantiating
        self.pop_size = size                    # Amount of agents in this population
        self.number_of_survivors = size // 2    # An integer value representing half of the population
        self.agent_DNA_length = dna_length      # The length of each agent's DNA sequence
        self.city = city                        # Connect this population to the city
        # Fill up the agent list with agents
        for _ in range(size):
            self.Agent_quiver.append(copy.deepcopy(Agent.Agent(self.city, dna_length)))

    # Function that calculates the fitness for every agent in the population
    # Should be called after after each round of movement
    def calculate_fitness(self):
        # Calculate fitness for each individual agent
        for x in range(len(self.Agent_quiver)):
            self.Agent_quiver[x].calculate_fitness(self.city)
        # Sort the agent quiver by fitness scores from lowest at early indices to highest at latter indices
        self.Agent_quiver = sorted(self.Agent_quiver, key = attrgetter('fitness_score'), reverse = False) 
        
    # Function for printing to console the top and average fitness score to monitor evolution progress
    def get_fitness_stats(self, screen):

        # Begin by adding up the sum of all fitness scores for this generation
        sum = 0
        for x in range(self.pop_size):
            sum += self.Agent_quiver[x].fitness_score
        # Capture the average in the average_fitness member variable
        self.average_fitness = sum // self.pop_size
        # Capture the top score in the top_score member variable
        self.top_score = self.Agent_quiver[self.pop_size - 1].fitness_score

        ################### Display stats to the screen #####################

        # Create our font objects to give our display boxes a font and font size
        # The 1st parameter is the font file which pygame contains and the second parameter is the font size
        stats_font = pygame.font.Font('freesansbold.ttf', 24) 
        
        # Create our text surfaces on which our fonts will be applied
        # 1st parameter is what gets written, 2nd is a special pygame antialias boolean
        # that needs to be set to True, the 3rd is the font color, and the 4th is the background color 
        gen_title_text = stats_font.render('Currently featuring generation: ' + str(self.global_gen_counter + 1), True, GREY, BLACK)
        ave_title_text = stats_font.render('Previous generation average fitness: ' + str(self.average_fitness), True, GREY, BLACK)
        top_score_title_text = stats_font.render('Previous generation top score: ' + str(self.top_score), True, GREY, BLACK)

        # Now we create rectangle objects for our text surfaces to be placed in
        gen_title_Rect = gen_title_text.get_rect() 
        ave_title_Rect = ave_title_text.get_rect()
        top_score_title_Rect = top_score_title_text.get_rect()

        # Now we place our rectangles on our city: 1st parameter is the x coordinate of the upper left corner of the rectangle
        # The 2nd parameter is the y coordinate of the upper left corner of the rectangle
        gen_title_Rect.center = (280, 430)
        ave_title_Rect.center = (250 , 460)
        top_score_title_Rect.center = (280 , 490)

        # Finally, we copy the text surfaces to the screen at the rectangle's coordinates
        screen.blit(gen_title_text, gen_title_Rect) 
        screen.blit(ave_title_text, ave_title_Rect)
        screen.blit(top_score_title_text, top_score_title_Rect)
    
    # Function for resetting the population at the city entrance
    # Once a population has completed a generation of movement, reset them to the beginning of the city
    def reset(self, screen):
        for x in range(self.pop_size):
            self.Agent_quiver[x].current_position = self.city.BEGIN_LOC
            self.Agent_quiver[x].current_orientation = self.city.CITY_START_ORIENTATION
            self.Agent_quiver[x].fitness_score = 0
            # Draw all of the agents at the city entrance
            pygame.draw.rect(screen, self.agent_color, [self.city.CELL_SIZE * self.Agent_quiver[x].current_position[0], self.city.CELL_SIZE * self.Agent_quiver[x].current_position[1], self.city.CELL_SIZE, self.city.CELL_SIZE])
        # update what we've drawn
        pygame.display.update()

    # Function that moves every agent in the population one step based on DNA index
    # Parameter:  DNA_index: integer that points to the index of the gene instruction that the population is currently following
    def move(self, DNA_index):
        # Iterate through the agent quiver moving each individual agent
        for x in self.pop_size:
            self.Agent_quiver[x].move(DNA_index,self.city)

    # This method selects the parents for the next generation using Roulette Wheel Selection
    # Implementation details referenced from: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm
    # In this method there is selection pressure towards fitter individuals but there is a chance for any agent to become a parent
    # Return:  A list of integers that point to the indices of the agents in the corresponding Agent_quiver list that will be chosen during crossover reproduction
    def selection(self):
        # Declare a variable to add up all of the fitness scores of the population
        sum = 0
        # Iterate through the population of agents adding up individual fitness scores
        for x in range(len(self.Agent_quiver)):
             sum += self.Agent_quiver[x].fitness_score

        # Recursively generate boundaries between 0 and 1 that split up the number space into probabilites for each agent
        # This way each agent will have certain probability to reproduce with those who have a higher fitness getting a larger chance to mate
        # Begin index zero with a value of 0
        selection_boundaries = [0]
        # Iterate through the population adding an increasing sized float value to each index based on the agents with higher fitness values getting assigned a bigger chunk of the pie
        ## The -1 in the for loop is for the last element whose total rounds to 1 which is added after the loop is completed
        for i in range(len(self.Agent_quiver) - 1):
            # add the previous fitness proportion to the current fitness proportion to get a new boundary
            # What we're really doing here is wieghting each agent's selection probability according to its fitness score
            selection_boundaries.append(selection_boundaries[i] + ((self.Agent_quiver[i].fitness_score)/sum))
        selection_boundaries.append(1)

        # Now we have n boundaries (dividing lines) between 0 and 1 where n = the number of agents
        # The number line between 0 and 1 is split into n different sections in between boundaries corresponding to the probability of selection
        # Now a random float value is chosen between 0 and 1 to see which parents get selected
       
        # List holding the indices that point to selected parents from the original population 
        parent_indices = []
        # Flag used to prevent an agent from mating with itself
        previously_selected_parent = None
        x = 0
        # Begin a loop that will traverse the population
        while x < self.pop_size:
            # This random selection will occur n times where n = population size
            r = random.random()
            # Find the index of the parent that got randomly selected
            selected_parent_index = findClosest(selection_boundaries, len(selection_boundaries), r)

            # Prevent self-mating
            # If same parent is selcted two times in a row, go through loop again to select a new parent
            if (selected_parent_index == previously_selected_parent):
                # decrement loop counter to ensure N parents are selected
                x -= 1
            # else if the selected parent is a different agent then the previously selected agent, add to selection list
            else:
                # Add this index to the list of indices to be selected
                parent_indices.append(selected_parent_index)
                # Update this selected parent to previous selection for the next round
                previously_selected_parent = copy.deepcopy(selected_parent_index)
            # Increment our loop counter
            x += 1
        # return a list of indices pointing to parents in Agent_quiver that should be sequentially iterated through to produce children
        return parent_indices

    # This method removes the least fit agents from the population based on number_of_survivors member variable
    # This method is called each time new children have been created to create room in the population for the children to replace
    def kill_the_weak(self):
        # Let's initialize an array to hold the survivors
        weak = []
        # Now we iterate through the list of fitness sorted agents saving the fittest portion
        for x in range((self.number_of_survivors)):
             weak.append(self.Agent_quiver[x])
        # Kill the weaklings
        for agent in range((self.number_of_survivors)):
            del self.Agent_quiver[agent]

        return weak

    # A function called after killing the weak from the population
    # The function adds children to the fit population to get back up to pop_size
    # Parameter:   children: a list of agents produced from the crossing of parent agents during reproduction
    def add_children(self, children):
        # For as many children as there are in the children list, append a child to the agent quiver
        for x in range(len(children)):
            self.Agent_quiver.append(copy.deepcopy(children[x]))
    
    # Function to define DNA crossover reproduction
    # Because the directional order of an agent's movements will lead to
    # increased fitness within individual agents, we adopt a version
    # of reproduction called ordered crossover.  In ordered crossover,
    # large segments of DNA get chunked together and passed on to successive generations.
    # Throughout this method, we often refer to the first parent in a genetic 
    # combination as p1, and the second parent as p2.
    # Ultimately, in this version of crossover we want to take a DNA strand
    # of random size from p1 plucked from a random location within p1's DNA sequence.
    # We then place the first index of that DNA strand at the same starting index in the new baby agent.
    # At that point we begin filling in the rest of the child's DNA structure with 
    # p2's DNA
    # Return:  new_pop: a list of agents resulting from the mating of selected parent agents
    def crossover(self):
        # We begin by initiating the selection by which the population of agents that has just
        # completed city traversal is assessed based on their fitness score and using probabilities
        # chosen to participate in the reproduction process.  Every agent in the population 
        # has the statistical chance to make it into the selected_parents list, but agents
        # with the higher fitness scores have a higher probability of getting selected

        # Initiate the selection function to choose parents for reproduction
        selected_parents = self.selection()

        self.mutation_rate = .15
        
        # Initialize an array to hold our new crossover generation of children
        new_pop = []
        
        # Now we can start the reproductive process.  This will be a pretty detailed
        # for loop that will iterate through the selected parent list 
        # combining specific DNA segments and genes to create children.
        # Each iteration of the first nested loop combines 2 agents from 
        # the selected_parents list and creates a child.
        # iterator i will follow p1 and j will follow p2
        j = 1
        # The 3rd argument in the range function causes the i iterator to increment by 2 every loop
        # Both i and j iterators need to be incremented by 2 every time because each loop iteration
        # combines parents from neighboring indices two at a time
        for i in range(0, len(selected_parents), 2):
            # Initialize a dynamic array that will hold the specific sequence of DNA
            # from p1 that will be passed to the child
            DNA_holder = []

            # Create a random integer from 50 to the size of an agent's DNA strand
            # We will pull a strand of DNA of this random size from p1
            p1_strand_length = random.randint(50, self.Agent_quiver[selected_parents[i]].DNA_length)

            # Create a random integer from 0 up to the size of p1's DNA genes 
            # that are not getting pulled to represent the index where we will
            # pull the DNA strand from p1 and also the index where we will place 
            # the DNA strand from p1 into the new child DNA structure.
            # In other words, we're going to pluck the random sized DNA
            # segment from p1 beginning at a random location in p1's DNA
            # structure, and the following variable will help us place that same 
            # DNA segment beginning at the same index in the child
            p1_DNA_start_index = random.randint(0, (self.Agent_quiver[selected_parents[i]].DNA_length - p1_strand_length))
            # We need to preserve this starting index despite needing to iterate across it
            # in an upcoming loop, so we establish a deep copy
            p1_DNA_start_index_deepCopy = copy.deepcopy(p1_DNA_start_index)

            # Next we initialize a list that will hold the DNA structure of this new child
            new_child_DNA = []

            # Iterate through the p1 DNA structure capturing a chunk of size p1_strand_length
            # beginning at the random index number catpured in p1_DNA_start_index
            while p1_DNA_start_index_deepCopy < (p1_strand_length + p1_DNA_start_index):
                # Hold the DNA segment of p1. p1 is represented by self.Agent_quiver[selected_parents[i]]
                DNA_holder.append(self.Agent_quiver[selected_parents[i]].DNA[p1_DNA_start_index_deepCopy])
                # Increment the iterator
                p1_DNA_start_index_deepCopy += 1

            # Now that we have p1's DNA accounted for, we need to begin 
            # building the child's DNA structure.
            # We begin inserting into the child DNA structure the DNA strand 
            # from p1 that we've just captured in DNA_holder beginning at the same index as p1
            
            # Recalibrate the index iterating variable
            p1_DNA_start_index_deepCopy = copy.deepcopy(p1_DNA_start_index)
    
            # Declare a counter variable
            k = 0
            # Start a loop that runs as many iterations as the randomized
            # size of p1's DNA strand that we pulled
            while p1_DNA_start_index_deepCopy < (p1_DNA_start_index + p1_strand_length):
                # Add to the child's DNA structure the strand from p1 by inserting it 
                # starting at the same index that the strand began in p1 
                new_child_DNA.insert(p1_DNA_start_index_deepCopy, DNA_holder[k])
                # Increment your index iterator and counter variable
                p1_DNA_start_index_deepCopy += 1
                k += 1
            
            # Now that the child has received the DNA it will take from p1, 
            # we need to fill in the remaining DNA elements with genes
            # from the DNA structure of p2.
            # Begin by initializing a variable that will point to the index that 
            # falls directly after the last index filled with p1 DNA
            x = p1_DNA_start_index + p1_strand_length
            
            # Iterate as long as we're in between the end of the p1 strand and the 500th gene 
            while (x < self.Agent_quiver[selected_parents[i]].DNA_length):
                # keep loading indices from p2 into the corresponding indices in the child DNA array
                new_child_DNA.insert(x, self.Agent_quiver[selected_parents[j]].DNA[x])
                x += 1

            # Now wrap back around to the beginning of the child DNA list filling in any indices 
            # that are open and lie before the p1 DNA strand begins
            y = 0
            while(y < p1_DNA_start_index):
                # Keep loading indices from p2 into the corresponding indices in the child DNA array
                new_child_DNA.insert(y, self.Agent_quiver[selected_parents[j]].DNA[y])
                y += 1

            # We now have a list of DNA genes that is an ordered mixture of 2 parents
            # Now we create a new child infusing them with the DNA resulting from the
            # crossover reproduction process
            new_child = Agent.Agent(self.city, self.agent_DNA_length, new_child_DNA)

            
            # The last part of the reproductive process is to introduce mutation
            # We want to only introduce mutation a small percentage of the time.
            # Also, we want the percentage of time that a child's genes get mutated 
            # to be highest in the beginning generations and decrease with successive generations.
            
            # We begin by capturing a random float between 0 and 1 which will be our probability
            rand = random.random()
              
            # If the randomly generated float is less than the mutation_rate
            if rand < self.mutation_rate:
                # Mutate this child
                new_child.mutate()

            # Now that we've successfully crossed DNA from 2 parent agents to produce 
            # a child whose DNA is a combination of both of its parents, as well as
            # implemented DNA mutation based on a predetermined probability, now we 
            # need to add the child from this iteration to our new population
            new_pop.append(new_child)

            # We need to increment our j variable an extra digit so that it jumps 2 indices every loop
            j += 2

        # Let's increment the generation counter before we return from this method
        self.global_gen_counter += 1
        # decrement mutation rate by 1 percent each round until we reach .05
        if (self.mutation_rate > .05):
            self.mutation_rate -= .005

        # return a new generation of agents
        return new_pop

#################################################################################
# This code below is adapted from Smitha Dinesh Semwal to be used in selection() 
# https://www.geeksforgeeks.org/find-closest-number-array/
##################################################################################
# This code uses binary search to locate the index of the closet element in a list to a target value
# Modification made to code to return the single index value that the target lies in
# Returns the index corresponding to the selected parent based on the random value passed into target 
# Parameters: arr: array holding boundary locations from 0 to 1. 
#             n = length of arr
#             target: random float(0,1) used to randomly select parent        
def findClosest(arr, n, target): 
  
    # Corner cases 
    if (target <= arr[0]): 
        return 0 
    if (target >= arr[n - 1]): 
        return (n - 2)
  
    # Doing binary search 
    i = 0; j = n; mid = 0
    while (i < j):  
        mid = (i + j) // 2
  
        if (arr[mid] == target): 
            return mid
  
        # If target is less than array  
        # element, then search in left 
        if (target < arr[mid]) : 
  
            # If target is greater than previous 
            # to mid, return closest of two 
            if (mid > 0 and target > arr[mid - 1]): 
                return (mid-1)
  
            # Repeat for left half  
            j = mid 
          
        # If target is greater than mid 
        else : 
            if (mid < n - 1 and target < arr[mid + 1]): 
                return mid
                  
            # update i 
            i = mid + 1
          
    # Only single element left after search 
    return mid 