#Consider a list (list = []). You can perform the following commands:
#
#insert i e: Insert integer  at position .
#print: Print the list.
#remove e: Delete the first occurrence of integer .
#append e: Insert integer  at the end of the list.
#sort: Sort the list.
#pop: Pop the last element from the list.
#reverse: Reverse the list.

#Code
if __name__ == '__main__':
    N = int(input())
    arr = []
    
    for i in range(N) : 
        line = input();
        item = []
        item = line.split()
        if 'insert' in item:
            arr.insert(int(item[1]),int(item[2]))
        elif 'print' in item:
            print(arr)
        elif 'remove' in item:
            arr.remove(int(item[1]))
        elif 'append' in item:
            arr.append(int(item[1]))
        elif 'sort' in item:
            arr.sort()
        elif 'pop' in item:
            arr.pop()
        elif 'reverse' in item:
            arr.reverse()
