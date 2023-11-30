
import datetime
import math

def show_date():
   dt = datetime.datetime.now().strftime("%A, %B %d")
   tm = datetime.datetime.now().strftime("%H:%M")
   return dt


def roundup(x): 
    t1 = (int(math.ceil(x / 1000)) * 1000) / 1000
    t =  int(math.ceil(t1 / 100.0)) * 100
    #print(t)
    return t


def roundup1(x): 
    t1 = (int(math.ceil(x / 100)) * 100) / 100
    t =  int(math.ceil(t1 / 100.0)) * 100
    #print(t)
    return t


def roundup2(x):
    t = math.ceil(x)
    return t


