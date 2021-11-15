# Snkrs_KR_DrawChecker_Discord
나이키 코리아 드로우 결과 디스코드 알림 프로그램

## 개요
Selenium, Chromedriver를 이용한<br> 
나이키 코리아 드로우 응모결과 디스코드 알림 프로그램.

## 실행 방법
정보를 입력 후, 소스 코드를 내려받아 실행한다.
 
## 실행 파일 사용시 
```pyinstaller```패키징 후 실행<br>
 
### 실행 전 준비 
* 본인의 크롬 브라우저의 버전과 맞는 크롬 드라이버 다운로드<br>
  - [크롬 드라이버 다운로드 링크](https://chromedriver.chromium.org/downloads)  
* 크롬 드라이버를```Testdraw.py```,```discord_hooks.py```,```exe```와 같은 폴더 내에 다운로드 한다.
* ```Testdraw.py```실행.

## 실행 순서
### 1. 코드 실행 
```Testdraw.py```를 파이썬을 통해 실행한다.<br>
### 2. 모듈 다운로드
```pip install 모듈명```을 파이썬 터미널을 통해 다운로드 한다.<br>
### 3. 계정 정보 입력
```SendID```변수에 사용할 계정의 아이디와 비밀번호를 입력한다.<br> 
### 4. 디스코드 웹 토큰 설정
```discord_webhook = ''```변수에 디스코드 웹훅 토큰을 입력한다.<br> 
### 5. 실행파일 만들기
```pyinstaller 모듈을 사용하여 exe 파일 추출 및 실행```<br>

## 실행 결과
<img src="https://github.com/coper3976/SnkrsKR_DrawChecker/blob/main/%EC%8B%A4%ED%96%89%20%EA%B2%B0%EA%B3%BC.png">
