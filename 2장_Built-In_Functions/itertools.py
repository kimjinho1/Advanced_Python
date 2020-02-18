import itertools


def testFunction(x):
    return x < 40


def main():
    # cycle 함수를 통해 리스트를 무한 반복자로 만들 수 있다.
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # count 함수를 통해 간단한 카운터를 만들 수 있다.
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))

    # accumulate 함수는 리스트의 누적값이 담긴 리스트를 만들어준다. 
    vals = [10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals)
    print(list(acc))

    # 인자로 max를 줌으로써 범위 내 최대값이 담긴 리스트를 만들 수도 있다. 
    acc = itertools.accumulate(vals, max)
    print(list(acc))
        
    # chain 함수는 리스트들을 하나로 연결해준다.
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    
    # dropwhile 함수는 조건에 맞지 않는 요소들로 리스트로 만들어 주고
    # takewhile 함수는 조건에 맞는 요소들로 리스트로 만들어 준다.
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    
    
if __name__ == "__main__":
    main()
    