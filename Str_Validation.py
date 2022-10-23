#You are given a string .
#Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

if __name__ == '__main__':
    s = input()
    
    for c in s:
       k = c.isalnum()
       if (k==True):
           break
        
    print(k)
    
    for c in s:
       k = c.isalpha()
       if (k==True):
           break
        
    print(k)
    
    for c in s:
       k = c.isdigit()
       if (k==True):
           break
        
    print(k)
    
    for c in s:
       k = c.islower()
       if (k==True):
           break
        
    print(k)
    
    for c in s:
       k = c.isupper()
       if (k==True):
           break
        
    print(k)
