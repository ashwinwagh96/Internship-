"""
Created on Wed Jun 14 2017

@author: awagh
"""
# THIS FILE CONTAINS A FUNCTION transformer_sizing which is used for designing the transformer system for an apartment.
# Inputs required : i) Transformer rating
#                   ii) Total load connected per level   

"""PROBLEMS
"""


from collections import defaultdict 
transformer_dict = defaultdict(dict)

def transformer_sizing(level_total,transformer_rating):
    transformer_count = 0
    init_count = 0
    i = 0
 
    while init_count < len(level_total):
        if level_total[i] > transformer_rating :                # Check if transformer can support the supply 
                print "Please choose higher rating transformer -- " + "Level {}".format(i) + " load: " + "{}  ".format(level_total[i]) + "Transformer rating : {0}".format(transformer_rating)
                break
            
        temp_total = 0
        
        for i in range(init_count,len(level_total)):
            if level_total[i] > transformer_rating :
                break
            
            temp_total += level_total[i]
            
            if temp_total >= transformer_rating :
                print ("Transformer {0}".format(transformer_count)+ " for Levels L{0}".format(init_count) + " to L{0}".format(i-1))
                transformer_dict['0{0}'.format(transformer_count)]['transformer'] = 'TX0{0}'.format(transformer_count)
                transformer_dict['0{0}'.format(transformer_count)]['start'] = 'L0{0}'.format(init_count)
                transformer_dict['0{0}'.format(transformer_count)]['end'] = 'L0{0}'.format(i-1)
                transformer_dict['0{0}'.format(transformer_count)]['total_load'] = '{}'.format(temp_total - level_total[i])
                transformer_count += 1
                init_count = i
                break
            
            elif (i == len(level_total)-1):
                print ("Transformer {0}".format(transformer_count)+ " for Levels L{0}".format(init_count) + " to L{0}".format(i))
                transformer_dict['0{0}'.format(transformer_count)]['transformer'] = 'TX0{0}'.format(transformer_count)
                transformer_dict['0{0}'.format(transformer_count)]['start'] = 'L0{0}'.format(init_count)
                transformer_dict['0{0}'.format(transformer_count)]['end'] = 'L0{0}'.format(i)
                transformer_dict['0{0}'.format(transformer_count)]['total_load'] = '{}'.format(temp_total)
                init_count = len(level_total)
                break
            
    return transformer_dict