'''
 dict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : {
                        "" : "1"
                    }
                }
            }
        }

output: {
            "Key1" : "1",
            "Key2.a" : "2",
            "Key2.b" : "3",
            "Key2.c.d" : "3",
            "Key2.c.e" : "1"
'''
dict={"Key1" : "1","Key2" : {"a" : "2", "b" : "3","c" : {"d" : "3", "e" : { "" : "1"}}}}
print(dict)
for a in dict:
    print(a, ":", dict[a])
print("*****************")
print("printing nested dictionary")
for a in dict:
    for b in dict[a]:
        for c in dict[a][b]:
            for d in dict[a][b][c]:
                print(a, ":", b, ":", c, ":", d, dict[a][b][c][d])



