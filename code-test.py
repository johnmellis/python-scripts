# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 11:00:57 2022

@author: tina.ellis
"""


  


mylist = []

    
user = {"name":"tina","password":"abc123","objects":["object1","object2","object3"]}
user2 = {"name":"john","password":"2222","objects":["object1","object2"]}
mylist.append(user)
mylist.append(user2)
# =============================================================================
# mylist["tina"] = ["asdf",["object1","object2","object3"]]
# mylist["john"] = "john"
# mylist["malachi"] = "malachi"
# 
# mylist["tina"]["password"] = "asdf"
# mylist["tina"][0] = "password"
# print(mylist)

# =============================================================================

uservalue = "tina"
for user in mylist:
    if(user["name"] == uservalue):
        print(user["name"] + "found! Here are their objects: " + ','.join(user["objects"]))

# =============================================================================
# else:  
  #     print("this is not "+uservalue+", this is " + user["name"])
# =============================================================================

print(mylist)
[{'name': 'tina', 'password': 'abc123', 'objects': ['object1', 'object2', 'object3']}, {'name': 'john', 'password': '2222', 'objects': ['object1', 'object2']}]


for user in mylist:
    if(user["name"] == "tina"):
        mylist.pop(mylist.index(user))