"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""

result = "fooziman"

def fn_hack_2(result):
    vocales = 'aeiou'
    result = ''.join(([x for x in result if x not in vocales]))
    return result


print(fn_hack_2(result))