"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""

result = "fooziman"

def fn_hack_1(result):
    result = result.replace("o", "O",1)
    result = result.replace("i", "I")
    result = result.replace("u", "U")
    return result


print(fn_hack_1(result))