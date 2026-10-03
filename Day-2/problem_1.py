# student Dictonary


dict1 = {"name":"Gautam",
        "Number":"9457899999",
        "city":"Jaipur",
        "Gender":"male"}
print(dict1)

print(dict1["name"])
print(dict1["Number"])
dict1["city"] = "Delhi"



dict1["college"] = "Maism"
print(dict1)


for i in dict1.keys():
    print(i)

for j in dict1.values():
    print(j)

for i in dict1.items():
    print(i)


