# CS473 Genetic Algorithm Final Project
Welcome to our Whitworth Advanced Algorithms and Analysis Final Project!  We created a genetic algorithm.  Genetic algorithms are loosely based on the principles of natural selection and evolution.  They have a unique ability to search problem spaces to calculate optimal solutions much faster than humans.  The problem space that we chose to define is the navigation of a small portion of the city streets in Spokane.  Our vision for this algorithm is to optimize the travel routes for a delivery service.  We set the genetic algorithm free upon the defined map of Spokane and allow it to calculate an optimized travel route given a set of input locations.

Authors: Brycen Martin, Jonathan Laughlin and Shane Snediker
Updated: December 15, 2020

## Goals
We intentionally defined a wide range of goals for this algorithm so as to help keep us focused.  We didn't want to settle for an elementary product, however, having rudimentary goals also helps us capture encouragement throughout the program design as the pieces begin to come together.  The following list comprises our set of goals, from simple to complex:
* We've never connected a project to an API.  We want to sufficiently connect our map of Spokane to Google's API and use their geographical information
* We will code a genetic algorithm (GA) bot, including all traditional elements of a GA (encoding, selection, crossover, mutation, ect.).
* We will define an acceptable level of fitness for the GA so that it doesn't exert unnecessary, excessive time optimizing routes
* Our GA bot will arrive at an initial location successfully
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
                          
                           |                                Astor Ave
                        
                        Astor Ave                               |_____Rowan Ave_____                            
                        
                           |                                                        |
                        
                           |___Rowan Ave_______                                     |
                        
                                                                                Astor Ave
                        
                                                                                    |
                        
                                                                                    |

## Algorithm Analysis

### Key Genetic Algorithm Components
* Encoding
We initialize a seed population with an initial DNA consisting of completely random navigational directives. We hold the "genes" in a 1 dimensional array. Once the population size is predetermined a seed population of agents is initialized each given an initial random DNA sequence of instructions ('L', 'R', or 'F').
* Selection
A generation of agents expires when each agent has completed its full array of genetic instructions. We use a roulette style selection process based on probabilities. Every agent of a given population has a statistical chance to enter the reproductive process, with agents with higher fitness scores having a higher probability of getting selected. We order the agents by fitness score and delegate each agent a float value between 0 and 1 in ascending order with larger float values correlating to higher fitness scores. We then randomly generate float values between 0 and 1 which correlate to the agents that we are going to select for reproduction. This selection strategy favors higher fitness scores, but also doesn't completely eliminate lower fitness scores, which allows for more genetic variety being perpetuated throughout successive generations. We select half of the population to enter the crossover process.
* Crossover
At this point the population enters the reproductive process. Because an agent's fitness score is tied to the order of its movements, we desire to preserve this order in successive generations. Therefore, we use a method of crossover reproduction called ordered crossover. According to this strategy, we pull a random length strand of DNA from parent 1 from a random array starting index, we place this strand in the new_child DNA structure at the exact same starting index. We then fill in the remaining DNA indices with the corresponding genes from parent 2. The resulting child DNA array is an ordered mix of parent 1 and parent 2.
* Mutation
Mutation is critical for persistent genetic variety which helps your algorithm avoid local maxima. Within the crossover process, we subject every new child to the possibility of mutation according to a random number generator that is tied to probabilities. For the first 10 generations of agents, every new baby bot has a 15% chance of getting mutated. For generations 11-20 every new baby bot has a 10% chance of getting mutated. And every generation thereafter the baby bots have a 5% chance of mutation. Our method of mutation is to pull a strand of DNA that is 10% of the total DNA sequence from a random location within the sequence and randomly generate completely new DNA instructions.

## Files

## Works Cited 