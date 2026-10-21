def are_anagrams(word1, word2):
    if word1 == word2:
        return False
    else:
        x = list(word1)
        y = list(word2)
        x.sort()
        y.sort()
        if x == y:
            return True
        else:
            return False
        
if are_anagrams("poodle", "poodle"):
    print("Yes")
else:
    print("No")