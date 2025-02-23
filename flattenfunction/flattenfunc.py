first_input = [[1,'a',['cat'], 2],[[[3]],'dog'],[4,5]]
v = []
def f(i):
    if isinstance(i, int) == True:
        return i
    elif isinstance(i, str) == True:
        return str(i)
    elif isinstance(i, list) == True:
        if i[0] == "cat":
            v.append(first_input[0][2][0])
        elif i[0][0] == 3:
            v.append(first_input[1][0][0][0])
x = [e for e in first_input[0] if f(e)]
y = [e for e in first_input[1] if f(e)]
z = [e for e in first_input[2] if f(e)]
a = x + y + z + v
print(a)

second_input = [[1, 2], [3, 4], [5, 6, 7]]
d = second_input.copy()
d.reverse()
def g(x,y,z):
    x = d[0]
    y = d[1]
    z = d[2]
    x.reverse()
    y.reverse()
    z.reverse()
    list_all = [x]+[y]+[z]
    print(list_all)
l = []
l2 = []
l3 = []
print(g(l,l2,l3))
