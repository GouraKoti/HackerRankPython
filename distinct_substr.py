#Split s into n/k substring and print distinct chars

def merge_the_tools(string, k):
    # your code goes here
    t = int(len(string)/k)
    j=0
    for i in range(t):
        sub = string[j:j+k]
        print(''.join(set(sub)))
        j = j+k
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
