
a1=1
a2=1

q1=1
q2=1
epsilon=0.01
while (abs(q1-q2)>epsilon) or q1==q2:
    q2=q1
    q1=a1/a2
    a1,a2=a2,a2+a1
print(q2)