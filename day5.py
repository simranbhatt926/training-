# def disp1():
#     print("Inside")
#     return disp2
# def disp2():
#     print("Inside1")    
# var1=disp1()
# var1()    

# function changing
# def disp1():
#     print("Inside")
#     return disp2
# def disp2():
#     print("Inside1")
#     return disp3    
# def disp3():
#     print("Inside2")        
# disp1()()()
# def outer():
   
#     def inner():
#         print("inside inner function")
#     print("inside outer function")
#     inner()
# outer()
# def outer():
   
#     def inner():
#         print("inside inner function")
#     print("inside outer function")
#     return inner
   
# var1=outer()
# var1()

# def product(a,b):
#     p =a*b
#     print(p)

# product(4,5)
# def product(a,b,c):
#     p=a*b*c
#     print(p)
# product(4,5,6) 
# def disp(*args):
#     print("type of args : ", type(args))

#     print("Hello world" , args.__len__())

# # disp()
# # disp(10)    
# # disp(20,1,3)
# # disp(9,20,70)
# disp(7.5, 9,True)

# 2nd way of  overloading

# import multipledispatch
# ## passing two parameters

# def product(first, second):
#     result= first*second
#     print(result)

# def product(first,second,third):
#     result=first*second*third
#     print(result)

# product(10,20)


# help ()
# print ("hello")
# help(print)
# help(int())
# # help(object)
# number = input("Enter a nuber : ")
# print(number)
# print(type(number))

# help(print)
# print(help(print))
# lambda function

# def my_func(a):
# # function body
#    pass
# def double(x):
#     return x*2
# my_list=[1,2,3,4,5,6]
# new_list=list(map(double, my_list))
# for result in new_list:
#     print(result)
# list1=list(new_list)    
# print(list1) # [2,4,6,8,10]

my_list=[1,2,3,4,5,6]
new_list=list(map(lambda x: x*2, my_list))
print(new_list)

