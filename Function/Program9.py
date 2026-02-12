name = "abc"
print(name)

def fun1():
    name = "def"
    print(name)

print(name)
fun1()

def fun2():
    global name
    name = "ghi"
    print(name)

print(name)
fun2()
print(name)
