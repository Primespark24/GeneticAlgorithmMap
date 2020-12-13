import googlemaps 
from datetime import datetime
from googlemaps import Client
gmaps = Client(key='AIzaSyCFcf_BmN1Qm1q-a3yy07RXtPHMgOiyZ-w')

################### FUNCTIONS ###################
def PathGenerator(Sequence, Addresses, Location = [1,1,2]):
    #UNSURE HOW TO HANDLE LOCATION
    Path = []
    for Direction in Sequence:
        if(Direction == 'L'):
            Path.append(Addresses[0])
    return Path


class intersection:
    def __init__(self, North, South, East, West):
        self.North = North
        self.South = South
        self.East = East
        self.West = West

    def __repr__(self):
        return "Left to right intersection:% s Up to down Intersection:% s" % (self.leftRight, self.leftRight)



################### MAIN CODE ###################

################### LIST OF EAST STREETS ###################
NorthE =['N Stuart St', 'N Ruby St', 'N Mayfair St', 'N Colton St' 'N Lidgerwood St', 'N Astor St' 'N Addison St', 'N Wiscomb St' 'N Standard St', 'N Dakota St' 'N Cincinnati St', 'N Hamilton St', 'N Nevada St', 'N Columbus St', 'N Morton St', 'N Denver St', 'N Perry St', 'N Hogan St', 'N Helena St', 'N Madelia St', 'N Pittsburg St', 'N Magnolia St', 'N Napa St', 'N Martin St', 'N Crestline St', 'N Lee St', 'N Stone St', 'N Altamont St', 'N Cook St', 'N Smith St', 'N Lacey St', 'N Nelson St', 'N Regal St', 'N Haven St', 'N Market St']
EastN = ['E Francis', 'E Decatur Ave', ]

################### LIST OF WEST STREETS ###################

NorthWestSide = ['N Monroe St', 'N Lincoln St', 'N Post St', 'N Wall St', 'N Howard St', 'N Stevens St', 'N Washington St', 'N Whitehouse St', 'N Calispel St', 'N Normandie St', 'N Atlantic St', 'N Atlantic Dr', 'N Division St' ]

################## ADDRESSES OF WEST STREETS #####################
West = [
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
    ['W Grace Ave', []],
    ['W Buckeye Ave', []],
    ['W Chelan Ave', []],
    ['W York Ave', []],
    ['W Jackson Ave', []],
    ['W Carlisle Ave', []],
    ['W Montgomery Ave', []],
    ['W Mansfield Ave', []],
    ['W Knox Ave', []],
    ['W Shannon Ave', []],
    ['W Indiana Ave'[]]]

#LRAddresses = []*4


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
