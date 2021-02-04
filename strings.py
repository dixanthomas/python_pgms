
my_msg='hello world'
print(my_msg)
my_msg='dixan\'s world'
print(my_msg)
my_msg="dixan's world"
print(my_msg)
my_msg="""dixan"s world
its"""
print(my_msg)
my_msg="dixan's world"

print(len(my_msg))  #string length

print(my_msg[6])
print(my_msg[3])
print(my_msg[9])

print(my_msg[3:7]) #substring
print(my_msg[:7]) #from start
print(my_msg[5:]) #to end

print(my_msg.upper())
print(my_msg.lower())

print(my_msg.count('hell'))
print(my_msg.count('d'))

print(my_msg.find('xan'))
print(my_msg.find('nix'))

new_my_msg=my_msg.replace('dixan','nix')
print(new_my_msg)

greet='hello'
name='dixan'
my_msg=greet + ', ' + name
print(my_msg)

my_msg=greet+', ' + name + ' .welcme'
print(my_msg)

my_msg='{}, {}. welcomeee'.format(greet,name)
print(my_msg)

my_msg=f'{greet}, {name}. welcoming' #fstring
print(my_msg)

print(dir(greet)) #list of string attributes and methods

print(help(str)) #str is a class in python

print(help(str.lower))#specific details of lower function