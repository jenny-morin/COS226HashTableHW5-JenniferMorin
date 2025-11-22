#Jennifer Morin
#COS226
#Hash Function HW 5

import csv as csv
import time
#Hash Function- create a good method

#Linear probing, if full insert in next avaiable spot(could loop back to the top)
    #Stop searching when you find an empty spot
#Linked list when a collide happens you append it 
#size = 59494 
size=4347430
hashTable = [None] * size
# x=0
# biggest = 0
collision = 0
itemsPlaced = 0

class DataItem:
    def __init__(self, line):
        self.movie_name = line[0]
        self.genre = line[1]
        self.release_data = line[2]
        self.director = line[3]
        self.revenue = float(line[4][1:])
        self.rating = float(line[5])
        self.min_duration  = int(line[6])
        self.production_comp  = line[7]
        self.quote  = line[8]
        #print(self.movie_name,self.genre,self.release_data,self.director,self.revenue,self.rating,self.min_duration,self.production_comp,self.quote)


def hashFunction(mydata):
    ascii_values=[]
    #for char in mydata.movie_name:
    for char in mydata.quote:
        ascii_values += [ord(char)]
    key = 0
    for i in ascii_values:
        key+=i
    return key

def hashInsert(key, mydata,collision,itemsPlaced):
    if hashTable[key] == None:
        hashTable[key]= mydata
        itemsPlaced+=1
    else:
        collision=hashCollisionLinked(key,mydata,collision)
    #itemsPlaced+=1
    return collision,itemsPlaced

def hashCollisionLinked(key,mydata,collision):
    if(type(hashTable[key])==list):
        hashTable[key].append(mydata)
    else:
        currKey = hashTable[key]
        temp=[currKey,mydata]
        hashTable[key]=temp
    collision+=1
    return collision

def hashCollision(key,mydata,collision):
    ogKey=key
    currKey = hashTable[key]
    while currKey != None:
        key += 1
        if ogKey == key:
            print("Full")
            return
        currKey = hashTable[key]
    hashTable[key]=mydata
    collision+=1
    return collision

file = "MOCK_DATA.csv"
lineCounter =0
start = time.time()
with open(file, 'r', newline='', encoding ="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if lineCounter != 0:
            myDataItem = DataItem(row)
            titleKey= hashFunction(myDataItem)
            collision,itemsPlaced=hashInsert(titleKey,myDataItem,collision,itemsPlaced)
        lineCounter+=1
end = time.time()

print(f"\n---Hash Table using the movie quotes---")
print(f"\tLines read: {lineCounter}")
print(f"\tItems added: {lineCounter-1}")
print(f"\tCollisions handled: {collision}")
print(f"\tEmpty spots remaining: {size-itemsPlaced}")
print(f"\tTime used: {end-start:0.2f} seconds\n")

#handle collision function that decides on a new key value or adds it as the linked list

#reflection is in readme
#use csv library for python

#[0]*1500
#prime numbers