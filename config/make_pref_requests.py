import copy
import requests7

c = copy.deepcopy(requests7.requests[0])
d = copy.deepcopy(requests7.requests[1])

a={}
for i in range(1,1000, 2):
    a[i] = c
    a[i+1] = d
with open("requests8.py", "w") as f:
    f.write("requests = " + str(a))
print(len(a))
