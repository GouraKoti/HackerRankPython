#Kevin and Stuart want to play the ‘The Minion Game’.

#Game Rules
#Both players are given the same string, S.
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.

#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.
#Your task is to determine the winner of the game and their score.

#Input Format :
#A single line of input containing the string S.
#Note: The string S will contain only uppercase letters:[A - Z] .

#Constraints :
#0 < len(s) <= 10^6

#Output Format :
#Print one line: the name of the winner and their score separated by a space.
#If the game is a draw, print Draw.

#Code
def minion_game(string):
    Kevin = 0
    Stuart = 0
    length = len(string)
    
    for i,c in enumerate(string):
        if c in 'AEIOU':
            Kevin+=length-i
        else:
            Stuart+=length-i
    
    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Kevin < Stuart : 
        print('Stuart', Stuart)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
