# 주소록 프로그램
# 2023-02-06
# Tarel

class Contact:
    # 생성자 - 이름, 전번, 이멜, 주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr
        
def run():
    temp = Contact("Tarel", "010-1234-5678", "abcdefg@example.com",
                   "부산시 남구 대연동")
    print(temp)

if __name__ == '__main__':
    print('주소록앱 시작합니다.')
    run()
