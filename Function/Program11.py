def fun1():
    name = "Harshita"

    def fun2():
        nonlocal name
        name = "Gupta"

    fun2()
    print(name)

fun1()
