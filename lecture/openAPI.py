# OpenAPI 사용하기
# - platform.openapi.com
# API KEY 발급
# 카드 등록(VISA, MASTER) + 5.5달러(보유)

#라이브러리 관리
# 1.venv(가상환경)
#   터미널 ->
# 2.Anaconda


#챗봇 만들기
# - Chat GPT : 서비스 이름(ex: 카카오톡)
#   > 인공지능 모델: GPT
#   > 무료 : 3.5    유료 : 4.0

# OpenAI 회사에서 GPT 관련 API 제공
#   - https://openai.com/blog/openai-api


from openai import OpenAI
client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "클라우드 설명해줘."}
  ]
)

print(completion.choices[0].message)