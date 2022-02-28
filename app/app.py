from os import environ
import json
import requests
import streamlit as st

context = dict()
context['sentence'] = '가로가 15cm, 세로가 7cm인 직사각형의 넓이를 구하시오.'
context['sentence'] = st.text_input('수학 문제를 입력하시오.', context['sentence'])
st.write('입력된 질문:', context['sentence'])
INFERENCE_URL = environ['INFERENCE_URL']

if st.sidebar.button('제출'):
    with st.spinner('수학 코드를 생성중입니다...'):
        # response = requests.post('http://model:5000/predict', json=json.dumps(context))
        response = requests.post(f'{INFERENCE_URL}/predict', json=json.dumps(context))
        result = json.loads(response.text)
        pred = result[0]['generated_text'].lstrip(context['sentence'])
        st.code(pred, language='python')
    try:
        exec(pred)
        st.write('정답:', y)
        st.info('수학 코드가 생성되었습니다!')
    except:
        st.error('수학 코드 생성을 실패하였습니다')