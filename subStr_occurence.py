#In this challenge, the user enters a string and a substring. 
#You have to print the number of times that the substring occurs in the given string. 
#String traversal will take place from left to right, not from right to left.

#Code
def count_substring(string, sub_string):
    count = 0
    ln = len(string)
    i = 0
    while i < ln:
        val = string.find(sub_string,i)
        if val != -1:
            count+=1
            i = val + 1
        else:
            i+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
