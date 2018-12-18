colors = ['yellow', 'red', 'blue', 'green', 'black']

#print the first list element
print("the first elementt is :%s"%(colors[0]))

#print the last list element
print("the last  element in list is :%s"%(colors[-1]))

#append the new list element pink
colors.append("pink")
print("append sucessful! the new list is %s"%(colors))

#remove the yellow from the lis
colors.remove("yellow")
print(" yellow removed new list is %s"%(colors))

#pop out the last element
colors.pop()
print("the color is poped")

#return or print the position of red
print("the color red is at:%s"%(colors.index('red')))

#reverse the list element
colors.reverse()
print("the reversed list is %s"%(colors))

#sorted the list elemet
colors.sort()
print("the sorted list is %s"%(colors))
