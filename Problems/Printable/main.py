start = int(input())

if start in range(32, 127):
    print(chr(start))
else:
    print("False")