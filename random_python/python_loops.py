# for count in range (0, 6):
#     print "looping -", count

    #**********looping through a list****************
    #create a new list
    #remember list can have many data-types and even more lists

# my_list = [4, 'dog', 99, ['list', 'inside', 'another'], 'hello world']

# for element in my_list:
#     print element

#*********while loops*********************************
# count = 0
# while count <= 5:
#     print "looping -", count
#     count += 1

#***********loop control**************

# for val in "string":
#     if val == 'i':
#         break
#     print val

#**********continue********
# for val in 'string':
#     if val == 'i':
#         continue
#     print val

#*****else***************

# x = 8
# y = x
# while y > 0:
#     print y
#     y = y - 1
# else:
#   print "Final else statement"

x = 3
y = x
while y > 0:
    print y
    y = y - 1
    if y == 0:
        break
else:
    print "Final else statement"
