# CS473 Genetic Algorithm Final Project
Welcome to our Whitworth Advanced Algorithms and Analysis Final Project!  We created a genetic algorithm.  Genetic algorithms are loosely based on the principles of natural selection and evolution.  They have a unique ability to search problem spaces to calculate optimal solutions much faster than humans.  The problem space that we chose to define is the navigation of a small portion of the city streets in Spokane.  Our vision for this algorithm is to optimize the travel routes for a delivery service.  We set the genetic algorithm free upon the defined map of Spokane and allow it to calculate an optimized travel route given a set of input locations.

To Run the program, open Main.py and run without debugging.  

Authors: Brycen Martin, Jonathan Laughlin and Shane Snediker

Updated: December 17, 2020

## Goals
We intentionally defined a wide range of goals for this algorithm so as to help keep us focused.  We didn't want to settle for an elementary product, however, having rudimentary goals also helps us capture encouragement throughout the program design as the pieces begin to come together.  The following list comprises our set of goals, from simple to complex:
* We will code a genetic algorithm (GA) bot, including all traditional elements of a GA (encoding, selection, crossover, mutation, ect.).
* We will define an acceptable level of fitness for the GA so that it doesn't exert unnecessary, excessive time optimizing routes
* Our GA bot will arrive at an initial location successfully
* We've never connected a project to an API.  We want to sufficiently connect our map of Spokane to Google's API and use their geographical information
* Given a fixed set of inputs, our GA bot will optimize a route to the delivery locations
* Given a set of inputs that changes in real time, our GA bot will be able to alter its optimization calculations to determine an evolving optimization of delivery routes.
* We will create a graphical representation of our bots traversing the problem space

## Assumptions
In order to realistically simulate a delivery service within the scope of this project, it was necessary to significantly scale down the problem space.  This required some core assumptions.  The following is a list of the assumptions that were central to understanding the efficacy of our GA bots:
* If the bot is traveling on a road, it is allowed to make a U-turn.  It can reverse directions without worrying about traffic laws.  
* The shortest distance between 2 locations is defined simply as Google's satellite distance between the two locations; traffic, road construction and other variables are neglected.
* If a road is disconnected by a small distance, we treat that situation as though the road stays connected.  The following pictorial example helps visualize this siutation:
  
        ___Rowan Ave_______                                     |
                           |                                    |
                           |                                    |
                           |                                    |
                           |                                Astor Ave
                           |                                    |
                        Astor Ave                               |_____Rowan Ave_____                            
                           |
                           |                                                        |
                           |                                                        |
                           |___Rowan Ave_______                                     |
                                                                                    |
                                                                                Astor Ave
                                                                                    |
                                                                                    |
                                                                                    |
                                                                                    |

## Algorithm Analysis

### Key Genetic Algorithm Components

* Encoding
  
We initialize a seed population with an initial DNA consisting of completely random navigational directives. We hold the "genes" in a 1 dimensional array. Once the population size is predetermined a seed population of agents is initialized each given an initial random DNA sequence of instructions ('N', 'S', 'E', or 'W').

* Selection

A generation of agents expires when each agent has completed its full array of genetic instructions. We use a roulette style selection process based on probabilities. Every agent of a given population has a statistical chance to enter the reproductive process, with agents with higher fitness scores having a higher probability of getting selected. We order the agents by fitness score and delegate each agent a float value between 0 and 1 in ascending order with larger float values correlating to higher fitness scores. We then randomly generate float values between 0 and 1 which correlate to the agents that we are going to select for reproduction. This selection strategy favors higher fitness scores, but also doesn't completely eliminate lower fitness scores, which allows for more genetic variety being perpetuated throughout successive generations. We select half of the population to enter the crossover process.  Therefore new generations of robots consist of 50% new babies and 50% of the agents with the highest fitness scores from the previous generation.

* Crossover

At this point the population enters the reproductive process. Because an agent's fitness score is tied to the order of its movements, we want to preserve this order in successive generations. Therefore, we use a method of reproduction called ordered crossover. According to this strategy, we pull a random length strand of DNA from parent 1 from a random array starting index, we place this strand in the new_child DNA structure at the exact same starting index. We then fill in the remaining DNA indices with the corresponding genes from parent 2. The resulting child DNA array is an ordered mix of parent 1 and parent 2.

* Mutation

Mutation is critical for persistent genetic variety which helps your algorithm avoid local maxima. Within the crossover process, we subject every new child to the possibility of mutation according to a random number generator that is tied to probabilities. For the first 10 generations of agents, every new baby bot has a 15% chance of getting mutated. For generations 11-20 every new baby bot has a 10% chance of getting mutated. And every generation thereafter the baby bots have a 5% chance of mutation. Our method of mutation is to pull a strand of DNA that is 10% of the total DNA sequence from a random location within the sequence and randomly generate completely new DNA instructions.

### Worst Case Scenario Algorithm Analysis

