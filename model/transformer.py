import bentoml
from transformers import AutoTokenizer, GPT2LMHeadModel

# model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
model = GPT2LMHeadModel.from_pretrained("./../../../Downloads/test-kogpt-trained-epoch6")
tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")

tag = bentoml.transformers.save("math_code_generation", model=model, tokenizer=tokenizer)
