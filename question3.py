'''
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''

num = int(input("Enter number: "))
d = dict()

''' 
    Why here num+1 because if user enter number 4
    then it start from 1 to 4. 
    If you write only num and you enter number 4
    then it start with 1 to 3.
'''
for i in range(1,num+1):
    d[i] = i*i
print(d)