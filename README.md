# Python GUI - Shortcut Launcher
## 목표 및 목적

### 문제 분석
 + 단축키 프로그램 
    + 메인 윈도우 창 띄우기
        + 윈도우 크기 조정 가능
    + 버튼 구현 
        + 2열 4행 배치
        + 윈도우 크기에 따라 버튼 크기 결정
    + 버튼이 눌리면 명령 실행
    + 메뉴
        + 프로그램 설정: 새로운 윈도우에 표현
        + 프로그램 정보
        + 종료 : 프로그램을 종료
    + 프로그램 색상 지정

## 개발 사양
### 하드웨어
+ CPU : AMD Ryzen 7 4800H with Radeon Graphics, 2900Mhz, 8 코어, 16 논리 프로세서
+ RAM : 32.0GB
+ SSD : 1TB
+ GPU : AMD Radeon(TM) Graphics

### 소프트웨어
+ OS : Microsoft Windows 10 Education
+ 개발 스택 : Tkinter
+ 개발 프로그램 : Visual Studio Code
+ 개발 언어 : Pyhron v3.9

### 코드룰

    #변수명
    test_variable = 1

    #클래스명
    class test_class:
        def __init__(self):
            #프로퍼티명
            self.test_property = 1

        #메소드명
        def test_method(self):
            print(self.test_property)

    if __name__ == "__main__":
        test_variable = test_class(2)
        test_variable.test_method()

