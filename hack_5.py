"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

result = "fooziman"

def fn_hack_5(result):
    count = 2
    if len(result) >= 3:
        while count < len(result):
            if result[0] == 'f':
                if count < 5: result = result[:count] + '-' + result[count+1:]
                else: result = result[:count] + '-' + result[count:]
            else: result = result[:count] + '-' + result[count+1:]
            count += 3
    if result[0] == 'f': return result[:-1]
    return result



print(fn_hack_5(result))