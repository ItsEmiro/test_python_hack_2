"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

result = ["a","b","c","d","e"]

def fn_hack_7(result):
    if len(result) != 0:
        for i in range(len(result)):
            if i % 2 != 0: 
                result[i] = i + 1
            else:
                result[i] = str(i + 1)  

    if not result:
        result = ['0']
    return result
    
print(fn_hack_7(result))