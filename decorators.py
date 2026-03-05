# decortor - a fucntion that extencds that behvior of another function 
import functools

def adding_each_scoop(limit): 
    msg = "added scoop"
    while limit != 0: 
        yield msg 
        limit-=1
    print("scoops added")


#decorator
def add_sprinkles(func): 
    @functools.wraps(func) # so you dont lose the idenity of the og method 
    def wrapper(*args, **kwargs): # need to have this so that it doesnt get run anytime the decortor is applied 
        print("you add sprinkles")
        return func(*args, **kwargs) # actualy returns the funcs return value
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):  
        print("adding fudge")
        return func(*args, **kwargs)
    return wrapper

@add_fudge 
@add_sprinkles
def get_icecream(flavor):
    print("hello")
    generator = adding_each_scoop(3)
    for scoop in generator: 
        print(scoop)
    print(f"heres your {flavor} icecream")

get_icecream("strawbery")