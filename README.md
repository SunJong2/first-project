# 🌤️ 날씨 검색 앱

도시 이름을 입력하면 현재 날씨를 보여주고, 검색 기록을 저장하는 웹 앱

## 기술 스택
- **Backend**: Python, FastAPI
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **외부 API**: wttr.in

## 주요 기능
- 도시별 현재 날씨 조회 (온도, 체감온도, 습도, 기압, 시야)
- 검색 기록 자동 저장 및 최근 10개 표시

## 실행 방법

**1. 라이브러리 설치**
```bash
pip3 install fastapi uvicorn requests
```

**2. 서버 실행**
```bash
uvicorn main:app --reload
```

**3. 브라우저에서 접속**