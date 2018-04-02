#find and replace
# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find('day')

# print "It's thanksgiving day. It's my birthday,too!".replace('day', 'month')

#*****************print min and max********************
# x = [2,54,-2,7,12,98]
# print min(x)
# print max(x)

#**********first and last********************
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0], x[-1]

#*******************new list*****************

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()

b = x[:len(x)/2]
c = x[len(x)/2:]
newarr = []
newarr.append(b)

print newarr + c