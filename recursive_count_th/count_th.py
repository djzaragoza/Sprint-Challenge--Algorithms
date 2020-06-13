'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # Objective --
    # recursive function checking the string for 'th' -- account for possible mixed cases
    # TBC
    ## find every 'th' word only if letters 't' and 'h' are next to each other
    
    ## need to figure out a way to count words
    ## need to figure out the account of mixed cases 

    if word[0:2] == 'th':
        count += 1
        return count_th(word[2:len(word)], count)
    elif len(word[1:len(word)]) > 1:
        count = count_th(word[1:len(word)], count)

    return count

    pass
