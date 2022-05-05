
x={'rice':30.6, 'beans':50.2, 'vegetable':75.9}
print(x)
print(x.keys())
for a in x.keys():
    print(a)
print(x.values())
for y in x.values():
    print(y)

for k, v in x.items():
    print(k,v)

print("******************")
MyDictionary={
    "One": {"Firstname": "Aarthi", "Lastname": "Palanisamy" },
    "Two": {"Firstname": "Suds", "Lastname": "Muthuswamy"}
}
print("*******************")
print("Printing MyDictionary as print(MyDictionary)")
print(MyDictionary)
print("******************")
print("Printing as key, value pair using print(a  : MyDictionary[a])")
for a in MyDictionary:
    print(a, ":", MyDictionary[a])
print("******************")
print("Printing as key value pair using k, v in MyDictionary.items()")
for k, v in MyDictionary.items():
    print(k, v)
print("****************")
print("Printing as MyDictionary.items")
print(MyDictionary.items())
print("******************")
''' printing nested values '''
print("Print as flattening the dictionary")
for a in MyDictionary:
    for b in MyDictionary[a]:
        print(a, ":", b, ":", MyDictionary[a][b])

