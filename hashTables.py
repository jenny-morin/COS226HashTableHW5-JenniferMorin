#Jennifer Morin
#COS226
#Hash Function HW 5

import csv as csv
import time
#Hash Function- create a good method

#Linear probing, if full insert in next avaiable spot(could loop back to the top)
    #Stop searching when you find an empty spot
#Linked list when a collide happens you append it 
size = 59494 
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
    for char in mydata.movie_name:
        ascii_values += [ord(char)]
    key = 0
    for i in ascii_values:
        key+=i
    # if x==0:
    #     biggest = key
    #     x+=1
    # elif key > biggest:
    #     biggest = key
    return key#,x,biggest
    #print(key) 
    #print(ascii(mydata.movie_name))
def hashInsert(key, mydata,collision,itemsPlaced):
    if hashTable[key] == None:
        hashTable[key]= mydata
        #print(hashTable[key])
    else:
        #print("I am not adding anythinggg")
        collision=hashCollision(key,mydata,collision)
    itemsPlaced+=1
    return collision,itemsPlaced

def hashCollision(key,mydata,collision):
    ogKey=key
    currKey = hashTable[key]
    while currKey != None:
        key += 1
        if ogKey == key:
            print("Full")
            return
        currKey = hashTable[key]
    #print("put her there")
    hashTable[key]=mydata
    #hashInsert(key,mydata)
    collision+=1
    return collision

file = "MOCK_DATA.csv"
lineCounter =0
start = time.time()
with open(file, 'r', newline='', encoding ="utf8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print(row)
        if lineCounter != 0:
        #create a DataItem from row
            myDataItem = DataItem(row)
            # titleKey,x,biggest = hashFunction(myDataItem,x,biggest)
            titleKey= hashFunction(myDataItem)
            #print(titleKey)
            collision,itemsPlaced=hashInsert(titleKey,myDataItem,collision,itemsPlaced)
        #print(biggest)
            
        #feed the appropriate feild into the hash function to get a key
        #mod the key value by the hash table length
        #try to insert DataItem into hash table
        #handle any collisions
        lineCounter+=1
end = time.time()
print(f"Lines read: {lineCounter}")
print(f"Items added: {itemsPlaced}")
print(f"Collisions handled: {collision}")
print(f"Empty spots remaining: {size-itemsPlaced}")
print(f"Time used: {end-start:0.2f} seconds")

#handle collision function that decides on a new key value or adds it as the linked list

#reflection is in readme
#use csv library for python

#[0]*1500
#prime numbers