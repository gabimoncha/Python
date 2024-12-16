import turtle
import secrets

t = turtle.Turtle()
num = secrets.SystemRandom().randint(1, 1000)
t.right(num)
t.speed(num)
t.left(num)


def tree(i):
    if i < 10:
        return
    else:
        t.right(15)
        t.forward(15)
        t.left(20)
        t.backward(20)
        tree(2 * i / 5)
        t.left(2)
        tree(3 * i / 4)
        t.left(2)
        tree(i / 2)
        t.backward(num / 5)
        tree(secrets.SystemRandom().randint(1, 100))
        tree(secrets.SystemRandom().randint(1, num))
        tree(secrets.SystemRandom().randint(1, num / 2))
        tree(secrets.SystemRandom().randint(1, num / 3))
        tree(secrets.SystemRandom().randint(1, num / 2))
        tree(secrets.SystemRandom().randint(1, num))
        tree(secrets.SystemRandom().randint(1, 100))
        t.forward(num / 5)
        t.right(2)
        tree(3 * i / 4)
        t.right(2)
        tree(2 * i / 5)
        t.right(2)
        t.left(10)
        t.backward(10)
        t.right(15)
        t.forward(15)
        print("tree execution complete")


def cycle(i):
    if i < 10:
        return
    else:
        try:
            tree(secrets.SystemRandom().randint(1, i))
            tree(secrets.SystemRandom().randint(1, i * 2))
        except:
            print("An exception occured")
        else:
            print("No Exception occured")
        print("cycle loop complete")


def fractal(i):
    if i < 10:
        return
    else:
        cycle(secrets.SystemRandom().randint(1, i + 1))
        cycle(secrets.SystemRandom().randint(1, i))
        cycle(secrets.SystemRandom().randint(1, i - 1))
        cycle(secrets.SystemRandom().randint(1, i - 2))
        print("fractal execution complete")


fractal(secrets.SystemRandom().randint(1, 200))
print("Execution complete")
turtle.done()
