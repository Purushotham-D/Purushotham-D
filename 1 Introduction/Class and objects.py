#class FirstClass:
#    def __init__(self,name,mob,usn):
#        self.name=name
#        self.mob=mob
#        self.usn=usn
#        
#stud1=FirstClass(name='puruboi',mob=97654454456,usn='1va16ec077')
#print(stud1.mob)
#print(stud1.usn)
#print(stud1.name)

#class StudentDetails:
#    def __init__(self,name,mob):
#        self.name=NONE
#        self.mob=mob
#        Print_Student_Details(self)
#        
#    def Print_Student_Details(self):
#        self.name=input('enter the name')
#        self.mob=input('enter the number')
#        print('mame of the student is {} and mob num is {}'.format(self.name,slef.mob))
#        
#stud1=StudentDetails('abcd',97662897919)
#stud1.name
#stud1
#stud2=StudentDetails()
#stud2.name

class StudentDetails:
    
    
    def __init__(self):
        
        self.name = None
        self.mob = None
        self.print_student_details()
        
    def print_student_details(self):
        self.name = input('enter the name of the student:')
        self.mob = input('enter the mob number of the students:')
        print('name of the student is: {}\
              and mobile number is: {}'.format(self.name,self.mob))
        
stud1=StudentDetails()

dir (list)


'''program 1'''

a,b=1,[2]
d=a/b
print('program completed')


'''program 2'''

a,b=1,[2]

try:
    a/b
except Exception as e :
    print(e)
print('program completed')


'''program 3'''

a,b=1,[2]

try:
    a/b
except Exception as e :
    print(e)
finally:
    print('program will execute fr sure')

print('program completed')


'''program 4'''

a,b=1,[2]

try:
    a/b
except ZeroDivisionError :
    print(a)   
except Exception as e :
    print(e)
finally:
    print('program will execute fr sure')

print('program completed')


'''program 5'''

a,b=1,'3'

try:
    a/b
except ZeroDivisionError :
    print(a)
except TypeError:
    int(a)/int(b)
except Exception as e :
    print(e)
finally:
    print('program will execute fr sure')

print('program completed')

'''program 6'''

a,b=1,'0'

try:
    a/b
except ZeroDivisionError :
    print(a)
except TypeError:
    int(a)/int(b)  
    ''''this is not handled so program stop here'''
except Exception as e :
    print(e)
finally:
    print('program will execute fr sure')

print('program completed')


'''program 7'''

a,b=1,'0'

try:
    a/b
except ZeroDivisionError :
    print(a)
except TypeError:
    ''''now this is handled''''
    try:
        int(a)/int(b)  
    except ZeroDivisionError :
        print(a)
except Exception as e :
    print(e)
finally:
    print('program will execute fr sure')

print('program completed')


'''recursive function'''

'''program 8'''

'''simple function''''
def simple(a,b,c):
    print(a+b+c)
simple(3,4,5)
''' if the function wanted to be called many times the its time consuming , recursive mean function calling itself again and agian''''
'''eg for recursive function'''
'''straight printing'''
def ruc_fun(x):
    if x<10:
        print(x)
        ruc_fun(x+1)
    else:
        return 0
    
'''function call'''
ruc_fun(1)

'''reverse printing'''
def ruc_fun(x):
    if x>=0:
        print(x)
        ruc_fun(x-1)
    else:
        return
    
ruc_fun(10)

'''factorial'''
def fact(x):
    if x==1 or x==0:
        return x
    else:
        return x*fact(x-1)
a=(fact(30)/((fact(2))*(fact(28))))
print(a)


'''assignments

1.fibonacci series
 
2.single dictionary a big one with n number of dictionaries with it 
  eg {{a1:{a2:{a3:{a4:5}}}},{b1:{b2:3}},{c1:3},{d1:{d2:{d3:{d4:{d5:6}}}}}}
  if key of a1 asked it shld print 5
  
3. in a 5 steps how may possible ways are ther to climb it '''

'''handshake problem'''
for i in range(1,30,-1):
    a=a+1
    print(a)

    
'''fibonacci series'''

def recur_fibo(n):
    
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
        
for i in range(1,50):
    print(recur_fibo(i))
    
'''using list and map'''
list(map(recur_fibo,range(50)))

'''optimised'''
cash={}
def recur_fibo(n):
    if n in cash.keys():
        return cash[n]
    elif n<=1:
        return n
    else:
        cash[n]=(recur_fibo(n-1)+recur_fibo(n-2))
        return cash[n]

for i in range(1,50):
    print(recur_fibo(i))
    

'''Inheritance'''

''' simple inheritance: base class and derived class ie derived class has all properties of base and itslef 
multilevel : gf--f--s
multiple: f--m--s
hiearachy--- b---d1----r  and d2 ---r
''''


''' program-1'''
class MyError(Exception):
    pass
a,b=2,3
if a<b:
    raise MyError
else:
    print(a+b)


'''program 2'''

class MyError(Exception):
    pass

def my_func(a,b):
    if a<b:
        raise MyError
    else:
        print(a+b)
        
        
try:
    my_func(2,3)
except MyError as e:
    print('my own defined error occured')
except Exception as ee:
    print(ee)
    
