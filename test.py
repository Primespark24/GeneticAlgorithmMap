import googlemaps 
from datetime import datetime
from googlemaps import Client
gmaps = Client(key='AIzaSyCFcf_BmN1Qm1q-a3yy07RXtPHMgOiyZ-w')

################### CLASSES AND FUNCTIONS ###################

def PathGenerator(Sequence, Addresses, Location = [1,1,2]):
    #UNSURE HOW TO HANDLE LOCATION
    Path = []
    for Direction in Sequence:
        if(Direction == 'L'):
            Path.append(Addresses[0])
    return Path

# A class for representing intersections
# Constructor: takes 4 Boolean arguments (North, South, East, West). True
#              if that direction is available to the bot, false otherwise
# _repr_ : Printing the details of the intersection
class intersection:
    def __init__(self, North, South, East, West):
        self.North = North
        self.South = South
        self.East = East
        self.West = West

    def __repr__(self):
        return "North:% s South:% s East:% s West:% s" % (self.North, self.South, self.East, self.West)


################### MAIN CODE ###################

################### LIST OF EAST STREETS ###################
# All North/South streets east of Division street
NorthE =['N Stuart St', 'N Ruby St', 'N Mayfair St', 'N Colton St' 'N Lidgerwood St', 'N Astor St' 'N Addison St', 'N Wiscomb St' 'N Standard St', 'N Dakota St' 'N Cincinnati St', 'N Hamilton St', 'N Nevada St', 'N Columbus St', 'N Morton St', 'N Denver St', 'N Perry St', 'N Hogan St', 'N Helena St', 'N Madelia St', 'N Pittsburg St', 'N Magnolia St', 'N Napa St', 'N Martin St', 'N Crestline St', 'N Lee St', 'N Stone St', 'N Altamont St', 'N Cook St', 'N Smith St', 'N Lacey St', 'N Nelson St', 'N Regal St', 'N Haven St', 'N Market St']
# All East/West streets east of Division street
EastN = ['E Francist', 'E Decatur Ave', 'E Dalke Ave','E Bismark Ave', 'E Central Ave', 'E Columbia Ave', 'E Joseph Ave', 'E Nebraska Ave', 'E Rowan Ave', 'E North Ave', 'E North-Sanson Alley', 'E Sanson Ave', 'E Everett Ave','E Diamond Ave', 'E Crown Ave', 'E Queen Ave', 'E Olympic Ave', 'E Wabash Ave', 'E Broad Ave', 'E Wellesley Ave', 'E Hoffman Ave', 'E Princeton Ave', 'E Heroy Ave', 'E Longfellow Ave', 'E Rich Ave', 'E Rockwell Ave', 'E Lacrosse Ave', 'E Ostrander Ave', 'E Walton Ave', 'E Garland Ave', 'E Empire Ave', 'E Providence Ave', 'E Kiernan Ave', 'E Gordan Ave', 'E Glass Ave', 'E Garnet Ave', 'E Courtland Ave', 'E Bridgeport Ave', 'Liberty Ave', 'E Dalton Ave', 'E Euclid Ave', 'E Fairview Ave', 'E Cora Ave', 'E Cleveland Ave', 'E North Foothills Dr', 'E Grace Ave', 'E Buckeye Ave', 'E Marietta Ave', 'E Avon Pl', 'E Jackson Ave', 'E Charlisle Ave', 'E Montgomery Ave', 'E Illinois Ave', 'E Ermina Ave', 'E Baldwin Ave', 'E Indiana Ave']

######################################
# 0 - street does not exist in current location
# 2 - Starting or stoping point of road
# 1 - Connection exists
###################################### 
East = ['E Francis Ave'
['E Francis Ave', ['0','']],
['E Dalke Ave', ['1',]],
['E Bismark Ave', ['X']],
['E Bismark Ave', ['0']],
['E Bismark Ave', ['0']],
['E Bismark Ave', ['X']],
['E Central Ave', ['1']]]

# All North/South streets west of Division street
NorthW = ['N Monroe St', 'N Lincoln St', 'N Post St', 'N Wall St', 'N Howard St', 'N Stevens St', 'N Washington St', 'N Whitehouse St', 'N Calispel St', 'N Normandie St', 'N Atlantic St', 'N Atlantic Dr', 'N Division St' ]
# All East/West streets west of Division street
West = []

