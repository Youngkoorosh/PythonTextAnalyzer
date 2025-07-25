pragList = []

while True:
    try:
        pragList.append(input())
    except:
        break
        
c = 0
l = 0

for line in pragList:
    for char in line:
        if ord('a') <= ord(char) <= ord('z'):
            c += 1
        elif ord('A') <= ord(char) <= ord('Z'):
            c += 1
    if line.strip() != "":
        l += 1
print(l)
print(c)
