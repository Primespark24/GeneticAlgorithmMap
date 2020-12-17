# Brycen Martin, Jonathan Laughlin and Shane Snediker
# Dr. Jones CS473
# Genetic Algorithm Final Project
# Updated December 14, 2020


import Agent        # import user defined agent class to represent City navigating bots
import City         # import user defined City class to represent the problem space
import Reproduction # import user defined Reproduction Class
import pygame       # import pygame library to display graphics
import copy         # import the copy library used for making deep copies of variables
import os           # Allows us to control where the city window pops up on the screen

# Define our city colors
BLACK = (0, 0, 0)          # Background color
RED = (255, 0, 0)          # City street colors
WHITE = (255, 255, 255)    # Agent test color
BLUE = (50, 50, 255)       # Agent test color
TEAL = (0, 128, 128)       # Stat counters
GRAY = (169, 169, 169)     # Streets 

# I'd like to control the positioning of the screen - like where it pops up on the computer screen
x_win_loc = 100     # Represents the x coordinate of the upper left corner of the pop up window
y_win_loc = 50      # Represents the y coordinate of the upper left corner of the pop up window
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (x_win_loc, y_win_loc)  # Tell the window where to pop up 

# global variables that control the time clock and the drawable screen
clock = None
screen = None


# Function that initializes pygame object which allows us to draw a city to the screen
# Parameter:  city: a city object containing the graphical city data
def pygame_setup(city):
    # Initialize the pygame library that facilitates the graphical representation of the city
    pygame.init()
    # create a screen to draw the city on utilizing the pygame library
    global screen
    screen = pygame.display.set_mode([City.City.CITY_SIZE[0], City.City.CITY_SIZE[1] + 200])
    # Set title of screen
    pygame.display.set_caption("Advanced Algorithms Final Project Fall 2020")
    # Declaration of a clock variable that utilizes a clock function
    # from the pygame library that mediates the speed of the screen updates
    global clock
    clock = pygame.time.Clock()
    # Set the screen background
    screen.fill(BLACK)

# Function that paints our graphical city to the screen
# Parameter:  city: a city object containing the graphical data
def draw_city(city):
    NS = True
    N = True
    EW = False
    S = False
    rowInc = 1
    row = 0
    for rowGraph in range(117):
        square = 0
        #print(row)
        col = 0
        if(NS):
            index = 1        
            if N:
                intersectionIndex = 0
            elif S:
                intersectionIndex = 1 
            else:
                intersectionIndex = float('inf') # Catch error if N and S are both False  
        while square < 36:
            color = BLACK

            #print the roads that go north to south
            if(NS):
                if square == index:
                    #print(row, intersectionIndex, city.CITY_GRID[col][row][intersectionIndex])
                    if(city.CITY_GRID[row][col][intersectionIndex] == True):
                        color = GRAY
                    else:
                        color= BLACK
                    pygame.draw.rect(screen,
                        color,
                        # x coordinate is the product of the cell width and the current column 
                        [city.CELL_SIZE * rowGraph,#square,   
                        # y coordinate is the product of the cell height and the current row     
                        city.CELL_SIZE * square,#rowGraph,     
                        # rectangle width
                        city.CELL_SIZE,             
                        # rectangle height
                        city.CELL_SIZE])
                    index+=3
                    col+=1

            #Print the roads that go east to west
            elif(EW):
                if(city.CITY_GRID[row][col][3] == True):
                    color = GRAY
                else:
                    color = BLACK
                #print(square)
                pygame.draw.rect(screen,
                    color,
                    # x coordinate is the product of the cell width and the current column 
                    [city.CELL_SIZE * rowGraph,#square,   
                    # y coordinate is the product of the cell height and the current row     
                    city.CELL_SIZE * square,#rowGraph,     
                    # rectangle width
                    city.CELL_SIZE,             
                    # rectangle height
                    city.CELL_SIZE])
                square+=1
                #print(square)
                if(city.CITY_GRID[row][col][4] == True):
                    color = GRAY
                elif(True in city.CITY_GRID[row][col]):
                    color = GRAY
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                    color,
                    # x coordinate is the product of the cell width and the current column 
                    [city.CELL_SIZE * rowGraph,#square,   
                    # y coordinate is the product of the cell height and the current row     
                    city.CELL_SIZE * square,#rowGraph,     
                    # rectangle width
                    city.CELL_SIZE,             
                    # rectangle height
                    city.CELL_SIZE])
                square+=1
                #print(square)
                if(city.CITY_GRID[row][col][2] == True):
                    color = GRAY
                else:
                    color = BLACK
                pygame.draw.rect(screen,
                    color,
                    # x coordinate is the product of the cell width and the current column 
                    [city.CELL_SIZE * rowGraph,#square,   
                    # y coordinate is the product of the cell height and the current row     
                    city.CELL_SIZE * square,#rowGraph,     
                    # rectangle width
                    city.CELL_SIZE,             
                    # rectangle height
                    city.CELL_SIZE])
                #print(square)
                col+=1
            square +=1
            #print(square)
        if(N):
            NS = False
            N = False
            EW = True
        elif(EW):
            EW = False
            S = True
            NS = True
        else:
            S = False
            N = True 
        # Update the screen with what has been drawn
        pygame.display.update()
        rowInc+=1
        if(rowInc == 4):
            row+=1
            rowInc = 1

