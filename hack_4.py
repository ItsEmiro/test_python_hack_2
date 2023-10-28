"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

result = "fooziman"

def fn_hack_4(result):
    result = result if len(result) <= 3 else result[1:-1]
    return result



print(fn_hack_4(result))