def capitalize (name):
    result = ''                                             # An empty string to append all capitalized words
    nameList = name.split ()                                # The name take in to a list
    for i in nameList :
        if i == nameList [0]:                               # 1st name without initial spaces
            result = i.capitalize ()        
        
        else:
            result = result + " " + i.capitalize ()         # rest names with initial spaces

    return result
    

name = input ()
print (capitalize (name))


# Instead of capitalize (), title () can be used.
# Difference is ,
#   5a.capitalize () -> 5a      (Capitalize only 0th indexed character (if it is a lowercase letter))
#   5a.title () -> 5A           (Capitalize letter that is met 1st from the begining)