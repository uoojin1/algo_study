# write a method to replace all spaces in a string with %20

def urlify(str):
    str = str.strip()
    first_space = True
    url = ''
    for char in str:
        if char == " ":
            if first_space == True:
                url += "%20"
                first_space = False
            else:
                continue
        else:
            url += char
            first_space = True
    return url

print(urlify("     w adsf    sdf awf   "))