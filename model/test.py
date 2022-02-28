import requests
import json

server_add = "http://127.0.0.1:5000/predict"
#server_add = "https://inference-hroadop25q-du.a.run.app"

if __name__ == "__main__":
	context = dict()
	context['sentence'] = """둘레가 120cm인 정오각형의 한 변의 길이는 몇 cm일까요?"""
	js = json.dumps(context)
	result = requests.post(url=server_add, headers={"content-type": "application/json"}, json=js)
	res = json.loads(result.text)
	print(res)
