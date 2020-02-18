from string import Template


def main():
    # format을 사용한 문자열 포맷팅
    str1 = "You're watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    # 템플릿 생성
    templ = Template("You're watching ${title} by ${author}")
    
    # 키워드 인자를 통해 substitute 메서드 사용
    str2 = templ.substitute(title="Advanced Python", author="Joe Marini")
    print(str2)
    
    # 사전을 통해 substitute 메서드 사용
    data = { 
        "author": "Joe Marini",
        "title": "Advanced Python"
    }
    str3 = templ.substitute(data)    
    print(str3)

    
if __name__ == "__main__":
    main()