################## INTERSECTION INFO FOR WESTSIDE STREETS #####################
West = [
    #need to change all lines to follow the one below :(
    ['W Francis Ave', [intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(2,2),intersection(0,0),intersection(2,2)]], 
    ['W Dalke Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Central Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']], 
    ['W Columbia Ave', ['2','1','1','1','2','1','1','1','1','1','1','0','2']], 
    ['W Franklin Ct', ['0','0','0','0','0','0','0','0','2','0','2','0','0']],
    ['W Joesph Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Nebraska Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Rowan Ave', ['2','1','1','1','1','1','1','2','0','0','0','0','0']],
    ['W Everett Ave', ['2','1','1','1','1','1','1','2','0','0','0','0','0']],
    ['W Queen Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Wabash Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Wellesley Ave', ['2','1','1','1','1','1','1','1','1','1','0','1','2']],
    ['W Amherst Ct', ['0','0','0','0','0','0','0','0','1','0','0','1','0']],
    ['W Sussex Ct', ['0','0','0','0','0','0','0','0','0','0','0','1','0']],
    ['W Princeton Ave', ['2','1','1','1','1','1','1','2','0','0','0','0','0']],
    ['W Heroy Ave', ['2','1','1','1','1','1','1','1','0','0','0','2','0']],
    ['W Longfellow Ave', ['2','1','1','1','1','1','1','1','1','1','0','1','2']],
    ['W Rockwell Ave', ['2','1','1','1','1','1','1','1','1','1','0','1','2']],
    ['W Lacrosse Ave', ['2','1','1','1','1','1','1','1','1','1','0','1','2']],
    ['W Walton Ave', ['2','1','1','1','1','1','1','1','1','2','0','0','0']],
    ['W Garland Ave', ['2','1','1','1','1','1','1','1','1','1','1','0','2']],
    ['W Providence Ave', ['2','0','1','1','1','0','1','0','1','1','1','0','2']],
    ['W Kiernan Ave', ['2','0','1','0','1','0','2','0','0','0','0','0','0']],
    ['W Gordon Ave', ['2','0','1','0','1','0','1','0','1','1','1','0','2']],
    ['W Glass-Gordon Alley', ['2','0','0','0','0','0','0','0','0','0','0','0','0']],
    ['W Glass Ave', ['2','0','1','0','1','0','1','0','1','1','1','0','2']],
    ['W Courtland Ave', ['0','0','0','0','0','0','0','0','0','1','1','0','2']],
    ['W Gray Ct',  ['0','0','0','0','0','0','0','0','0','1','1','0','2']],
    ['W Cora Ave',  ['2','1','1','0','1','1','1','0','1','1','1','0','2']],
    ['W Alice Ave',  ['2','1','1','0','1','1','1','0','0','0','0','0','2']],
    ['W Dalton Ave',  ['2','1','1','1','1','1','1','0','1','1','0','0','2']],
    ['W Euclid Ave',  ['2','1','1','1','1','1','1','0','1','1','1','0','2']],
    ['W Frederick Ave',  ['2','1','1','1','1','1','1','0','1','1','2','0','0']],
    ['W Park Pl',  ['0','0','2','1','0','1','0','0','1','1','2','0','0']],
    ['W Fairview Ave', ['2','1','2','0','0','0','0','0','0','0','0','0','0']],
    ['W Waverly Pl', ['0','0','2','1','1','0','1','0','0','1','1','0','2']],
    ['W Cleveland Ave', ['2','1','1','1','1','0','1','1','1','1','2','0','0']],
    ['W Grace Ave', 
    ['W Buckeye Ave', 
    ['W Chelan Ave', 
    ['W York Ave', 
    ['W Jackson Ave', 
    ['W Carlisle Ave', 
    ['W Montgomery Ave', 
    ['W Mansfield Ave', 
    ['W Knox Ave', 
    ['W Shannon Ave', 
    ['W Indiana Ave'

LRAddresses = []*4

"""
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
for i in range(200):
     gmaps.directions('6220 North Division, Spokane, WA', '5313 East Frederick, Spokane, WA')
    
#gmaps.distance_matrix('6220 North Division, Spokane, WA','5313 East Frederick, Spokane, WA')
print("done")

directions = directions[0]
i=1
for leg in directions['legs']:
    startAddress = leg['start_address']
    print("Start Address:", startAddress)
    endAddress = leg['end_address']
    distance = leg['distance']['text']
    print("End Address:", endAddress)
    print("Distance:", distance)
    for step in leg['steps']:
        html_instructions = step['html_instructions']
        html_instructions = html_instructions.split('<b>')
        html_instructions2 = ''
        for each in html_instructions:
            if(each != '<b>'):
                html_instructions2 += each
        html_instructions2 = html_instructions2.split('</b>')
        html_instructions3 = ''
        for each in html_instructions2:
            if(each != '<b\>'):
                html_instructions3 += each
        print("STEP {} {}".format(i ,html_instructions3))
        i = i+1
"""