my = {"manju": 90, "roja": 67, "pooja": 89}

for name, score in my.items():
    if score >= 89:
        print(name, score)#manju 90 pooja 89


for i in my:
    if my[i] >= 89:
        print(i)#manju pooja

for i in my:
    a={i:len(i)}
    print(a)
