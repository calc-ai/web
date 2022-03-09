import json
import bentoml
from bentoml.io import JSON

generator = bentoml.transformers.load_runner(tag="math_code_generation:latest", tasks='text-generation')

svc = bentoml.Service("generate", runners=[generator])

@svc.api(input=JSON(), output=JSON())
def predict(json_input: JSON):
	print(json_input, type(json_input))
	inp = json.loads(json_input)
	result = generator.run(inp['sentence'])
	return result
