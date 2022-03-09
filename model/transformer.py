import bentoml
from transformers import AutoTokenizer, GPT2LMHeadModel

model = GPT2LMHeadModel.from_pretrained("/Users/taekkim/Downloads/model")
tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")

tag = bentoml.transformers.save("math_code_generation", obj=model, tokenizer=tokenizer)
