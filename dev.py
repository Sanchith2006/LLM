from gpt4all import GPT4All
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf") 
x=input('enter the question:')
output = model.generate(x, max_tokens=20)
print(output)