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

from openai import OpenAI
 
client = OpenAI(
  api_key="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"
)
 
response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)
 
print(response.output_text);