A Genetic Algorithm is a very complex piece of code that is almost impossible to find a worst-case analysis to or any analysis for that matter since the number of things that tie to the worst case is so large and every little tweak made to a parameter or the number of bots or a genetic sequence could increase time for the algorithm to run exponentially. For an example we ran a best-case vs worst case time scenario using our current code and if the destination was within a few blocks the route was optimized within 10 minutes but if it was on the other side of our data the time is unknown as I let it run from 7:30 pm December 16 to 1:30 pm December 17 and during that time over 125000 generations had run, and they had not come close to finishing when the program was stopped.







### Updates/If We Had More Time

The program has a lot of assumptions that cause it to be imperfect if you were to use it in the city as streets have been changed to be straight paths instead of curved or diagonal and some single block streets were removed due to the added complexity for the bots to navigate. Other things that need to be changed/improved is our fitness equation/evaluation because if it were improved the bots would converge more efficiently allowing us to use bigger data sets without having to run the code for multiple days to see results
## Files

* Agent.py

This is the file that defines our genetic algorithm robot class.  Integral to the definition of our bots is the constructor function.  Python doesn't allow for overloading constructors, so you have to account for each necessary object instance within one constructor.  The Agent constructor takes 3 arguments: a city object which connects the agent to the problem space, an integer value representing how many genetic instructions the agent will receive and an array of genes.  If the 3rd argument is left out of the constructor function call, this signifies a separate case of Agent creation in which a brand new agent is created and given a random sequence of genetic instructions.  The alternate Agent constructor call is utilized when the mating robots create a child with a specific gene sequence that gets passed into the constructor.

The Agent file contains all of the functions that guide the bot's movements throughout the city array as well as an individualized mutation function.  The mutation function pulls a strand of DNA from the agent that is 10% of it's total DNA sequence, and replaces it with a new, randomized sequence of genes.

Agent.py also contains the genetic algorithm's fitness function.  We used a distance formula function to assign fitness to individual agents.  At the conclusion of every generation of city traversal, we calculate individual bots' distance away from the delivery location by subtracting the array location where the robot ended up upon executing its full sequence of genetic instructions from the array location of the target delivery location.  Robots that end up closer to the delivery location earn a higher fitness score and any robot that makes it at least half way to the target earns a bonus score as well.

* City.py

This file defines our problem space.  Included is hard coded definitions of every intersection in a 6 square mile radius of North Spokane represented as Boolean array values (True if you a robot can traverse in that direction at that intersection, False if it cannot).





* Main.py

The main file that defines program operation.  We utilized the Pygame graphics library to create a graphical representation of our robots traversing the streets of Spokane.  Most of the functions in the main file use the Pygame paradigm to create graphics. However, the main program loop happens in this file as well.  The flow of the main program pseudo code is as follows:

For as many generations as is preset:

 -Instantiate a City object to give robots a design space to explore

 -Instantiate a Reproduction object so that the robots can engage in traditional genetic algorithm operations like selection, crossover and mutation.

 -Create a population of robots to search the problem space.

 -Unleash the robots within the problem space to execute 1 generation of genetic instructions.

 -Calculate fitness.

 -Select reproductive parents

 -Engage parents in crossover reproduction to add children to the next generation of bots.

* Reproduction.py
  
The file containing the core Genetic Algorithm components (Selection, Crossover, Mutation, Fitness).  See above for more details regarding our implementation details for these GA categories.  A personal favorite function of ours was our selection function.  It assigns every agent within the array of agents a float value between 0 and 1.  The agents with the higher fitness scores receive a higher float value.  We then randomly generate a float value between 0 and 1 and use binary search to find the agent whose float value is closest to the randomly generated number and that agent gets chosen to pass its genes on to the next generation.

* map.txt

A text file containing a copy of the streets utilized in the simulation









## Works Cited

1. "Genetic Algorithms - Parent Selection," Tutorialspoint. N.p., n.d. Web 13 December 2020.

2. Fisher, Jeremy. "Genetic Algorithms." YouTube, 11 July 2016, https://youtu.be/7J-DfS52bnl

3. Fullstack Academy. "Genetic Algorithm Tutorial - How to Code a Genetic Algorithm." YouTube, 14 June 2017, https://www.youtube.com/watch?v=XP8R0yzAbdo&list=PL5dxL3XCtx5ao_lt20RfFmO5LidWVpKi3&index=2

4. Craven, Paul Vincent. "Program Arcade Games With Python And Pygame." Program Arcade Games With Python And Pygame. N.p., n.d. Web 13 December 2020.

5. PythonProgramming.net. "Pygame Buttons." Python Programming Tutorials. Web. 17 Dec. 2020, https://www.citationmachine.net/bibliographies/838def73-b912-4c65-9d4f-ba7194bc38d9.

6. SmarakchopdarCheck out This Author's Contributed Articles., Smarakchopdar, and Check out This Author's Contributed Articles. "Find Closest Number in Array." GeeksforGeeks. 21 Jan. 2020. Web. 17 Dec. 2020.
