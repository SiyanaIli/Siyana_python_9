grades=[95,82,67,54,100,73,88,42]

excellent=[]
good=[]
passed=[]
failed=[]

for g in grades:
    if g<50:
        failed.append(g)
    else:
        if g<70:
            passed.append(g)
        else:
            if g<90:
                good.append(g)
            else:
                excellent.append(g)

print("excellent:", excellent)
print("good:", good)
print("pass:", passed)
print("fail:", failed)