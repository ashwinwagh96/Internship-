"""
Created on Wed Jun 14 2017

@author: awagh
"""

# THIS CONTAINS CODE FOR CALCULATING THE BUSBAR LENGTH REQUIRED FOR AN APARTMENT DESIGN
# INITIALLY ASSUMING NO FIRE CHECK AND SERVICE AREAS

""" 
PARAMETERS REQUIRED :
    1) Length of each floor
    2) Additional lengths like : Podium Height
    3) No. of transformers used and the levels they supply power to -> Dictionary containing transformer no. ; Start Level ; End Level
"""
import Excel_killer
 
horizontal = input("Lenght of Horizontal run : ")
h_level = input("Height of each level: ")                       #Height of each level
h_podium = input("Height of the podium: ")                      #Podium Height
len_apt = input("Length of apartment: ")
#cd = input("Enter approx cable diameter for vertical shaft planning: ")

busbar_cost_per_mtr = input("Cost price per mtr for busbar : ")
cable_cost_per_mtr = input("Cost price per mtr for cable : ")

#Additional lengths to account for
additional = []
while (1):
    temp = input("Extra Length: ")
    if (str(temp)).lower() == 'done' :
        break
    #elif type(temp) != int or type(temp) != float :
    #    print "Incorrect input"
    else :    
        additional.append(temp)
total_additional = 0
for i in range(len(additional)):
    total_additional += additional[i]

"""
# Dictionary for testing the code
dictionary = {'00' : {'transformer' :'TX00', 'start':'L00', 'end' : 'L05' },
              '01' : {'transformer' :'TX01', 'start':'L06', 'end' : 'L11' },
              '02' : {'transformer' :'TX02', 'start':'L12', 'end' : 'L15' },
              '03' : {'transformer' :'TX03', 'start':'L16', 'end' : 'L18' } }
"""
flag = raw_input("Rough Estimate(type 'y') or Exact Solution(type 'n') : ")
if flag == 'n' : 
    dict1 = Excel_killer.trans_store
    dict2 = Excel_killer.dictionary
    
    from collections import defaultdict
    
    print "\n--------------FOR BUSBAR SYSTEM------------------\n  "
    busbar_length_per_transformer = defaultdict(dict)
    for i in range(len(dict1)):
        busbar_length_per_transformer['TX0{0}'.format(i)] = round((total_additional + horizontal + h_podium + (float((dict1['0{0}'.format(i)]['end'])[1:])+1)*h_level),2) 
    
    #print "\nBUSBAR LENGTH PER TRANSFORMER \n" + '{0}'.format(busbar_length_per_transformer)     
    
    total_busbar_length = 0
    for i in range(len(busbar_length_per_transformer)):
        total_busbar_length += busbar_length_per_transformer['TX0{0}'.format(i)] 
    print "TOTAL BUSBAR LENGTH : " + '{0}'.format(total_busbar_length) + ' m'
     
    total_cable_length1 = 0
    # total_cable_length += float(apt_total[])*len_apt
    for i in range(1,len(Excel_killer.dictionary)):
        if type(Excel_killer.dictionary['{0}'.format(i)]['2']) != str :
            total_cable_length1 += (Excel_killer.dictionary['{0}'.format(i)]['2'])*len_apt        
    print "TOTAL CABLE LENGTH : " + '{0}'.format(total_cable_length1) + 'm'
    
    print "COST FOR BUSBAR SYSTEM: " + "{0}".format((busbar_cost_per_mtr*total_busbar_length) + (cable_cost_per_mtr*total_cable_length1))
    #shaftW = (2 * len(total_cable_length2) + 1) * 200
    #print("Consier a shaft 1200mm deep by " + str(int(shaftW)) + " mm wide to house this busbar")
    
    
    print "\n-----------FOR CABLE SYSTEM------------\n"
    total_cable_length2 = []
    for i in range(1,len(Excel_killer.dictionary)):
        if type(Excel_killer.dictionary['{0}'.format(i)]['2']) != str :
            total_cable_length2.append((i*h_level + h_podium + horizontal + total_additional + (Excel_killer.dictionary['{0}'.format(i)]['2']))*len_apt )
    cable_total_length2 = sum(total_cable_length2)
    print "TOTAL CABLE LENGTH: " + "{0}".format(cable_total_length2)
    print "COST FOR CABLE SYSTEM: " + "{0}".format((cable_total_length2)*(cable_cost_per_mtr))
    
    #print("Considering 1D spacing shaft wall area at worst point approx: ")     # Problem !!!!!
    #wa = cd * ((2* ((len(total_cable_length2)-1) * 6)) + 1)
    #wac = ((len(total_cable_length2)-1) * 6)
    #print("This shaft needs to accomodate " + str(int(wac)) + " No. cables equating to a wall area of " + str(int(wa)) + " mm")

#if flag == 'y':
    