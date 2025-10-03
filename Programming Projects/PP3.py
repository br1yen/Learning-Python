def word_count(string):
    """returns the count for every, unique length of words in a string"""
    for i in string:
        if i in [",", ".", ":", ";", "!", "?", "-", "\'", "\""]:
            string = string.replace(i, "")
    words = string.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    lengths.sort()
    length_index = []
    i = 0
    while i < (len(lengths)):
        length_index.append([lengths[i],lengths.count(lengths[i])])
        i += lengths.count(lengths[i])
    return length_index
 
user_string = input("Please input a string of words:\n")
output = word_count(user_string)
print(output)
print("Your string contains: ")
if output == []:
    print("nothing")
else:
    for i in range(len(output)):
        if output[i][1] == 1:
            print(f"{output[i][1]} word of length {output[i][0]}")
        else:
            print(f"{output[i][1]} words of length {output[i][0]}")

        
 
    
    
