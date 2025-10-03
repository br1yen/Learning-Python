def seperate(text):
    """makes a new line after each period"""
    return text.replace(".", ".\n")

def avgLst():
    """calculate the average of a list"""
    nums = eval(input("Enter a list of number in the format [1, 2, 3, ...]:\n"))
    if len(nums) == 0:
        return 0.0
    else:
         return sum(nums) / len(nums)

def evens(n):
    """finds all the even numbers in a range that is positive"""
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        for i in range(2,n+1):
            if i % 2 == 0:
                print(i)
        

    
    
