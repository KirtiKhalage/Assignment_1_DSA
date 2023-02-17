#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

# In[26]:


def find(array,key): 
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == key:
                print(array[i],",",array[j],end ="\n")
    return ""    
array = [2,5,4,3,6,4]
key = 8
print("Pairs of an integer array whose sum is equal to", key, "are:")
print(linear_search(array,key))


# 
# # Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

# In[16]:


def reverse_array(array, starting, ending):
    while starting < ending:
        array[starting], array[ending] = array[ending], array[starting]
        starting +=1
        ending -=1
    
array = [1,2,3,4,5,6,7,8]
print(array)
starting = 0
ending = 7
reverse_array(array,starting,ending)
print(array)


# # Q3. Write a program to check if two strings are a rotation of each other?

# In[35]:


def check_rotation(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    if size1 != size2:
        return "Not valid"
    temp = string1 + string1
    if (temp.count(string2)> 0):
        return "Strings are rotation of each other"
    else:
        return "Strings are not rotations of each other"
string1 = "KIRTI"
string2 = "TIKIR"
 
check_rotation(string1, string2)


# # Q4. Write a program to print the first non-repeated character from a string?

# In[6]:


def non_repeated(string):
    while string != "":
        length = len(string)#8
        x = string[0]#t
        string = string.replace(x, "")
        length_1 = len(string)
        if length_1 == length-1:
            print ("First non-repeated character from string is" ,x)
            break
non_repeated("kkirttii")
        


# # Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

# In[10]:


def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print ("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
# main
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')


# # Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

# In[12]:


def isOperator(x):
    if x == "+":
        return True 
    if x == "-":
        return True
    if x == "/":
        return True
    if x == "*":
        return True
    return False
def postToPre(post_exp):
    s = []
    length = len(post_exp)    
    for i in range(length):
        if (isOperator(post_exp[i])):
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
            temp = post_exp[i] + op2 + op1
            s.append(temp)
        else:
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans
post_exp = "AB+CD-*"
print("Postfix to Prefix ") 
postToPre(post_exp)


# # Q7. Write a program to convert prefix expression to infix expression.

# In[16]:


def prefixToInfix(prefix):
    stack = []
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i -= 1
        else:
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
    return stack.pop()
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
str = "*-A/BC-/AKL"
print(prefixToInfix(str))


# # Q8. Write a program to check if all the brackets are closed in a given code snippet.

# In[20]:


def brackets_closed(express):
    stack = []
    for char in express:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
    if stack:
        return False
    return True
express = "{(}[]"
if brackets_closed(express):
    print("Closed")
else:
    print("Not Closed")


# # Q9. Write a program to reverse a stack.

# In[42]:


class Stack_structure:
    def __init__(self):
        self.items = []

    def check_empty(self):
        return self.items == []

    def push_val(self, data):
        self.items.append(data)

    def pop_val(self):
        return self.items.pop()

    def print_it(self):
        for data in reversed(self.items):
            print(data)

def insert_bottom(instance, data):
    if instance.check_empty():
        instance.push_val(data)
    else:
        deleted_elem = instance.pop_val()
        insert_bottom(instance, data)
        instance.push_val(deleted_elem)

def stack_reverse(instance):
    if not instance.check_empty():
        deleted_elem = instance.pop_val()
        stack_reverse(instance)
        insert_bottom(instance, deleted_elem)

my_instance = Stack_structure()
data_list = input('Enter the elements to add to the stack: ').split()
for data in data_list:
    my_instance.push_val(int(data))

print('The reversed stack is:')
my_instance.print_it()
stack_reverse(my_instance)
print('The stack is:')
my_instance.print_it()


# # Q10. Write a program to find the smallest number using a stack.

# In[40]:


class smallest_in_stack(object):
    small=float('inf')
    def __init__(self):
        self.small=float('inf')
        self.stack = []
    def push(self, x):
        if x<=self.small:
            self.stack.append(self.small)
            self.small = x
        self.stack.append(x)
    def pop(self):
        z = self.stack[-1]
        self.stack.pop()
        if self.small == z:
            self.small = self.stack[-1]
            self.stack.pop()
    def top(self):
        return self.stack[-1]
    def get_small(self):
        return self.small
s = smallest_in_stack()
s.push(-8)
s.push(4)
s.push(-9)
print(s.get_small())
s.pop()
print(s.top())
print(s.get_small())

