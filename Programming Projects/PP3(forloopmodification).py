def word_count(string):
    """returns the count for every, unique length of words in a string"""
    for i in string:
        if i in [",", ".", ":", ";", "!", "?", "-", "\'", "\""]:
            string = string.replace(i, "")
    words = string.split()
    lengths = []
    for word in words:
        lengths.append(len(word))
    print(lengths)
    lengths_index = []
    for length in range(min(lengths),max(lengths)+1):
        if length in lengths:
            lengths_index.append([length, lengths.count(length)])

    print(lengths_index)
 
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

        
 
    
    
