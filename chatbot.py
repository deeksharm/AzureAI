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
