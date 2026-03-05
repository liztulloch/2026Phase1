# decortor - a fucntion that extencds that behvior of another function 
from contextlib import contextmanager

#decorator
def add_sprinkles(func): 
    def wrapper(*args, **kwargs): # need to have this so that it doesnt get run anytime the decortor is applied 
        print("you add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):  
        print("adding fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge 
@add_sprinkles
def get_icecream(flavor):
    print("hello")

    print(f"heres your {flavor} icecream")

get_icecream("strawbery")