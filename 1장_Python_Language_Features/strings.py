def main():
    s = "This is a string"
    print(s)
    
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    # 문자열과 바이트를 바로 합치려고 하면 에러가 뜬다.
    # print(s+b)
    
    # 문자열과 바이트를 함께 사용하려면 우선 인코딩과 디코딩을 해야 한다.
    s2 = b.decode('utf-8')
    print(s+s2)
    
    b2 = s.encode('utf-8')
    print(b+b2)
        
    
if __name__ == "__main__":
    main()
