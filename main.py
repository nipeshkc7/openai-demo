import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print('Hi, Im Marv the sarcastic robot \n')
print('Ask me a question...')
userInput = input()

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=userInput,
  temperature=0.9,
  max_tokens=60,
  top_p=0.3,
  frequency_penalty=0.5,
  presence_penalty=0
)

print(response.choices[0].text);