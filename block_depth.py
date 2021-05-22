
# Jason Richardson
# 4/27/2021




num_of_brack = 0        # keeps track of nested brackets

inside_paranth = 0      # keeps track of when symbols are inside parantheses

inside_single_line_comment = 0      # check for single line comment

inside_multi_line_comment = 0   # checks for being inside a multi line comment

possible_multi_line = 0     # variable gets incremented until it reaches 2 indicating inside a multi line comment

end_multi_line = 0          #  keeps track of when a multi line comment ends


file = open("input.txt", "r")	# open input file for reading

expressions = file.readlines()		# read each line into a list

file.close()				# close the file

for p in expressions:       # loop through each line as a string 
    
    inside_paranth = 0      # initialize inside parantheses flag
    
    inside_single_line_comment = 0      # initialize inside single line comment flag
    
    for p2 in p:            # loop through each character for processing
        
        if(p2 == '"'):          # inside parantheses
            
            if(p2 == '"' and inside_paranth == 1):  # exiting parantheses
                
                inside_paranth = 0
                
            else:           # inside parantheses
                
                inside_paranth = 1
        
        if(p2 == '/'):      # possible start of comment
            
            inside_single_line_comment = inside_single_line_comment + 1         # if / then start counting to find second / indicating a single line comment
            
            possible_multi_line = 1     # indicate possible multi line comment
            
            if(inside_single_line_comment == 2):    # if inside single line comment then everything after comment symbols on current line don't need processing
                
                break
            
            if( end_multi_line == 1 ):      # indicate end of multi line comment
                
                inside_multi_line_comment = 0
                
        if( p2 == "*"):         # possible second symbol in start of multi line comment or possible first symbol in end of multi line comment
            
            if( possible_multi_line == 1 ):     # indicate start of multi line comment
                
                inside_multi_line_comment = 1
        
            if( possible_multi_line == 2):      # indicate end of multi line comment 
                
                end_multi_line = 1              # let the earlier if loop know the / symbol following the * is the end of the multi line comment
                
            possible_multi_line = 2             # set to 2 for detecting the second * in */ indicating end of the multi line comment
            
            
            
        if(p2 == "{" and inside_paranth != 1 and inside_multi_line_comment != 1):   # check for paranthes and comments and if not inside one then increment bracket count
            
            num_of_brack = num_of_brack + 1
            

        if(p2 == "}" and inside_paranth != 1 and inside_multi_line_comment != 1):   # check for parantheses and comments and if not inside one then decrement bracket count
            
            num_of_brack = num_of_brack - 1
            
    print(num_of_brack,p)       # print line with bracket count
   

if( num_of_brack != 0 ):        # check for unclosed brackets
    
    print("Error: expected '}' but found EOF")
    
    
 
				