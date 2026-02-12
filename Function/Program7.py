name = "Harshita"
print(name)

def fun():
    global name
    print(name)
    name = "Gupta"
    lang = "Python"
    print(lang)

fun()
print(name)
