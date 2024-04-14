# def display():
#     print("first")
#     print("second")
#     print("Third")
# display()    
# def show():
#     n1=100
#     print(n1)
#     ch="A"
#     print("A")
#     n1=500
#     print(n1)

# show()    
# var1=500
# def display():
#     var1=300
#     globel= var2
#     var2=600

#     print("value of var1" ,var1)
# display()    


# def display1():
#     print("value of var1 is : ",var1)
#     print("vale of var2 is ", var2)
# display1()    
# def disp():
#     print("inside disp")
# def myfun():
#     print("inside main")
#     disp()

# myfun()        
# def disp(var):
#     print("inside disp\t" ,var)
# def myfun():
#     print("inside main")
#     print(20)
#     disp()

# myfun()        
# var =500
# def myfun():
#     var=100
#     print("local variable\t", var)
# myfun()    
# def disp(var1=10,var2=20):
#     print(var1,"\t",var2)

# def fun():
#     disp()
#     disp(10)
#     disp(100,200)
# fun()    
# non default argument follows default argument
# def disp(var2=90,var1):
#     print(var1,"\t",var2)

# def fun():
#     disp(90)
   
# fun()    
# def disp(*vargs):
#     print(type(vargs))
#     if(vargs.__len__()==0):
#         print("no argument passed")
#     else:
#         for k in vargs:
#             print(k)
# def fun():
#     disp()
#     disp(10,20,30)
#     disp("abc",200,True,4,7)
# fun()
# def myfun(**varg):
#     print(type(varg))
#     for key,value in varg.items():
#         print(key, value)
# # myfun('A',"hellow",5,6,True,500) 

# myfun(name="Rohit",age=30)       

# myfun(name="virat kohli",age=35, roll_number=1,address="delhi") 
# def sqaure(num):
#     ''' This function accepts a number the square of the number'''
#     return num*num
# print(sqaure(10))    
# print(sqaure.__doc__)

# print(print.__doc__)
# print(help.__doc__)
# def msg(num):


#     print(num)
#     print(type(num))
#     return num*num


# msg()    
# def Add(n1, n2):
#     return n1 + n2
# print(Add(60,50))

# name= input("Enter your name")
# age =int(input("Enter your age "))
# print("Your name is: ",name)
# print("Your name is :  {name}")
# print("Your name is {}".format(name))
# name = input("Enter your name")
# age=int(input("Enter your age "))
# message = "{}'s  age is {}"
# print(message.format(name,age)) 



