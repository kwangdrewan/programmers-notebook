import openai
from openai.api_resources import Answer

openai.api_key = "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"

context = "My bedroom is messy. I leave socks all over the place."
question = "How can I ensure my bedroom stays organized?"

response = openai.Answer.create(
    engine="davinci",
    prompt=context,
    question=question,
    max_tokens=1024,
)

answer = response.answers[0]
print(answer)
