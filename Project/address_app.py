# 주소록 프로그램
# 2023-02-06
# Tarel
import os # 운영체제용 모듈


# 2. 클래스 생성
class Contact:
    # 생성자 - 이름, 전번, 이멜, 주소
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 4. __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n'
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}\n')
        return str_res
    
    # 10. 객체 존재 여부 확인
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False
    
    # 12. 각 멤버변수에 접근하는 함수
    # getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name
    def getPhoneNum(self) -> str:
        return self.__phone_num
    def getEmail(self) -> str:
        return self.__email
    def getAddr(self) -> str:
        return self.__addr
    




# 5. 사용자 입력
def set_contact():
    name, phone_num, email, addr = input('정보입력(이름, 전번, 이메일, 주소) ').split('/')
    # print(name, phone_num, email, addr)
    # 7. Contact 객체 만들기
    contact = Contact(name, phone_num, email, addr)
    return contact

# 9. 주소록 출력
def get_contact(list):
    for item in list:
        print(item)
        print('====================')


# 10. 주소록 삭제
def del_contact(list, name):
    count = 0
    for i, item in enumerate(list): #리스트 인덱스 추가생성
        if item.isNameExist(name):
            count += 1
            del list[i] # 리스트삭제

    if count > 0:   # 11. 메시지 출력
        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다.')
    #     print(item)
    # name = input('이름을 입력해주세요: ')
    # if name in list:
    #     list.remove(name)

#13. 주소록 파일 저장
def save_contacts(list):
    file = open('C:\Source\studyPython2023\Project\contact.txt', 'w', encoding='utf-8')
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}\n'
        file.write(f'{text}\n')
    file.close()

# 추가. 화면클리어
def clear_console():
    command = 'clear'#리눅스나 유닉스 화면 클리어 명령어
    if os.name in ('nt', 'dos'): #windows운영체제라면
        command = 'cls' #윈도우 화면 클리어 명령어
    os.system(command)
    

# 6. 메뉴표시
def get_menu():
    str_menu = ('주소록앱 v0.5\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱종료')
    print(str_menu)
    menu = int(input('메뉴입력: '))
    return menu

# 3. 전체실행
def run():
    contacts = list()   # 주소를 담기 위한 빈 리스트를 생성
#     temp = Contact("Tarel", "010-1234-5678", "abcdefg@example.com",
#                    "부산시 남구 대연동")
#     print(temp)
    clear_console()
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: #8. 연락처 추가
            contact = set_contact()
            contacts.append(contact)
            input('주소록 입력 성공')
            clear_console()
            
        elif sel_menu == 2: #9. 연락처 출력
            get_contact(contacts)
            input('주소록 출력 완료')
            clear_console()

        elif sel_menu == 3: #10. 연락처 삭제
            name = input('삭제할 이름을 입력해주세요: ')
            del_contact(contacts, name)
            input()
            clear_console()
        
        elif sel_menu == 4:
            save_contacts(contacts)
            
            break
        else:
            clear_console()
        
if __name__ == '__main__':
    run()
    
