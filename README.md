# seojh
OpenAI사의 GPT  모델을 활용한 챗봇 개발하기

# VScode를 사용한 Python 개발환경 구축
    1. VScode 설치
    2. Python 설치(Python.org) + 환경변수(path) 체크!
    3. VScode 에서 Extentions(Python, Python Extension Pack, gitgraph or gitlens) 추가
    4. VScode 에서 Github 계쩡으로 로그인(연동)
    5. Github 에서 Repository(프로젝트) 생성
    6. VScode 에서 "git clone repository"로 5번에서 생성한 프로젝트 내려받기
    7. 가상환경 생성(venv) : 가상환경 구축 참조
    8. VScode 에서 Python: Select Interpreter 설정(Ctrl + Shift + p) -> venv 설정


# Python 가상환경 구축
## 1. venv
    -   python - m venv ./venv
    -   .\venv\Scripts\activate
    -   pip install [라이브러리명](가상환경 라이브러리 설치)