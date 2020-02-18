# 항상 파일의 맨 위에 import 문을 놓는다.
import sys
import os


# 함수와 클래수는 빈 줄 두개, 매서드는 빈 줄 하나로 구분한다.
class MyClass():
    def __init__(self):
        self.prop1 = "my class"

    def method1(self, arg1):
        pass
    
    
# 한 줄의 문자 길이는 79자 이하여야 한다.
def main():
    # Long comments, like this one that flow across several lines, are
    # limited to 72 characters instead of 79 for lines of code.
    cls1 = MyClass()
    cls1.prop1 = "hello world"
    
    
if __name__ == "__main__":
    main()

# 이 외에도 한 줄로 된 if 문, for, while loop, except 복합문을 쓰지 않는다거나  
# 들여쓰기는 space 4번을 이용한다거나 등등 다양한 가이드가 있다.  
# 자세한 건 https://www.python.org/dev/peps/pep-0008/ 를 참고하자.