# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name,score]
        records.append(student)
        
    Low = min(records, key= lambda x : x[1] )[1]
    filtered = [x for x in records if x[1] != Low]
    
    secLow = min(filtered, key= lambda x : x[1] )[1]         
        
    names = [x[0] for x in records if x[1] == secLow]
    names.sort()
    for x in names:
        print(x)
