# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(str1, str2):
    # [assignment] Add your code here
    if (sorted(str1) == sorted(str2)):

       return True

    else:
        return False

str1 = "angel"
str2 = "angle"

print(find_anagram(str1, str2)) 

