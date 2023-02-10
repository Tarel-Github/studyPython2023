# studyPython2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual Studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔출력 (HelloWorld)
    - 주석

```python
# desc: 콘솔출력 / 주석
print("Hello World!") # 콘솔출력함수
```

1일차 정리
코딩을 하기 앞서서 먼저 코딩을 하기 위한 환경을 구성하는 방법부터 시작
간단한 콘솔출력과 주석

## 2일차
1. 파이썬 기본
    - 변수
    - 자료형
    - 연산자
    - 흐름제어

```python
# 문자열 포맷팅
pi = 3.141592
print(f"파이값은 {pi} 입니다.")         # 파이값은 3.141592 입니다.
print(f"파이값은 {pi: 0.02f} 입니다.")  # 파이값은  3.14 입니다.
print(f"파이값은 {pi: 10.3f} 입니다.")  # 파이값은      3.142 입니다.
```

2일차 정리
print를 사용한 콘솔 명령에서 end, sep 등의 추가 명령어

변수 사용방법, 자료형의 종류

리스트와 튜플
리스트는 대괄호, 튜플은 소괄호를 사용
리스트는 값 수정이 가능하지만 튜플은 불가능 (마치 변수와 상수처럼)

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 별찍기 프로그램
    - 함수
        - 지역변수와 전역변수
        - 람다함수
        - 내장함수와 외장함수


3일차 정리
프로그래밍 언어의 기본이나 다름없는 제어문과 그를 활용한 구구단, 별찍기 예제를 완성하고
함수에 대한 부분 학습, 함수의 키워드는 def
함수 내에서 전역변수를 사용할 경우, 키워드는 global
내장함수의 경우, 파이썬 공식 홈페이지에서 확인할 수 있다.
https://docs.python.org/3/library/functions.html

## 4일차
1. 파이썬 기본
    - 가상환경
    - 객체지향 OOP
    - 패키지, 모듈

4일차 정리
객체지향을 비롯한 이론적은 부분을 위주로 학습

## 5일차
1. 파이썬 기본
    - 패키지
    - 입출력
    - 예외처리

## 6일차
1. 파이썬 기본
    - 콘솔 출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중상속

2. 파이썬 응용
    - 주소록 프로그램[소스](https://github.com/Tarel-Github/studyPython2023/blob/main/Project/address_app.py)

![실행화면](https://raw.githubusercontent.com/Tarel-Github/studyPython2023/main/images/address_app.png)

## 7일차
1. 파이썬 응용
    - 주피터 노트북
        - 노트북 생성
    - 리스트 연산 추가
    - 라이브러리 사용법
        - folium(지도 라이브러리)

주피터 노트북과 folium을 사용한 지도표시

## 8일차
1. 파이썬 응용
    - 라이브러리 사용법
        - urllib.request
    - 웹크롤링
        - 기상청 오늘의 날씨 크롤링
        - 데이터포털 OpenAIP 크롤링
        - BeautifulSoup 크롤링

![실행화면](https://raw.githubusercontent.com/Tarel-Github/studyPython2023/main/images/jupyter_folium.png)

FoliumOpenAPI 연동화면


## 9일차
1. 파이썬 응용
    - GUI 개발(PyQt)
    - 응용 학습

## 10일차
1. 파이썬 응용
    - GUI 개발
        - PyQt 위젯 계속

        