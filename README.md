# Snkrs_KR-DrawChecker

Snkrs_KR-DrawChecker for README.md

## 개요
여러 계정을 사용하는 사용자들의 편의를 위한<br> 
나이키 코리아 드로우 응모결과 확인 프로그램.

## 실행 방법
업로드한 실행 파일을 실행하거나, 소스 코드를 내려받아 파이썬으로 실행한다.
 
## 실행 파일 사용시 
```DrawChecker.exe```파일 실행<br>
```Mac os``` 지원X
 
### 실행 전 준비 
* 본인의 크롬 브라우저의 버전과 맞는 크롬 드라이버 다운로드<br>
  - [크롬 드라이버 다운로드](https://chromedriver.chromium.org/downloads)  
* 크롬 드라이버를 같은 ```코드``` 또는 ```exe``` 폴더 내에 다운로드 한다.
* ```코드```를 파이썬을 통해 실행한다.

## 실행 순서
### 1. 코드 실행 
```코드```를 파이썬을 통해 실행한다.<br>
### 2. 모듈 다운로드
```pip install 모듈명```을 파이썬 터미널을 통해 다운로드 한다.<br>
### 3. 계정 정보 입력
```SendID```변수에 사용할 계정의 아이디와 비밀번호를 입력한다.<br> 
### 4. 실행파일 만들기
```pyinstaller -F --add-binary "C:\Users\user\Desktop\chromedriver\chromedriver.exe;." DrawChecker.py```를<br>
*(본인의 파이썬 코드 파일 위치로 지정해야함)* 터미널로 한번 실행해주면 exe파일로 추출된다.  

## 주의사항
### 1. **반드시 크롬 드라이버와 코드 또는 exe파일은 같은 위치에 있어야함** 
### 2. ****



