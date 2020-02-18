def main():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # iterable 객체: 반복 가능한 객체 
    # iterator 객체: 값을 차례대로 꺼낼 수 있는 객체 
    # next 함수를 사용할 때마다 iterator의 첫 번째, 두 번째, 세 번째 값이 출력된다.
    i = iter(days)
    print(next(i))  # Sun
    print(next(i))  # Mon
    print(next(i))  # Tue

    # 인덱스를 출력하고 싶을 때는 enumerate 함수를 사용해주자.
    for m in range(len(days)):
        print(m+1, days[m])

    # 아래와 같이 짜지 말자!
    #for m in range(len(days)):
    #    print(m+1, days[m])

    # zip 함수는 말 그대로 2개를 하나로 압축해준다.
    for m in zip(days, daysFr):
        print(m)

    # 이런 식으로 zip과 enumerate 동시에 사용할 수도 있다.
    for i, m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")


if __name__ == "__main__":
    main()