"""
def draw_city(city): 
    # Draw the city one time before entering the game loop
    # For every one of the 41 rows in the grid
    for row in range(39):
        # And every one of the 70 columns as well              
        for column in range(12):
            # Let's make the background black
            color = BLACK
            # Now we iterate through our 2 dimensional array and print street locations in red  

            for value in range(5):
                color = BLACK
                if city.CITY_GRID[row][column][value] == True:
                    color = BLUE

                # The pygame draw.rect function takes 3 primary arguments:
                # The first argument is the surface on which the rectangle will be drawn
                # The second is the desired color of the rectangle
                # The third is a tuple with the following values in this order:
                # x coordinate, y coordinate, width of rectangle, Height of rectangle, and the thickness of the rectangle lines
                # If no argument is given for the thickness parameter (like in our case), then the default is to fill the rectangle with the color argument
                pygame.draw.rect(screen,
                                color,
                                # x coordinate is the product of the cell width and the current column 
                                [city.CELL_SIZE * column*value,   
                                # y coordinate is the product of the cell height and the current row     
                                city.CELL_SIZE * row*value,     
                                # rectangle width
                                city.CELL_SIZE,             
                                # rectangle height
                                city.CELL_SIZE])
    # Update the screen with what has been drawn
    pygame.display.update()        
"""
# Function to move every agent in a population one time
# Parameter:  pop: a population object representing the population of agents traversing the city
#             a_divisor: divides amount of agents displayed by this number      (cuts down complexity for larger samples)
#             dna_divisor: divides the amount of actions displayed by this number (cuts down complexity for larger samples)
def move_population_once(pop,a_divisor = 1, dna_divisor = 1):
    # Boolean flag that gets set if an agent was able to move and changed positions
    Moved = False
    # Declare a couple of global variables to track the agent's traversal through their DNA sequence 
    global actionNumber, done_moving
    # Check if agents still have moves to execute
    if (actionNumber < pop.agent_DNA_length):
        # move every agent once
        for x in range(pop.pop_size):
            # Capture each agent in the population's movement status
            Moved = pop.Agent_quiver[x].move(actionNumber, pop.city)
            #print(actionNumber)
            # If an agent changes positions, update the screen
            if (Moved == True) and (actionNumber % dna_divisor == 0) and ((x == (pop.pop_size -1)) or (x % a_divisor == 0)):
                # change the previous position to black
                color = GRAY
                # Peek line 60 for draw.rect() argument explanation
                pygame.draw.rect(screen, color, [pop.city.CELL_SIZE * pop.Agent_quiver[x].previous_position_map[0], pop.city.CELL_SIZE * pop.Agent_quiver[x].previous_position_map[1], pop.city.CELL_SIZE, pop.city.CELL_SIZE])
                # update the new position to Red
                color = RED
                pygame.draw.rect(screen, color, [pop.city.CELL_SIZE * pop.Agent_quiver[x].current_position_map[0], pop.city.CELL_SIZE * pop.Agent_quiver[x].current_position_map[1], pop.city.CELL_SIZE, pop.city.CELL_SIZE])
                # Update the screen with what has been drawn
                pygame.display.update()
        # increment which DNA gene is firing (which action the agent is taking)
        actionNumber += 1
    # Now the agent has exhausted their sequence of gene instructions
    else:
        done_moving = True

# Function that resets the city erasing the previous generation of agents and placing the new generation at the beginning location
# Parameter:  pop: a reproduction object representing a new generation of agents traversing the city
def clear_screen(pop):
    # Draw over all agents with black, clean the board
    for x in range(pop.pop_size):
        # change the previous position to black
        color = GRAY
        pygame.draw.rect(screen, color, [pop.city.CELL_SIZE * pop.Agent_quiver[x].current_position_map[0], pop.city.CELL_SIZE * pop.Agent_quiver[x].current_position_map[1], pop.city.CELL_SIZE, pop.city.CELL_SIZE])
    # update what we've drawn
    pygame.display.update()
 

