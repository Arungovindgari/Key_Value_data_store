import threading 
from threading import*
import time

y={}

def create(key,value,timeout=0):
    if key in y:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(y)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    y[key]=l
            else:
                print("error: Memory limit exceeded!!! ")
        else:
            print("error: Invalind key_name!!! key_name must contain only alphabets and no special characters or numbers")
            
def read(key):
    if key not in y:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=y[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                string=str(key)+":"+str(b[0]) 
                return string
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            string=str(key)+":"+str(b[0])
            return string
        
def delete(key):
    if key not in y:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        b=y[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del y[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired")
        else:
            del y[key]
            print("key is successfully deleted")

def modify(key,value):
    b=y[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in y:
                print("error: given key does not exist in database. Please enter a valid key")
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired")
    else:
        if key not in y:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            y[key]=l
