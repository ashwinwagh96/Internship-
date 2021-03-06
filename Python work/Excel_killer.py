"""
Created on Tue Jun 13 2017

@author: awagh
"""
"""
THIS CODE IS USED FOR CALCULATING i) THE TOTAL LOAD CONNECTED PER LEVEL
                                  ii) TRANSFORMER SPECIFICATIONS
                                  iii) TCL and NMD
                                  iv) TRANSFORMER SIZING
INPUTS REQUIRED :  i)   APARTMENT CONFIGURATION EXCEL SHEET
                   ii)  LOAD DETAILS PER APARTMENT TYPE (written in a dictionary 'load_dict')
                   iii) TRANSFORMER SECONDARY VOLTAGE
                   iv)  DIVERSITY
"""

""" PROBLEMS
1) LEVELS WITH LABELS OTHER THAN LXX ALSO GET COUNTED AS LXX. CAN BE RECTIFIED 
"""
""" FUTURE SCOPE
1) The code can be improvised by using tables instead of dictionaries, as they are easier to access
2) GUI can be built to make the data easily accessible and atlerable
3) The data can be directly input to the script instead of getting from excel sheet.
"""

 
from collections import defaultdict
from trans_sizing import transformer_sizing
from get_data import get_Data
  
dictionary = get_Data('TestFile#1.xlsx')
normal_diversity = 0.3    
diversity = 0.6
# load per apt. type in kW
load_dict = {'1 BHK' : 18.6, '2 BHK' : 20.1, '3 BHK' : 26.4, '4 BHK' : 30.1, '5 BHK' : 35.3,'6 BHK' : 43.6}

transformer_sec_volt = 415
phase_neutral_voltage = round(transformer_sec_volt / 1.732,0)
print " \nTRANSFORMER SPECIFICATIONS \n" 
print "Voltage: " + "%s/%s" %(transformer_sec_volt,phase_neutral_voltage)
transformer_rating = input('Rating of the transformer : ')                      #Rating of the transformer

""" -------------------- START POSITION OF APARTMENET DATA ----------------------- """ 

rows = len(dictionary)
columns = len(dictionary['0'])
start_pos = 0
for i1 in range(rows):
    if ('BHK' in str(dictionary['0']['{0}'.format(i1)])):
        start_pos = i1
        break

""" --------------------------- CURRENT RATING PER APT TYPE ----------------------- """

current_rating = defaultdict(dict)
for i in range(len(load_dict)):
    current_rating['{0}'.format(dictionary['0']['{0}'.format(i+start_pos)])] = round(load_dict['{0}'.format(dictionary['0']['{0}'.format(i+start_pos)])]*1000 /(415*1.732),2)
print "\nCURRENT RATING PER APT TYPE" 
print "{0}\n".format(current_rating) 

""" ------------- LOAD & DIVERSIFIED LOAD PER APT + TOTAL FLATS PER APT TYPE -------------------""" 

load_per_apt_dict = defaultdict(dict)
div_load_apt_dict = defaultdict(dict)

total_flats_per_apt_type = []

for j2 in range(start_pos,columns):
    temp_flats_count = 0
    for i2 in range(1,rows):
       temp_var = dictionary['0']['{0}'.format(j2)]
       load_per_apt_dict[format(i2-1)][format(j2-start_pos)] = (dictionary['{0}'.format(i2)]['{0}'.format(j2)])*(load_dict['{0}'.format(temp_var)])  
       div_load_apt_dict[format(i2-1)][format(j2-start_pos)] = round((load_per_apt_dict[format(i2-1)][format(j2-start_pos)] * diversity*1000 /(transformer_sec_volt*1.732)),2)
       temp_flats_count += dictionary['{0}'.format(i2)]['{0}'.format(j2)]
    total_flats_per_apt_type.append(temp_flats_count)

#print total_flats_per_apt_type
#print load_per_apt_dict
#print div_load_apt_dict

""" -------------------------- TOTAL LOAD PER LEVEL --------------------- """
level_total = []
for l in range(len(div_load_apt_dict)):
    temp = 0
    for k in range(len(div_load_apt_dict['0'])):
        temp += div_load_apt_dict['{0}'.format(l)]['{0}'.format(k)]
    level_total.append(temp)
#print level_total   
 
""" -------------------------- TCL AND NMD (in kW) ----------------------- """
tcl = []
nmd = []
for pos in range(len(total_flats_per_apt_type)):
    temp_load1 = total_flats_per_apt_type[pos]*load_dict['{0}'.format(dictionary['0']['{0}'.format(pos+start_pos)])] 
    temp_load2 = temp_load1 * normal_diversity
    tcl.append(round(temp_load1,2))    
    nmd.append(round(temp_load2,2))       

print "tcl: {0}".format(tcl) 
print "nmd: {0}".format(nmd)


""" ------------------- TRANSFORMER SIZING ------------------------------  """
print "\nTRANSFORMER SIZING"
trans_store = transformer_sizing(level_total,transformer_rating)        #Calling the function          
        