'''program 3'''

class MyError(Exception):
    pass

def my_func(a,b):
    if a<b:
        raise MyError
    else:
        print(a+b)
        
        
try:
    my_func(2,[3])
except MyError as e:
    print('my own defined error occured')
except Exception as ee:
    print(ee)  
    
'''program 4'''
class StudentDetails:
    def __init__(self,name,mob):
        self.name=name
        self.mob=mob
        
    def print_details(self):
        print(self.name,self.mob)

s1=StudentDetails('abcd',122344555)
s1.mob
s1.name
s1.print_details()

class StudentMarks:
    def __init__(self,sub,marks,name,mob):
        self.name=name
        self.mob=mob
        self.sub=sub
        self.marks=marks
        
    def print_marks_details(self):
        print(self.sub,self.marks)

     def print_details(self):
        print(self.name,self.mob)

s1= StudentMarks('python',76,'tgh',986)
s2.sub
s2.marks
s2.print_marks_details()
s2.print_details()

'''program 5''''

class StudentDetails:
    def __init__(self):
        self.name = None
        self.mob = None
    
    def get_details(self):
        self.name = input('enter the name of the student:')
        self.mob = input('enter the mob number of the student')
    def print_details(self):
        print(self.name,self.mob)


s1 = StudentDetails()

s1.mob
s1.name
s1.print_details()


class StudentMarks(StudentDetails):
    def __init__(self,sub,marks):
        self.sub = sub
        self.marks = marks
    
        
    def print_marks_details(self):
        print(self.sub,':',self.marks)
    
  

s2 = StudentMarks('python',76)
s2.get_details()
s2.marks

s2.mob
s2.name

s2.sub

s2.print_details()

s2.print_marks_details()


'''logging and generators
log-- history 
generators---

maping works on individual 
pandas works on grp of framework ( like objects )'''

list(range(1,27))
ord('A')
chr(65)
list(chr(range(65,91)))
a=list()
[chr(i) for i in range(65,91)]


'''basics '''
_ (protected)
__(private)
'''single layer protection''''
class DummyClass:
    
    def __init__(self):
        self.__pri=None
        self._pro=None
        self.pub=None
    
   def assigne_private_value(self,value):
       self.__pri=value  
   def print_private_value(self):
       print(self.__pri)
       
obj= DummyClass()
dir(obj)
obj.pub=4
obj.pub
obj._pro=5
obj._pro
obj.__pri

'''multi layered protection'''
class DummyClass:
    
    def __init__(self):
        self.__pri = None
        self._pro = None
        self.pub = None
    
    def _assigne_private_value(self,value):
        self.__pri = value
    def protected_private_value_assigne(self,value):
        self._assigne_private_value(value
                                    )
    def print_private_value(self):
        print(self.__pri)
    
obj = DummyClass()

obj.assigne_private_value(9876)
obj.print_private_value()         #can be done
obj.pub=4                             #can be done
obj.pub                             #can be done
''' this type of asssigning value to pri and pro is false '''
obj._pro = 5                          #not to be done
obj._pro                              #not to be done


obj.__pri = 7                         #not to be done
obj.__pri                              #not to be done


'''agrs and kwargs'''

def foo(*args):
    print(args)
    for i in args:
        print(i)
        
foo(1,2,3,4,5,6)
foo()
foo('1',3)

def foo_1(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        print(i,'-->',j)

foo_1(name = 'abced',age = 45678)


d = {'name':'rtyui','mob':98765,'place':'sdfghj'}
foo_1(**d)

print(*list(range(4)))

''' calculating time taken by the function'''
import time

st = time.time()
foo(2,3,4,5,6)
et = time.time()
print(et-st)

def time_calculator(func):
    
    def inner_dec(*args,**kwargs):
        import time
        st = time.time()
        func(*args,**kwargs)
        et = time.time()
        print(et-st)
    return inner_dec

@time_calculator
def foo(*num,**d):
    print(num)
    for i in num:
        print(i)
    print(d)

foo(3,3,4,name = 'abcd')

def hello_decorator(func): 
  
    # inner1 is a Wrapper function in  
    # which the argument is called 
      
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
  
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
  
        print("This is after function execution") 
          
    return inner1 


@hello_decorator
def foo():
    print('hi')
foo()

'''prograM'''

def foo(l=[1,2,3,4]):
    print(l)
foo()
foo([2])


'''prograM-2'''

def foo(l=[1,2,3,4]):
    print(l)
    l.append(77688)
    l[0]=93888
    print(l)
    
foo()


from functools import reduce
r_list=list()
l=[1,2,3,4,5]
for i in l:
    li=l.copy()
    li.pop(i)
    r_list.append(reduce(lambda x,y:x*y,li))
    print(r_list)
    
for i in range(len(l)):
    r_list.append(reduce(lambda x,y:x*y,l[:i]+l[i+1:]))
    
    
    
    
    
    
'''prime nos'''
import math 
for i in range(1,20):
    if i<=3:
        print(i)
    elif i>3:
        for j in range(2,int(math.sqrt(i)//1)+1):
            if i%j==0:
                print(i,'np')
                break
        else:
               print(i,'p')
    
    