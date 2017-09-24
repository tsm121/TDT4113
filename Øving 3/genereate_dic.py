

def generate(start, stop):

    dic = {}
    index = 0

    for x in range(start,stop):


        dic[index] = chr(x)
        index += 1

    return dic


print(generate(32,127))