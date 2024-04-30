def _validate(f):
    def inner(sides):
        a, b, c = sides
        return (
            (a + b >= c)
            and (b + c >= a)
            and (a + c >= b)
            and not (len(set(sides)) == 1 and a == 0)
            and f(sides)
        )

    return inner


@_validate
def equilateral(sides):
    return len(set(sides)) == 1


@_validate
def isosceles(sides):
    return len(set(sides)) <= 2 


@_validate
def scalene(sides):
    return len(set(sides)) == 3
