"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

result = ["a","b","c","d","e"]
def fn_hack_6(result):
    final = []
    aux = 1
    for i in range(len(result)):
        if aux % 2 != 0:
            final.append(str(aux))
            if aux < len(result):
                final.append("-")
        aux += 1

    if not final:
        final = ["0"] 

    return final



print(fn_hack_6(result))