"""
Created on Wed Jun 14 2017

@author: awagh
"""
""" PROBLEMS 
1) Mainly requires same excel sheet template
"""
""" IMPROVEMENT SCOPE
 
""" 


def get_Data(filename):
    import xlrd
    #book = xlrd.open_workbook('TestFile#2.xlsx')
    book = xlrd.open_workbook(filename)
    sh = book.sheet_by_index(3)                         #keep the apartment config sheet on index'3' .... troublesome
    # CREATING DICTIONARY FROM EXCEL DATA
    from collections import defaultdict
    dictionary = defaultdict(dict)
    for i in range(sh.nrows):                           #form dictionary from excel values
        for j in range(sh.ncols):
            if type(sh.cell_value(rowx = i,colx = j)) != float:
                dictionary[format(i)][format(j)] = (sh.cell_value(rowx = i,colx = j)).encode('ascii','ignore')
            else:
                dictionary[format(i)][format(j)] = (sh.cell_value(rowx = i,colx = j))
    
    
    """--------------------------CREATING USABLE DATA SET---------------------------"""
    
    final_dict = defaultdict(dict)
    final_dict = dictionary
    
    # 1) CHECKING WHERE IS THE REQUIRED DATA 
    start_posR = 0
    start_posC = 0
    for i in range(sh.nrows) :
        if (start_posR != 0) or (start_posC != 0) :
            break
        for j in range(sh.ncols):
                if 'BHK' in str(final_dict['%s'%(i)]['%s'%(j)]):
                    start_posR = i
                    start_posC = j
                    break
    
    # 2) REMOVING USELESS DATA 
    for i in range(start_posR):
            final_dict.pop('{0}'.format(i))
    
    for i in range(start_posR,sh.nrows):
        if (final_dict['%s'%(i)]['%s'%(0)]) == '' :
            final_dict.pop('{0}'.format(i))
    
    # 3) ARRANGING THE DATA
    final_dict1 = defaultdict(dict)
    
    keys = final_dict.keys()
    temp_keys = []
    for key in keys:
        temp_keys.append('0'+key)
    temp_keys = map(int,temp_keys)
    key1 = sorted(temp_keys)   
    temp_key = 0
    for key in sorted(key1):    
        final_dict1['{0}'.format(temp_key)] = final_dict['{0}'.format(key)] 
        temp_key += 1
    
    
    # 4) GETTING NEEDED TITLES
    for i  in range(len(final_dict1['0'])) :
        if 'BHK' in final_dict1['0']['{0}'.format(i)] :
            final_dict1['0']['{0}'.format(i)] = (final_dict1['0']['{0}'.format(i)])[:5]
            
    for i in range(1,len(final_dict1)):
        for j in range(start_posC,len(final_dict1['0'])):
            if (type(final_dict1['%s'%(i)]['%s'%(j)]) == str):
                final_dict1['%s'%(i)]['%s'%(j)] = 0
    
    # ADDITIONAL MODIFICATIONS
    for i in range(len(final_dict1['0'])):
            if final_dict1['0']['%s'%(i)] == '' :
                for j in range(len(final_dict1)):
                    final_dict1['%s'%j].pop('%s'%(i))
    return final_dict1


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                   