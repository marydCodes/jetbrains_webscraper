# I love ord function!

a_string = input()
caesar = []
for i in a_string:
    temp = ord(i) + 1
    a_code = chr(temp)
    caesar.append(a_code)
encoded = "".join(caesar)
print(encoded)