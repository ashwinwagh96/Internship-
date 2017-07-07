"""
Created on Wed Jun 14 2017

@author: awagh
"""
"""
This function extracts the essential data from the excel sheet Apartment Configuration.
This data is used in the Excel_killer file for further calculations. 
"""

""" PROBLEMS 
1) Mainly requires same excel sheet template
"""
""" IMPROVEMENT SCOPE
1) Make the code more friendly..... Reduce its dependency on the template format
2) Detect the sheet on which apt config is written automatically 
""" 


def get_Data(filename):
    sheet_index = 3                     #specify the sheet index containing apt. config data ..... troublesome
    import xlrd
    #book = xlrd.open_workbook('TestFile#2.xlsx')
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(sheet_index)                         
    
    # CREATING DICTIONARY FROM EXCEL DATA
    from collections import defaultdict
    dictionary = defaultdict(dict)
    for i in range(sh.nrows):            #form dictionary from excel values
        for j in range(sh.ncols):
            if type(sh.cell_value(rowx = i,colx = j)) != float:
                dictionary[format(i)][format(j)] = (sh.cell_value(rowx = i,colx = j)).encode('ascii','ignore')
            else:
                dictionary[format(i)][format(j)] = (sh.cell_value(rowx = i,colx = j))
    
    
    """--------------------------CREATING USABLE DATA SET---------------------------"""
    
    final_dict = defaultdict(dict)
    final_dict = dictionary
    
    # 1) CHECKING LOCATION OF THE REQUIRED DATA IN DICTIONARY 
    start_posR = 0
    start_posC = 0
    for i in range(sh.nrows) :
        if (start_posR != 0) or (start_posC != 0) :
            break
        for j in range(sh.ncols):
                if 'BHK' in str(final_dict['%s'%(i)]['%s'%(j)]):    # finds the row and column of word containing
                    start_posR = i                                  # 'BHK' and stores in variables
                    start_posC = j
                    break
    
    # 2) REMOVING USELESS DATA 
    for i in range(start_posR):                 # removing the initial rows . pop removes the rows and
            final_dict.pop('{0}'.format(i))     # also shifts the dictionary by one. So keys change. 
    
    for i in range(start_posR,sh.nrows):                # removing the blank rows
        if (final_dict['%s'%(i)]['%s'%(0)]) == '' :
            final_dict.pop('{0}'.format(i))
    
    # 3) SORTING THE DATA
    final_dict1 = defaultdict(dict)
    
    keys = final_dict.keys()            # accessing the dictionary keys
    temp_keys = []                      # and sorting the dictionary using sorted keys
    for key in keys:
        temp_keys.append('0'+key)
    temp_keys = map(int,temp_keys)
    key1 = sorted(temp_keys)   
    temp_key = 0
    for key in sorted(key1):    
        final_dict1['{0}'.format(temp_key)] = final_dict['{0}'.format(key)] 
        temp_key += 1
    
    # 4) WRITING REQUIRED TITLES ..... problematic !!!
    for i  in range(len(final_dict1['0'])) :                 # here the titles are altered so as to make next    
        if 'BHK' in final_dict1['0']['{0}'.format(i)] :      # steps easier
            final_dict1['0']['{0}'.format(i)] = (final_dict1['0']['{0}'.format(i)])[:5]
            
    for i in range(1,len(final_dict1)):
        for j in range(start_posC,len(final_dict1['0'])):
            if (type(final_dict1['%s'%(i)]['%s'%(j)]) == str):
                final_dict1['%s'%(i)]['%s'%(j)] = 0
    
    # ADDITIONAL MODIFICATIONS
    for i in range(len(final_dict1['0'])):
            if final_dict1['0']['%s'%(i)] == '' :   # removes the unnecessary columns
                for j in range(len(final_dict1)):
                    final_dict1['%s'%j].pop('%s'%(i))
    
    return final_dict1


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                   