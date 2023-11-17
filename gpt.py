from ratelimit import limits, sleep_and_retry
import openai
from settings import API_KEY

openai.api_key = API_KEY

MINUTE = 60

@sleep_and_retry
@limits(calls=40, period=MINUTE)
def create_sentence(word, fake=False):
  if fake:
    return 'Test sentence'
  prompt = 'Create a sentence with word "{}"'.format(word)
  response = openai.Completion.create(
    model="text-davinci-002",
    prompt=prompt,
    temperature=0.6,
    max_tokens=200,
  )
  return response.choices[0].text
