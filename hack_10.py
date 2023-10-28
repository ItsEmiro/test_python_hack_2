"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

result = [{"a":"b"},{"c","d"},{"e":"f"}]

def fn_hack_10(array: list):
    result = []
    key = ''
    value = ''
    i = 0
    for j in range(len(array)):
        i += 1
        key = str(i)
        i += 1
        value = str(i)
        if j % 2 == 0: result.append({key: value})
        else: result.append({key, value})
    
    return result



print(fn_hack_10(result))