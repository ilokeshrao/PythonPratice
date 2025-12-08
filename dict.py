
Marks =  {
    "name" :  "lokesh",
    "age" : 21,
    "address": "rewari",
    "add" :"eeee"
}


# print(Marks.items())
# print(Marks.keys())
# print(Marks.values())
# Marks.update({"name": "lokesh"})  
# print(Marks)

# print(Marks.get("name"))  # None
# print(Marks["name"])      #Error 
# print(Marks.pop("add"))
# print(Marks.popitem())
# print(Marks.setdefault("gurgoan"))

copymarks = Marks.copy()

Marks["age"]=  25

print(Marks)
print(copymarks)

print(Marks.update({"name": "depuu"}))
print(Marks)




