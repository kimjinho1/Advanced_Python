def main():
    False_list = [False, 0, 0.0, 0j, '', (), [], {}, set(), range(0)]
    True_list = [True, 1, 2, 'abc', (3,4,5), [6,7], range(8)]

    def value_testing(li):
        """리스트 값들이 참인지 거짓인지 출력해주는 함수이다."""
        for value in li:
            print('{0} is {1}'.format(value, bool(value)))


    value_testing(False_list) # 모두 거짓임을 확인 할 수 있음.
    print()
    value_testing(True_list) # 모두 참임을 확인 할 수 있음.


if __name__ == "__main__":
    main()
