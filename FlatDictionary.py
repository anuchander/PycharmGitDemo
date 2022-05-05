'''
Another way to flatten dictionary:

import flatdict
d =  flatdict.FlatDict(data, delimiter='.')
print(d)
'''
def flatten_dictionary(dictionary):
    def recursor(parentK, givenVal):
        if type(givenVal) != dict:
            o[parentK] = givenVal
            return
        else:
            for eachChildK in givenVal.keys():
                if eachChildK == "":
                    recursor(parentK, givenVal[eachChildK])
                else:
                    if parentK != "":
                        recursor(parentK + "." + eachChildK, givenVal[eachChildK])
                    else:
                        recursor(eachChildK, givenVal[eachChildK])

    o = {}
    for eachK in dictionary.keys():
        recursor(eachK, dictionary[eachK])
    return o

dict={"Key1" : "1","Key2" : {"a" : "2", "b" : "3","c" : {"d" : "3", "e" : { "" : "1"}}}}
flatten_dictionary(dict)