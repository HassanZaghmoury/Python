# # define a function that says hello to the name provided
# # this starts a new block


# def say_hello(name):
#   #these lines are indented therefore part of the function
#   if name:
#    print 'Hello, ' + name + ' from inside the function'
#   else:
#    print 'No name'
# # now we're unindented and have ended the previous block
# say_hello('hassan')
# print 'Outside of the function'

# #*************************strings***********************************************

# print "this is a sample string"

# name = "Zen"
# print "My name is", name

# name = "Zen"
# print "My name is " + name
# #*****************************concatenating ****************************
# first_name = "Zen"
# last_name = "Coder"
# print "My name is {} {}".format(first_name, last_name)


# #*****************************string*****************************

# print "this is a sample string"

# name = "string sample 2"
# print "My name is", name

# name = "string sample 3"
# print "My name is " + name

# first_name = "string sample 4"
# last_name = "Coder"
# print "My name is {} {}".format(first_name, last_name)

# hw = "hello %s" % 'world'
# print hw
# # the output would be:
# # hello world

# #*****************************lists***********************************

# ninjas = ['Rozen', 'KB', 'Oliver']
# my_list = ['4', ['list', 'in', 'a', 'list'], 987]
# empty_list = []
# print(ninjas, my_list)
# print(ninjas)
# print my_list # you dont need to put ()

# #****************sample list**********************************

# fruits = ['skittles', 'sneakers', 'mango','apples']
# vegys = ['burgers', 'fires','carrot cake']
# fruits_and_vegys = fruits + vegys
# print(fruits_and_vegys)
# salad = 3 * vegys
# print salad

# #****************Accessing Values**************************

# drawer = ['documents', 'envelopes', 'pens']
# #access the drawer with index of 0 and print value
# print drawer[0]  #prints documents
# #access the drawer with index of 1 and print value
# print drawer[1] #prints envelopes
# #access the drawer with index of 2 and print value
# print drawer[2] #prints pens

#*****************Manipulating Lists**********************

# x = [1,2,3,4,5]
# x.append(99)
# print x
# #the output would be [1,2,3,4,5,99]


# x = [99,4,2,5,-3]
# print x[:]
# #the output would be [99,4,2,5,-3]
# print x[1:]
# #the output would be [4,2,5,-3];
# print x[:4]
# #the output would be [99,4,2,5]
# print x[2:4]
# #the output would be [2,5];

#**********************List Built-in Functions****************

# my_list = [1, 'Zen', 'hi']
# print len(my_list)
# # output
# for index, value in enumerate(my_list):
#     print"{} {} {}".format(value, value, value)
#***************************List Built-in Methods*************

my_list = [1,5,2,8,4]
my_list.append(7)
print my_list
my_list.extend(my_list)
print my_list

my_list.pop()
print my_list

print my_list.index(8)
# output:
# [1,5,2,8,4,7]


