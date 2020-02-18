def main():
    # bool 함수가 말고도 인자가 True일 경우 True를 리턴해주는 all,
    # False일 경우 True를 리턴해주는 any 함수가 존재한다.
    list1 = [1, 2, 3, 0, 5, 6]
    
    print(any(list1))
    print(all(list1))
    
    # min과 max 함수는 시퀸스의 최솟값과 최댓값을 리턴해준다.
    print("min: ", min(list1))
    print("max: ", max(list1))    
    
    # sum 함수는 시퀸스의 합을 리턴해준다.
    print("sum: ", sum(list1))
    
    
if __name__ == "__main__":
    main()
    