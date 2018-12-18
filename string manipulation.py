country="United States of India"
#Get the first 5 letters by using substring
a=country[:5]
print("first 5 letters are:%s"%(a))
#Get 'States' from the above string by using substring
b=country[7:13]
print("the substring is:%s"%(b))
#Get letter count without a space in the above sentence
c=len(country)
print("the total letters in string is :%d"%(c))
#Get the 'India' by using substring
d=country[-5:]
print("the substring is:%s"%(d))
# Print the country to upper
f=country.upper()
print("String in upper case is:%s"%(f))
# Print the country to lower
f=country.lower()
print("String in upper case is:%s"%(f))
#reverse the country
x="India"
print (''.join(reversed(x)))
#to swap the case
g=country.swapcase()
print("the swaped case is %s"%(g))
#to find the pacing
h=' ' in country == True
print("%s !the variable has space"%(h))













