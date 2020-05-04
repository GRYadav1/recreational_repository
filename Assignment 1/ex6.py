'''
Created on Aug 30, 2018

@author: gaura
'''

def example_decorator(argFunc):
    print("Before calling parameter function..")
    def inside_func():
        argFunc();
                
    return inside_func 

@example_decorator
def test_python():
    print("Welcome to Python Programming...");
    
    


test_python();


    
