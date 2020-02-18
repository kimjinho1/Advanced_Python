def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >= 80 and x < 90):
        return "B"
    elif (x >= 70 and x < 80):
        return "C"
    elif (x >= 65 and x < 70):
        return "D"
    return "F"


def main():
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJinhOKim"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # filter 함수는 특정 조건으로 걸러서 걸러진 요소들로 
    # iterator 객체를 만들어서 리턴해준다.
    odds = list(filter(filterFunc, nums))
    print(odds)

    # 꼭 숫자가 아니어도 상관없다.
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # map 함수는 반복가능한 iterable 객체를 받아서 
    # 각 요소에 함수를 적용해준다.
    squares = list(map(squareFunc, nums))
    print(squares)

    letters = list(map(toGrade, grades))
    print(letters)


if __name__ == "__main__":
    main()
