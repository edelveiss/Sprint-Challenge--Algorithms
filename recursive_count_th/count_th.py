'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
#RunTime complexity: O(n)
#Space complexity: O(n)
def count_th(word):
    #base case
    if len(word) == 0:
       return 0
    if word[:2] == 'th':
        #if there is 'th' in the word the counter is increased by one and move toward the base case
        return count_th(word[1:]) + 1
    #move toward the base case
    return count_th(word[1:])

print("th: ", count_th("thhthokTHhhth")) # 3 th
    
