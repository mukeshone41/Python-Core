first_name = 'Mridul'
last_name = 'Patel'
country = "India"
city = "Sultanpur"
age = 21
is_married = True
skill = ['HTML','CSS','React','Python']
Personal_informaiton= {
    "first_name" : 'mridul ',
    'last name' : 'Patel',
    'country' : 'india',
    "city" : "Sultanpur"
}
# printing the value stored in variable
print('first name =',first_name)
print('last_name =',last_name)
print('first name length',len(first_name))
print('last name length',len(last_name))
print('city' ,city)
print("age",age)
print('skill',skill)

# declare multiple variable in single line
first_name, last_name,age,country,skill = 'vipul','patel',21,'india','[python,java]'
print(first_name,last_name,age,skill)

# memory representation
x,y = 10,10
print(x)
z=y
print(id(x))
print(id(y))
print(id(z))
print(type(x))
print(type(10))
x = 5
print(x)