# Allows text objects to be generated using a string and a font
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

 # Button function adapted from: https://pythonprogramming.net/pygame-button-function-events/
 # creates a clickable button that executes a passed in function
 # Params: msg: button text, x:x, y:y, w:width, h:height, ic:inactive color, ac:active color, action: on click function
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # mouse is on top of button, change color
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            # display text on button and return color to inactive
            pygame.draw.rect(screen, ic,(x,y,w,h))
            smallText = pygame.font.SysFont("comicsansms",20)
            textSurf, textRect = text_objects(msg, smallText)
            textRect.center = ( (x+(w//2)), (y+(h//2)) )
            screen.blit(textSurf, textRect)
            # perform passed in function
            action()
                     
    else:
        #draw button with inactive color
        pygame.draw.rect(screen, ic,(x,y,w,h))

    # display text on button
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w//2)), (y+(h//2)) )
    screen.blit(textSurf, textRect)

# The first function called before main game loop is started
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Start",545,420,80,50,WHITE,BLUE,game_loop)
        pygame.display.update()

######### Highlight all the agents that are selected to get eaten ###########
# A fun, miscellaneous function that highlights on the screen the agents with the lowest fitness at the end of a generation
# Parameter:  pop: a Reproduction object representing a generation of agents traversing the city
def highlight_weak(pop):
    # Declare a variable that will capture the weakest agents from a generation of an agent population
    weakest = pop.kill_the_weak()
    # Let's paint them red to the screen
    color = RED
    for x in range(len(weakest)):
        pygame.draw.rect(screen, color, [city_instance.CELL_SIZE * weakest[x].current_position[0], city_instance.CELL_SIZE * weakest[x].current_position[1], city_instance.CELL_SIZE, city_instance.CELL_SIZE])
    # Update the screen with what has been drawn
    pygame.display.update()
    pygame.time.delay(3000)

######## Highlight all the selected parents #######
# Another miscellaneous function that highlights the fittest agents among a generation by painting them blue
# Parameter:  pop: a population object representing a population of agents traversing the city
def highlight_parents(pop):
    # Capture selected parents
    selected = copy.deepcopy(pop.selection())
    # Paint them blue to the screen
    color = WHITE
    for x in range(len(selected)):
        pygame.draw.rect(screen, color, [city_instance.CELL_SIZE * pop.Agent_quiver[selected[x]].current_position[0], city_instance.CELL_SIZE * pop.Agent_quiver[selected[x]].current_position[1], city_instance.CELL_SIZE, city_instance.CELL_SIZE])
    # Update the screen with what has been drawn
    pygame.display.update()
    pygame.time.delay(3000)

#------------------ Main object declarations and implementation begin here -------------------------------

########################################################
# Basic Genetic Algorithm Pseudo Code:
# 1: Seed first generation
# 2: do while(TerminationCondition != True):
# 3:    reproduction.move()
# 4:    reproduction.calculate_fitness()
# 5:    reproduction.select_parents()
# 6:    reproduction.crossover&mutate()
# 7:    reproduction.kill_the_weak()
# 8:    reproduction.reset()
#########################################################

# ----------------- Start of Main Program Loop ----------------------------------------------------
# Instantiate a city
city_instance = City.City()
# Seed the first population to navigate the city giving it (pop_size, city object, DNA_length declaration)
test_reproduction = Reproduction.Reproduction(30, city_instance, 300)
# setup pygame display
pygame_setup(test_reproduction.city)
# display the city to the pygame window
draw_city(test_reproduction.city)

done_moving = False     # The flag that allows the city to loop until the user clicks the close button
actionNumber = 0        # This is the DNA index for the agent to execute each loop
FPS = 1000              # defines game loop frames per second; lower numbers can be used to more closely observe agent movement
exited = False          # Flag holding the screen open

# main game loop where evolution of reproductions take place
def game_loop():
    
    global done_moving, actionNumber, FPS, exited

    # Begin a loop that runs for as many generations as you use as an argument for the range function
    for generation in range(100):
        # While the user hasn't clicked the exit button and the generation is still navigating through their DNA sequences
        while ((not exited) and (not done_moving)):
            # Define how many frames per second the simulation runs at
            clock.tick(FPS) # should be called once per frame
            # Checks if exit is clicked on
            for event in pygame.event.get():  
                # First, if the user clicks the close button, we need to close the window down
                if event.type == pygame.QUIT:
                    # by changing the loop flag to True
                    exited = True

            #####################
            # Population movement
            #####################
            
            # move the entire population one step forward
            move_population_once(test_reproduction,1,1)
            
        # Only continue with program, if window has not been exited
        if not exited:
            # RESET variables so next generation can be spawned into the city
            done_moving = False
            actionNumber = 0
            # Clear the screen
            clear_screen(test_reproduction)
            
            ######################
            ## Calculate Fitess
            ######################
            test_reproduction.calculate_fitness()
            test_reproduction.get_fitness_stats(screen)      
            # highlight_parents(test_population)
            #####################################################################
            ## Select Parents and Produce children through crossover and mutation
            #####################################################################
            children = test_reproduction.crossover()
            
            ##########################
            ## Kill the weakest agents
            ##########################
            # highlight_weak(test_population)
            test_reproduction.kill_the_weak()

            #############################
            ## Reset for next generation
            #############################
            
            test_reproduction.add_children(children)
            # move all agents back to the start of the city
            test_reproduction.reset(screen)
            
            print("Current generation: " + str(test_reproduction.global_gen_counter))
            print("Avg fitness: " + str(test_reproduction.average_fitness) + "Top Fitness: " + str(test_reproduction.top_score))
        
    # --------  End of Main Program Loop -----------

    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    pygame.quit()
    quit()

# Start the program
game_intro()