from os import environ
import json
import requests
import streamlit as st

context = dict()
context['sentence'] = '가로가 15cm, 세로가 7cm인 직사각형의 넓이를 구하시오.'
context['sentence'] = st.text_input('수학 문제를 입력하시오.', context['sentence'])
st.write('입력된 질문:', context['sentence'])
classes = [
    '산술연산',
    '순서정하기',
    '조합하기',
    '수 찾기-1',
    '수 찾기-2',
    '수 찾기-3',
    '크기 비교',
    '도형',
]
#     산술연산	주어진 특성 상황에서 연산식을 구하고 원하는 값을 구하는 유형
# 2	순서정하기	줄을 서는 상황이 주어지고 요구하는 값을 구하는 유형
# 3	조합하기	주어진 특정 상황에서 가능한 경우의 수를 구하는 유형
# 4	수 찾기-1	주어진 숫자 셋에서 특정 조건(가장 큰 수, 가장 작은 수 등)을 만족하는 수를 찾는 유형
# 5	수 찾기-2	문제에 미지수(A, B, C)가 주어지고 미지수가 포함된 연산 식 조건을 만족하는 미지수를 찾는 유형
# 6	수 찾기-3	연산을 잘못했을 때의 상황이 주어지고, 바르게 연산했을 때의 결과를 찾는 유형
# 7	크기 비교	주어진 상황에서 상대적인 크기를 비교하여 어떤 것이 더 큰 지를 찾는 유형
# 8	도형
#INFERENCE_URL = environ['INFERENCE_URL']

if st.sidebar.button('제출'):
    with st.spinner('수학 코드를 생성중입니다...'):
        response = requests.post('http://model:3000/predict', json=json.dumps(context))
        #response = requests.post(f'{INFERENCE_URL}/predict', json=json.dumps(context))
        result = json.loads(response.text)
        pred = result[0]['generated_text'].lstrip(context['sentence'])
        cls, _, *pred = pred
        st.info(f'모델이 예측한 이 문제 유형은 "{classes[int(cls) - 1]}"입니다.')
        pred = ''.join(pred)
        st.code(pred, language='python')
    try:
        exec(pred)
        st.write('정답:', y)
        st.info('수학 코드가 생성되었습니다!')
    except:
        st.error('수학 코드 생성을 실패하였습니다')
