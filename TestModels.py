import openai
with open("openai_token.txt", "r") as f:
    openai.api_key = f.read()
models = openai.Model.list()
for model in models['data']:
    print(model['id'])